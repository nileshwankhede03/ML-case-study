import pandas as pd
from sklearn.model_selection import train_test_split

def LoadData(filepath):
    df = pd.read_csv(filepath)
    print("Dataset gets in memory successfully")
    return df 

def GetInformation(df):
    print("Information about loded dataset is : ")
    print("Shape of dataset : ",df.shape)
    print("Columns : ",df.columns)
    print("Missing values : ",df.isnull().sum())

def EncodeData(df):
    df["variety"] = df["variety"].map({"Setosa" : 0, "Versicolor" : 1, "Virginica": 2})
    return df

def split_feature_target(df):
    X = df.drop('variety',axis = 1)
    Y = df["variety"]
    return X , Y

def split(X, Y , size = 0.2):
    return train_test_split(X,Y,test_size = size)

def train():
    pass


def main():
    data = LoadData("iris.csv")
    print(data.head())

    GetInformation(data)

    print("Data after encoded")
    data = EncodeData(data)
    print(data.head())

    print("Splitting features and labels : ")
    Independent , Dependent = split_feature_target(data)
    print(Independent.head())
    print(Dependent.head())

    X_train , X_test , Y_train , Y_test = split(Independent,Dependent,0.3)

    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)


if __name__ == "__main__":
    main()