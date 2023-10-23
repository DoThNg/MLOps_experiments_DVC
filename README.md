## MLOps and ML Pipeline Experiments
This is a repo for MLOps and ML pipeline experiments and practices using DVC and other tech stack :star: :star: :star:

The dataset (covertype.csv) used for all experiments in this repo contains tree observations from four areas of Roosevelt National Forest of northern Colorado. More info on dataset and variables can be found in the following: https://archive.ics.uci.edu/dataset/31/covertype

Acknowledgement:

Blackard,Jock. (1998). Covertype. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N.

The dataset can be obtained from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/31/covertype) or [kaggle](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)

1. [ML pipeline with DVC](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/1_ML_Pipeline_DVC): This is an experiment of building a simple and reproducible ML pipeline, using DVC at a local machine. 
2. [ML pipeline with DVC, MLFlow and Dagster](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/2_ML_Pipeline_DVC_MLflow): An experiment of developing a ML pipeline, enabled by data versioning (DVC), ML experiment tracking (MLFlow) and workflow orchestration (Dagster)
3. [ML Pipeline with DVC, PyCaret, MLflow and Dagster](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/3_ML_Pipeline_DVC_PyCaret): An extended version of experiment #2 with additional element of auto-ML (Pycaret) in training and evaluation.

