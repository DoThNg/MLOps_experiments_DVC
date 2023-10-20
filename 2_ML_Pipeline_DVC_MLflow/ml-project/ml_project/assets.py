from ml_project.train import train_model
from ml_project.evaluate import evaluate_model
from ml_project.prepare_data import move_split_data
import yaml
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import pickle

from dagster import asset, Definitions
from dagster.utils import file_relative_path
import mlflow
import mlflow.data
from mlflow.data.pandas_dataset import PandasDataset

@asset
def prepare_data():
    return move_split_data()

@asset
def train_ml_model(prepare_data):
    return train_model()

@asset
def evaluate_ml_model(train_ml_model):

    train_model_acc, train_model_auc, _ = evaluate_model(ml_data_category = "train_file")
    test_model_acc, test_model_auc, test_cm = evaluate_model(ml_data_category = "test_file")

    with open(file_relative_path(__file__, "./params.yaml")) as yaml_file:
        params = yaml.safe_load(yaml_file)  
    
    model_path = params["train"]["dir"]

    with open(model_path + "/train_model.pkl", "rb") as model_file:
        model_clf = pickle.load(model_file)
                    
    # Save feature importance
    train_data = pd.read_csv(os.path.join(params["prepare"]["dir"], params["prepare"]["train_file"]))
    model_evaluation_path = params["evaluate"]["dir"]  
  
    feature_importance = model_clf.feature_importances_
    sorted_idx = np.argsort(feature_importance)
    
    fig_feature, axs = plt.subplots(1, figsize = (15, 6))
    fig_feature.suptitle('Feature Importance')

    axs.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center', color = "#6baed6")
    axs.set_yticks(range(len(sorted_idx)), np.array(train_data.columns)[sorted_idx])
    axs.set_yticklabels(labels = np.array(train_data.columns)[sorted_idx], fontsize = 6)

    fig_feature.savefig(os.path.join(model_evaluation_path + "/feature_importance.png"))

    # Set up dataset dir
    base_dir = os.getcwd()

    TRAIN_DATA_FOLDER = "data/prepare/data_train.csv"
    TEST_DATA_FOLDER = "data/prepare/data_test.csv"
    VAL_DATA_FOLDER = "data/prepare/data_val.csv"
    
    train_src = os.path.join(base_dir, TRAIN_DATA_FOLDER)
    test_src = os.path.join(base_dir, TEST_DATA_FOLDER)
    val_src = os.path.join(base_dir, VAL_DATA_FOLDER)

    with mlflow.start_run():
        
        mlflow.set_tracking_uri("http://localhost:5000")

        # Log dataset: train, test, validation
        train_df = pd.read_csv(train_src)
        train_data: PandasDataset = mlflow.data.from_pandas(train_df, source=train_src)
        mlflow.log_input(train_data, context="train")

        test_df = pd.read_csv(test_src)
        test_data: PandasDataset = mlflow.data.from_pandas(test_df, source=test_src)        
        mlflow.log_input(test_data, context="test")
        
        val_df = pd.read_csv(val_src)
        val_data: PandasDataset = mlflow.data.from_pandas(val_df, source=val_src)        
        mlflow.log_input(val_data, context="validation")

        # Log params
        mlflow.log_params(model_clf.get_params())

        # Log metrics
        mlflow.log_metric("train_model_acc", train_model_acc)
        mlflow.log_metric("train_model_auc", train_model_auc)
        mlflow.log_metric("test_model_acc", test_model_acc)
        mlflow.log_metric("test_model_auc", test_model_auc)
        
        # Log figures
        mlflow.log_figure(fig_feature, "fig_feature.png")
        mlflow.log_figure(test_cm.figure_, "test_confusion_matrix.png")

defs = Definitions(
    assets=[prepare_data, train_ml_model, evaluate_ml_model]
)
