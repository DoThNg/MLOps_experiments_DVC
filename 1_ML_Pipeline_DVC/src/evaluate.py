from dvclive import Live
from sklearn.metrics import accuracy_score, roc_auc_score
import pickle
import pandas as pd
import os
import yaml
import numpy as np
import matplotlib.pyplot as plt

def evaluate_model(ml_model, data, ml_data_category, dvc_live):
    
    data_X, data_y = data.drop("Cover_Type", axis = 1), data["Cover_Type"]
    
    data_y_pred = ml_model.predict(data_X)
    data_y_prob_pred = ml_model.predict_proba(data_X)

    # Log ML metrics:
    model_acc = accuracy_score(data_y, data_y_pred)
    model_auc = roc_auc_score(data_y, data_y_prob_pred, multi_class='ovr')

    if not dvc_live.summary:
        dvc_live.summary = {"model_acc" : {}, "model_auc" : {}}
    dvc_live.summary["model_acc"][ml_data_category] = model_acc
    dvc_live.summary["model_auc"][ml_data_category] = model_auc
    
    # Log confusion matrix plot:
    dvc_live.log_sklearn_plot("confusion_matrix",
                              data_y,
                              data_y_pred,
                              name = f"confusion_matrix/{ml_data_category}"
                              )
    
    # Save feature importance
    with open("params.yaml") as yaml_file:
        params = yaml.safe_load(yaml_file)
    
    feature_importance_path = params["evaluate"]["dir"]   
    
    feature_importance = ml_model.feature_importances_
    sorted_idx = np.argsort(feature_importance)
    
    plt.figure(figsize=(15, 6))
    plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center', color = "#6baed6")
    plt.yticks(range(len(sorted_idx)), np.array(data_X.columns)[sorted_idx])
    plt.rc('ytick', labelsize=6)
    plt.title('Feature Importance')
    plt.savefig(os.path.join(feature_importance_path + "/feature_importance.png"))

if __name__ == "__main__":
    
    with open("params.yaml") as yaml_file:
        params = yaml.safe_load(yaml_file)

    model_evaluation_path = params["evaluate"]["dir"]    
    model_path = params["train"]["dir"]
    data_train = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["train_file"]))
    data_test = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["test_file"]))
    
    with open(model_path + "/train_model.pkl", "rb") as model_file:
        model_clf = pickle.load(model_file)

    with Live(model_evaluation_path, dvcyaml=False) as dvc_live:
        
        dvc_live.log_param("model_params", model_clf.get_params())
        
        evaluate_model(ml_model = model_clf, 
                       data = data_train, 
                       ml_data_category = "ml_train", 
                       dvc_live = dvc_live)
        
        evaluate_model(ml_model = model_clf, 
                       data = data_test, 
                       ml_data_category = "ml_test", 
                       dvc_live = dvc_live)
                


