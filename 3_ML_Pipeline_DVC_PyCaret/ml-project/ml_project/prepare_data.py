import shutil
import os

def move_split_data():
    
    TRAIN_DATA_SRC_FOLDER = "data/raw_data/data_train.csv"
    TRAIN_DATA_DST_FOLDER = "data/prepare/data_train.csv"

    TEST_DATA_SRC_FOLDER = "data/raw_data/data_test.csv"
    TEST_DATA_DST_FOLDER = "data/prepare/data_test.csv"

    base_dir = os.getcwd()
        
    train_src = os.path.join(base_dir, TRAIN_DATA_SRC_FOLDER)
    train_dst = os.path.join(base_dir, TRAIN_DATA_DST_FOLDER)
    shutil.copy(train_src, train_dst)

    test_src = os.path.join(base_dir, TEST_DATA_SRC_FOLDER)
    test_dst = os.path.join(base_dir, TEST_DATA_DST_FOLDER)
    shutil.copy(test_src, test_dst)