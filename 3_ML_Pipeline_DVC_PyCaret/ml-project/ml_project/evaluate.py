# import pickle
from pycaret.classification import load_model, predict_model
from sklearn.metrics import accuracy_score, roc_auc_score, ConfusionMatrixDisplay
import pandas as pd
import os
import yaml
from dagster.utils import file_relative_path

def evaluate_model():
    """"
    output: accuracy and auc
    """

    with open(file_relative_path(__file__, "./params.yaml")) as yaml_file:
        params = yaml.safe_load(yaml_file)
    
    data = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["test_file"]))

    data_X, data_y = data.drop("Cover_Type", axis = 1), data["Cover_Type"]

    base_dir = os.getcwd()
    model_clf = load_model(os.path.join(base_dir, "model/ml_model"))

    data_y_pred = predict_model(estimator = model_clf, data = data_X) 
    data_y_prob_pred = predict_model(estimator = model_clf, data = data_X, raw_score = True)

    model_acc = accuracy_score(data_y, data_y_pred.iloc[:,-2])
    model_auc = roc_auc_score(data_y, data_y_prob_pred.iloc[:,-7:].to_numpy(), multi_class='ovr')

    return model_acc, model_auc, model_clf
           


