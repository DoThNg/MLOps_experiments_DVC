## Build a Machine Learning (ML) pipeline with DVC
---

### Introduction
The objective of this practice is to get a reproducible and simple ML pipeline up and running quickly using **DVC**. The workflow includes:
1. **Task 1**: Preparing data (data split into train, validation and test datasets). The dataset (`covertype.csv`) used in this practice contains tree observations from four areas of Roosevelt National Forest of northern Colorado. More info on dataset and variables can be found in the following: https://archive.ics.uci.edu/dataset/31/covertype

  **Acknowledgement**:

  Blackard,Jock. (1998). Covertype. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N.

  The dataset can be obtained from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/31/covertype) or [kaggle](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)

2. **Task 2**: Based on attributes of dataset such as elevation, aspect, slope, hillshade, soil-type, etc, a model will be trained to predict 7 forest cover types.
3. **Task 3**: The trained model will be then evaluated with different metrics (i.e. accuracy and auc).

Each task above is performed by a corresponding python script file, as provided in the following [~/MLOps_experiments_DVC/1_ML_Pipeline_DVC/src](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/1_ML_Pipeline_DVC/src). This workflow will be reproducible using **DVC** - an open-source, Git-based data science tool that applies version control to machine learning development. Further info on DVC can be found in the following: https://dvc.org/

Tech stack:
- Python 3.10
- dvc (3.23.0)
- dvclive (3.0.1)

---
### Workflow in this practice is illustrated by the following:

  ![dvc_workflow](https://github.com/DoThNg/MLOps_experiments_DVC/blob/main/1_ML_Pipeline_DVC/docs/dvc_workflow.png)
---

### Steps to run the ML pipeline with dvc:
**Step 1:** Set up the virtual environment and install project requirements:

Proceed with project folder and Run the following commands:
- To create virtual env: `python -m venv {virtualenv name}`
- To install python libraries used in project: `pip install -r src/requirements.txt` (Reference: [requirements.txt](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/1_ML_Pipeline_DVC/src/requirements.txt))

**Step 2:** Initialize the DVC-enabled ML project:

**Note:**
- In this practice, the project folder is set up to be a sub-folder (`1_ML_pipeline_DVC`) in the root folder: `MLOps_experiments_DVC` - which is also a git repo. Therefore, the initialization of DVC project will be performed at root directory: `/MLOps_experiments_DVC` rather that at `/MLOps_experiments_DVC/1_ML_Pipeline_DVC`

Run the following command at root directory : `~/MLOps_Experiments`

```
dvc init
```

Check the git status and commit

```
git status
git commit -m "Initialize DVC"
```

Further info on initializing a project with DVC can be found in the following: https://dvc.org/doc/start

- Under directory `/MLOps_experiments_DVC/1_ML_pipeline_DVC`, create two sub-folders: `model` (This sub-folder contains trained model (.pkl)) and 'evaluation` (This sub-folder contains plots, model metrics and parameters after each run) 

**Step 3:** Data Versioning:
- Go to directory: ~/MLOps_experiments_DVC/1_ML_Pipeline_DVC: `cd 1_ML_Pipeline_DVC`
- In the newly-created folder - 1_ML_Pipeline_DVC, create a folder named `data` and store the dataset (`covtype.csv`) used in this practice into this folder.
- Run the following commands to start tracking the dataset:

```
dvc add data/covtype.csv
git add 'data\.gitignore' 'data\covtype.csv.dvc'
git commit -m "Add raw data"
```

- In the folder `data`, create another sub-folder named `prepare`. This folder will later contain train, validation and test datasets. 

**[Optional]** Save the following python file - [create_dataset.py](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/1_ML_Pipeline_DVC/src/create_dataset.py) in the directory `~/MLOps_experiments_DVC/1_ML_Pipeline_DVC`. This file can be later used to run the data split process to obtain a well-balanced train, validation and test datasets.


- A remote storage can be configured at this step. In the scope of this practice, the implementation is performed locally only, therefore the remote storage is also set up to be a local storage.

```
dvc remote add --local [local storage directory]
```

To upload or download data to and from this local storage, run the following command:

To upload tracked files or directories from the cache to this storage:
```
dvc push
```

To download tracked files or directories from this storage:
```
dvc pull
```

**Note:**
replace the `[local storage directory]` with a directory in the local machine.

**Step 4**: Set up YAML file containing parameters used in the ML pipeline.
- Add `params.yaml` in the following directory `~/MLOps_experiments_DVC/1_ML_Pipeline_DVC` (Reference: [params.yaml](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/1_ML_Pipeline_DVC/params.yaml))

**Step 5:** Add stages in the ML pipeline:

The stages in ML pipeline will be defined by YAML format files (i.e. `.dvc` and `dvc.yaml`). The stages can be created using `dvc stage add` command. Further info can be found in the following: https://dvc.org/doc/start/data-management/data-pipelines. Another way to add stages in the ML pipeline is add these stages directly to a `dvc.yaml` file - which is placed in the following directory `~/MLOps_experiments_DVC/1_ML_Pipeline_DVC`. (Reference: [dvc.yaml](https://github.com/DoThNg/MLOps_experiments_DVC/tree/main/1_ML_Pipeline_DVC/dvc.yaml))

**Step 6:** Run the ML pipeline:

After stages added, run the following command to run the entire ML pipeline:

```
dvc repro
```
**Note**: Running `dvc repro` where the dvc.yaml file is located.


