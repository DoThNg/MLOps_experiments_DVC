from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import pickle
import pandas as pd
import os
import yaml
from dagster.utils import file_relative_path

def train_model():
    
    with open(file_relative_path(__file__, "./params.yaml")) as yaml_file:
        params = yaml.safe_load(yaml_file)

    random_state = params["train"]["random_state"]
    max_depth = params["train"]["max_depth"]
    max_features = params["train"]["max_features"]
    min_samples_split = params["train"]["min_samples_split"]

    model_clf = DecisionTreeClassifier(max_depth=max_depth, 
                                       max_features=max_features, 
                                       min_samples_split=min_samples_split,
                                       random_state=random_state)
    
    data_train = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["train_file"]))
    data_val = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["val_file"]))

    data_X_train, data_y_train = data_train.drop("Cover_Type", axis = 1), data_train["Cover_Type"]
    data_X_val, data_y_val = data_val.drop("Cover_Type", axis = 1), data_val["Cover_Type"]     
    
    model_clf.fit(data_X_train, data_y_train)
    data_y_pred = model_clf.predict(data_X_val)
    data_y_prob_pred = model_clf.predict_proba(data_X_val)

    print("Accuracy:", accuracy_score(data_y_val, data_y_pred))
    print("AUC: ", roc_auc_score(data_y_val, data_y_prob_pred, multi_class='ovr'))

    if not os.path.exists(params["train"]["dir"]):    
        os.makedirs(params["train"]["dir"])
    
    with open(params["train"]["dir"] + "/train_model.pkl", "wb") as model_file:
        pickle.dump(model_clf, model_file)