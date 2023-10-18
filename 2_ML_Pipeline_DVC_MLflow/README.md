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

**Step 2:** Create a Dagster project
- Run command: `pip install dagster dagster-webserver`
- Run command: `dagster project scaffold --name ml-project` (dagster will create a project folder named: `ml-project`)
- Go to `ml-project/setup.py` and add python libraries used in this practice (Reference: [setup.py](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/ml-project/setup.py)
- Go to directort `~/ml-project` and then `pip install -e ".[dev]"` (This will install python library dependencies)

**Step 3:** Initialize the DVC-enabled ML project:

**Note:**
- In this practice, the project folder is set up to be a sub-folder (`2_ML_pipeline_DVC_MLflow`) in the root folder: `MLOps_experiments_DVC` - which is also a git repo. Therefore, the initialization of DVC project will be performed at root directory: `/MLOps_experiments_DVC` rather that at `/MLOps_experiments_DVC/2_ML_pipeline_DVC_MLflow`

Run the following command at root directory : `~/MLOps_experiments_DVC`

```
dvc init
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

The folder structure in directory: ~/ml-project as follows:
```bash
C:.
├───data
│   ├───prepare
│   └───raw_data
├───evaluation
├───ml_project
└───model
```

**Step 5**: Add dataset (`covertype.csv`) to raw_data folder (~/ml-project/data/raw_data)


