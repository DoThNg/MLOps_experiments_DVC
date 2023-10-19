## Build a Machine Learning (ML) pipeline with DVC, MLFlow and Dagster
---

### Introduction
The objective of this practice is to build a ML pipeline to predict forest cover types, using **DVC**, **MLFlow** and **Dagster**. The workflow includes:
1. **Task 1**: Preparing dataset (*csv files*) for Machine Learning (ML) training and evaluation.

  The dataset (`covertype.csv`) used in this practice contains tree observations from four areas of Roosevelt National Forest of northern Colorado. More info on dataset and variables can be found in the following:  
  https://archive.ics.uci.edu/dataset/31/covertype

  **Acknowledgement**:

  Blackard,Jock. (1998). Covertype. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N.

  The dataset can be obtained from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/31/covertype) or [kaggle](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)
  
2. **Task 2**: Training model (Decision Tree) based on datasets in Task 1.
  
3. **Task 3**: Evaluating the trained model in Task 2 based on metrics (accuracy and auc).

Tech stack:
- Python 3.10
- dvc (3.23.0)
- dagster (1.5.1)
- mlflow (2.7.1)

The above workflow will be orchestrated locally with **Dagster** - an orchestrator that's designed for developing and maintaining data assets. Further info on Dagster can be found in the following: https://dagster.io/

In addition, data versioning of datasets used in the ML pipeline will be managed by **DVC** - an open-source, Git-based data science tool that applies version control to machine learning development. Further info on DVC can be found in the following: https://dvc.org/ 

**mlflow** - an open source platform to manage the ML lifecycle will be used to track ML experiments in pipeline (More info on mlflow can be found in the following: https://mlflow.org/).

---
### Workflow Overview in this practice

  ![ml_workflow](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/docs/ml_workflow.png)

---

### Steps to run the ML data pipeline:
**Step 1:** Set up the virtual environment 
- Run command: `python -m venv {virtualenv name}`
- Place the file [data_split.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/data_split.py) in the directory where the virtual env is just created.

**Step 2:** Create a Dagster project
- Run command: `pip install dagster dagster-webserver`
- Run command: `dagster project scaffold --name ml-project` (dagster will create a project folder named: `ml-project`)
- Proceed to `ml-project/setup.py` and add python libraries used in this practice (Reference: [setup.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/setup.py))
- Proceed to directory `~/ml-project` and then `pip install -e ".[dev]"` (This will install python library dependencies)
- Place the following files in directory: `~/ml-project/ml_project`
  - Workflow: [assets.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/ml_project/assets.py)
  - Stage 1 (Prepare data): [prepare_data.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/ml_project/prepare_data.py)
  - Stage 2 (Train model): [train.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/ml_project/train.py)
  - Stage 3 (Evaluate model): [evaluate.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/ml_project/evaluate.py)
  - [params.yaml](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/ml_project/params.yaml)

**Step 3:** Initialize the DVC-enabled ML project:

**Note:**
In this practice, the project folder is set up to be a sub-folder (`2_ML_pipeline_DVC_MLflow`) in the root folder: `MLOps_experiments_DVC` - which is also a git repo. Therefore, the initialization of DVC project will be performed at root directory: `/MLOps_experiments_DVC` rather that at `/MLOps_experiments_DVC/2_ML_pipeline_DVC_MLflow`

Run the following command at root directory : `~/MLOps_experiments_DVC`

```
dvc init
```

A local storage for dataset in this practice can be also created at this step:

```
dvc remote add -d [storage name] [directory]
```

**Step 4**: Set up project sub-folders 
In directory: ~/ml-project create the following sub-folders: data, evaluation and model
```
mkdir data evaluation model
```
Go to newly created folder `data` (~/data) and create sub-folders: `prepare` and `raw_data`

```
mkdir prepare raw_data
```

The folder structure in directory: `~/ml-project` is as follows:
```bash
├───data
│   ├───prepare
│   └───raw_data
├───evaluation
├───ml_project
└───model
```

**Step 5**: Prepare raw data
- Add dataset (`covertype.csv`) to raw_data folder (~/ml-project/data/raw_data)
- Run the following command (at directory where the `data_split.py` file is located): 
```
python data_split.py
```

This will split dataset (`covertype.csv`) into train, test and validation data in `raw_data` folder 

**Step 6**: Run the ML workflow with dagster

Run command: `mflow ui` (This will launch the MLflow UI at at localhost:5000 in the browser)
Run command: `dagster dev` (This will launch the Dagster webserver/UI at localhost:3000 in the browser)

**Note**: Keep port:5000 active while running command: `dagster dev`

After running `dagster dev`, the ML pipeline can be materialized in Dagster webserver/UI.

  ![run_ml_pipeline](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/docs/dagster_workflow.png)

- The above workflow will generate datasets for ML pipeline at the step: `prepare_data`. Datasets created will be saved in folder '~/data/prepare`.
- The ML artifacts, params and metrics of this run can be found in MLFlow UI (which is still open at localhost:5000)
- Run following command in directory where the virtual env is created (in this pratice, the directory is `~/2_ML_Pipeline_DVC_MLflow/`) for data versioning of the datasets in folder `~/2_ML_Pipeline_DVC_MLflow/ml-project/data/prepare`:

```
dvc add 'ml-project\data\prepare'
git add 'ml-project\data\.gitignore' 'ml-project\data\prepare.dvc'
git commit -m "add dataset, imbalanced train data"
```

[**Optional**] The trained model can also be tagged as follows:

```
git tag -a "v1.0" -m "model v1.0 with dagster, mlflow, and imbalanced train data"
```

---

[**Optional**] The dataset used to train model in the above steps is imbalanced, illustrated as follows:  

  ![imbalanced_data](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/docs/class_distribution.png)

To address this problem, a more balanced dataset can be used to train model, and the undersampling technique will be used in this regard (This is just for practice of versioning a new dataset with DVC since the ML pipeline running with balanced dataset will later produce a model with a very low performance - undersampling reduces a significant proportion of dataset for training process).

Rerun **Step 5** above with the following argument added:
```
python data_split.py --data_balance True
```

This will create a balanced train dataset which is saved in folder `~/data/raw_data`. After generating a balanced dataset, **Step 6** can be rerun for the ML pipeline.

Once the pipeline runs successfully, run following command in directory `~/ml-project` for data versioning of the datasets newly created in folder `~/data/prepare`:

```
dvc add `ml-project\data\prepare`
git add 'ml-project\data\prepare.dvc'
git commit -m "Add prepared data with balanced train data"
```

If the model trained with imbalanced dataset is tagged as v1.0, this newly-created model with balanced dataset can be tagged as v2.0

```
git tag -a "v2.0" -m "model v2.0 with dagster, mlflow, and balanced train data"
```

**Note**:  To switch back to datasets v1.0 (imbalanced train dataset), run the following command:

```
git checkout v1.0
dvc checkout 'ml-project\data\prepare.dvc'
```
