## Build a Machine Learning (ML) pipeline with DVC, MLFlow, Pycaret and Dagster
---

### Introduction
This is a follow-up practice for this [experiment](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/2_ML_Pipeline_DVC_MLflow). The objective is to build a Machine Learning (ML) pipeline to predict forest cover types, using the following:
- **DVC**: an open-source, Git-based data science tool that applies version control to machine learning development. Further info on DVC can be found in the following: https://dvc.org/. DVC will be used for data versioning in this experiment.
- **MLFlow**: an open source platform to manage the ML lifecycle will be used to track ML experiments in pipeline (More info on mlflow can be found in the following: https://mlflow.org/). MLFLow will be used for ML experiment tracking in this practice.
- **Pycare**: an open-source, low-code machine learning library for automation of machine learning workflows (More info on Pycaret can be found in the following: https://pycaret.gitbook.io/docs/). In this experiment, pycaret will be used to automate ML training and evaluation process. 
- **Dagster**: an orchestrator that's designed for developing and maintaining data assets. Further info on Dagster can be found in the following: https://dagster.io/

The workflow in this practice includes:
1. **Task 1**: Preparing dataset (*csv files*) for Machine Learning (ML) training and evaluation.

  The dataset (`covertype.csv`) used in this practice contains tree observations from four areas of Roosevelt National Forest of northern Colorado. More info on dataset and variables can be found in the following:  
  https://archive.ics.uci.edu/dataset/31/covertype

  **Acknowledgement**:

  Blackard,Jock. (1998). Covertype. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N.

  The dataset can be obtained from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/31/covertype) or [kaggle](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)
  
2. **Task 2**: Using Pycaret for a auto ML process based on datasets in Task 1.
  
3. **Task 3**: Evaluating the best trained model in Task 2 based on metrics (accuracy and auc).

Tech stack:
- Python 3.10
- dvc (3.23.0)
- pycaret (3.1.0)
- mlflow (2.7.1)
- dagster (1.5.1)

**Note**: The above workflow is similar to that in this [experiment](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/2_ML_Pipeline_DVC_MLflow). The main difference is at step 2 of workflow, where the element of **auto ML** is introduced, using Pycaret library. At this step, 2 ML models (decision tree and random forest) are set in advance, and other steps including data splitting, data preproceesing, model training and evaluation will be handled by Pycaret (All results at this step will be logged, using MLflow).   

---
### Workflow Overview in this practice

  ![ml_workflow](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/3_ML_Pipeline_DVC_PyCaret/docs/ml_workflow.png)

---

### Steps to run the ML data pipeline:

Steps are largely the same as those in this [practice](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/2_ML_Pipeline_DVC_MLflow). Only differences are specified while the rest will be referred to this [practice](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/2_ML_Pipeline_DVC_MLflow):

**Step 1:** Set up the virtual environment 
Refer to this [Step 1](https://github.com/DoThNg/MLOps_experiments_DVC/edit/main/2_ML_Pipeline_DVC_MLflow/README.md)
Additionally, at this step, run the following command: `pip install pycaret==3.1.0`

**Step 2:** Create a Dagster project
Refer to this [Step 2](https://github.com/DoThNg/MLOps_experiments_DVC/edit/main/2_ML_Pipeline_DVC_MLflow/README.md).

**Step 3:** Initialize the DVC-enabled ML project:
Refer to this [Step 3](https://github.com/DoThNg/MLOps_experiments_DVC/edit/main/2_ML_Pipeline_DVC_MLflow/README.md)

**Step 4**: Set up project sub-folders 

The folder structure in directory: `~/ml-project` is as follows:
```bash
├───data
│   ├───prepare
│   └───raw_data
├───ml_project
└───model
```

**Step 5**: Prepare raw data
- Add dataset (`covertype.csv`) to raw_data folder (~/ml-project/data/raw_data)
- Run the following command (at directory where the `data_split.py` file is located): 
```
python data_split.py
```

**Note**: This will split dataset (`covertype.csv`) into train and test datasets in `raw_data` folder. Pycaret will later split the train dataset into 2 other sub-sets and train models based on this split. The test dataset can be used to evaluate the best trained model generated from running auto ml process with pycaret.  

**Step 6**: Run the ML workflow with dagster
Refer to this [Step 6](https://github.com/DoThNg/MLOps_experiments_DVC/edit/main/2_ML_Pipeline_DVC_MLflow/README.md)

After running `dagster dev`, the ML pipeline can be materialized in Dagster webserver/UI as follows:

  ![run_ml_pipeline](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/3_ML_Pipeline_DVC_PyCaret/docs/ml_pipeline.png)

---
[**Optional**] Practice of data versioning with DVC

- Place the file [data_split.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/3_ML_Pipeline_DVC_PyCaret/data_split.py) in the directory where the virtual env is just created.
- Refer to this [Section](https://github.com/DoThNg/MLOps_experiments_DVC/edit/main/2_ML_Pipeline_DVC_MLflow/README.md)

