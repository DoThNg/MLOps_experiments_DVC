from ml_project.evaluate import evaluate_model
from ml_project.prepare_data import move_split_data
import yaml
import pandas as pd
import os
import shutil

from dagster import asset, Definitions
from dagster.utils import file_relative_path 

from pycaret.classification import ClassificationExperiment

@asset
def prepare_data():
    return move_split_data()

@asset
def auto_ml(prepare_data):
    with open(file_relative_path(__file__, "./params.yaml")) as yaml_file:
        params = yaml.safe_load(yaml_file) 

    train_data = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["train_file"])) 
    
    exp = ClassificationExperiment()
    exp.setup(train_data, target = "Cover_Type", 
              fold = 3,
              log_experiment = True, 
              experiment_name = "auto_ml_v1",
              log_plots = True, 
              session_id = 12)
    
    best_model = exp.compare_models(include = ['rf', 'dt'])

    # save pipeline
    exp.save_model(best_model, "ml_model") 

    base_dir = os.getcwd()

    # Move saved model to folder model
    model_src = os.path.join(base_dir, "ml_model.pkl")
    model_dst = os.path.join(base_dir, "model")

    if os.path.isfile(os.path.join(model_dst, "ml_model.pkl")):
        os.remove(os.path.join(model_dst, "ml_model.pkl"))
    
    shutil.move(model_src, model_dst)

@asset
def evaluate_ml_model(auto_ml):

    test_model_acc, test_model_auc, model_clf = evaluate_model()

    # Print accuracy and auc results for test dataset
    print("model accuracy: {}".format(test_model_acc))
    print("model auc: {}".format(test_model_auc))                    
    
    # Print the best model
    print(model_clf)

defs = Definitions(
    assets=[prepare_data, auto_ml, evaluate_ml_model]
)