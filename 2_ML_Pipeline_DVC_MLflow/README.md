## Build a Machine Learning (ML) pipeline with DVC, MLFlow and Dagster
---

### Introduction
The objective of this practice is to build a ML pipeline using **DVC**, **MLFlow** and **Dagster**. The workflow includes:
1. **Task 1**: Preparing dataset (csv files*) for Machine Learning (ML) training and evaluation.

  The dataset (`covertype.csv`) used in this practice contains tree observations from four areas of Roosevelt National Forest of northern Colorado. More info on dataset and variables can be found in the following:  
  https://archive.ics.uci.edu/dataset/31/covertype

  **Acknowledgement**:

  Blackard,Jock. (1998). Covertype. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N.

  The dataset can be obtained from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/31/covertype) or [kaggle](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)
2. **Task 2**: Training model (Decision Tree) based on datasets in Task 1.
3. **Task 3**: Evaluating the trained model in Task 2 based on metrics (accuracy and auc).

The above workflow will be orchestrated locally with **Dagster** - an orchestrator that's designed for developing and maintaining data assets. Further info on Dagster can be found in the following: https://dagster.io/

In addition, data versioning of ML pipeline will be managed by **DVC** - an open-source, Git-based data science tool that applies version control to machine learning development. Further info on DVC can be found in the following: https://dvc.org/ while mlflow - an open source platform to manage the ML lifecycle will be used to track ML experiments in pipeline (More info on mlflow can be found in the following: https://mlflow.org/).

Tech stack:
- Python 3.10
- dvc (3.23.0)
- dagster (1.5.1)
- mlflow (2.7.1)

---
### Workflow Overview in this practice

  ![ml_workflow](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/2_ML_Pipeline_DVC_MLflow/docs/ml_workflow.png)

---
