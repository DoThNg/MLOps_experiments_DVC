import pandas as pd
from collections import Counter
import random

def create_dataset():
    
    random.seed(10)
    
    # set number of rows obtained randomly
    n_row = 2000

    data_list_ml_train = []
    data_list_ml_test = []

    df = pd.read_csv("./data/covtype.csv")

    data_class = Counter(df["Cover_Type"])

    for dc in range(1, 8):
        seq = data_class[dc]
        ml_train_idx = random.choices(range(1, seq), k = n_row)

        df1 = df.loc[df["Cover_Type"] == dc].iloc[ml_train_idx]
        ml_test_idx = df.loc[df["Cover_Type"] == dc].index.isin(ml_train_idx)
        df2 = df.loc[df["Cover_Type"] == dc][~ml_test_idx]

        data_list_ml_train.append(df1)
        data_list_ml_test.append(df2)

    df_train = pd.concat(data_list_ml_train)
    df_test = pd.concat(data_list_ml_test)

    # Save the data as csv files
    df_train.to_csv("./data/covtype_train.csv")
    df_test.to_csv("./data/covtype_test.csv")

if __name__ == "__main__":
    create_dataset()