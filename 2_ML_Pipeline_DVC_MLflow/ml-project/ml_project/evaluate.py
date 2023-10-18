from sklearn.metrics import accuracy_score, roc_auc_score, ConfusionMatrixDisplay
import pickle
import pandas as pd
import os
import yaml
from dagster.utils import file_relative_path

def evaluate_model(ml_data_category: str):
    """"
    input: 
    - ml_data_category: train_file or test_file
    output:
    metrics: accuracy, auc, 
    confusion matrix
    """

    with open(file_relative_path(__file__, "./params.yaml")) as yaml_file:
        params = yaml.safe_load(yaml_file)
  
    model_path = params["train"]["dir"]

    with open(model_path + "/train_model.pkl", "rb") as model_file:
        model_clf = pickle.load(model_file)
    
    data = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"][ml_data_category]))

    data_X, data_y = data.drop("Cover_Type", axis = 1), data["Cover_Type"]
    
    data_y_pred = model_clf.predict(data_X)
    data_y_prob_pred = model_clf.predict_proba(data_X)

    model_acc = accuracy_score(data_y, data_y_pred)
    model_auc = roc_auc_score(data_y, data_y_prob_pred, multi_class='ovr')

    cm = ConfusionMatrixDisplay.from_predictions(y_true=data_y,
                                                 y_pred=data_y_pred)

    return model_acc, model_auc, cm
           


