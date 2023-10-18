from sklearn.model_selection import train_test_split
import pandas as pd
from collections import Counter
import argparse
import random
import os


def split_dataset(train_data_balance=False):

    DATADIR = "./ml-project/data/raw_data"
    FILENAME = "covtype.csv"

    test_size = 0.2
    random_state = 12
    seed = 1

    df = pd.read_csv(os.path.join(DATADIR, FILENAME))

    if train_data_balance==False:

        # Split data into training, validation and testing
        data_train_val, data_test = train_test_split(df, 
                                                    test_size=test_size,  
                                                    random_state=random_state)

        data_train, data_val = train_test_split(data_train_val,  
                                                test_size=test_size, 
                                                random_state=random_state)
        
        if not os.path.exists(DATADIR):    
            os.makedirs(DATADIR)

        # Save the train dataset
        data_train.to_csv(os.path.join(DATADIR, "data_train.csv"), index = False)

        # Save the validation dataset
        data_val.to_csv(os.path.join(DATADIR, "data_val.csv"), index = False)

        # Save the test dataset
        data_test.to_csv(os.path.join(DATADIR, "data_test.csv"), index = False)
    
    else:
        
        random.seed(seed)
        
        # set number of rows obtained randomly
        n_row = 2000

        data_list_ml_train = []
        data_list_ml_test = []

        data_class = Counter(df["Cover_Type"])

        for n_class in range(1, 8):
            seq = data_class[n_class]
            ml_train_idx = random.choices(range(1, seq), k = n_row)

            df1 = df.loc[df["Cover_Type"] == n_class].iloc[ml_train_idx]
            ml_test_idx = df.loc[df["Cover_Type"] == n_class].index.isin(ml_train_idx)
            df2 = df.loc[df["Cover_Type"] == n_class][~ml_test_idx]

            data_list_ml_train.append(df1)
            data_list_ml_test.append(df2)

        df_train = pd.concat(data_list_ml_train)
        data_test = pd.concat(data_list_ml_test)

        # Split data into training, validation and testing
        data_train, data_val = train_test_split(df_train,  
                                                test_size=test_size, 
                                                random_state=random_state)
        
        if not os.path.exists(DATADIR):    
            os.makedirs(DATADIR)

        # Save the train dataset
        data_train.to_csv(os.path.join(DATADIR, "data_train.csv"), index = False)

        # Save the validation dataset
        data_val.to_csv(os.path.join(DATADIR, "data_val.csv"), index = False)

        # Save the test dataset
        data_test.to_csv(os.path.join(DATADIR, "data_test.csv"), index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_balance", default=False)
    args = parser.parse_args()
    split_dataset(train_data_balance = args.data_balance)