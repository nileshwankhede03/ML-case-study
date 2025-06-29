from sklearn.datasets import load_iris
import pandas as pd
'''
Documentation : 
df["variety"] : used to access column name 
    1 . load to the csv file
    2. clean the data if rows have missing values, a.delete the row or add avg in a missing values.
    2. pre-processing / encoding for ML algorithms. (so use map() function)
        this method helps to transform data or used to substitute the values,
        or in simple words can values replace using {key : value}
    3. seperate Independent & depedent variables
    use drop() : The drop() function in Pandas is used to remove specified rows or columns from a DataFrame or Series. check parameters using VScode intelligent.

    4. shape : property is used to get row , colmn values. ex. (150, 4).  150 : rows  4. colmns
'''
def main():
    df = pd.read_csv("iris.csv")
    print("Dimension of dataset is : ",df.shape)
    print("Dataset loaded sucessfully")

    # print(df["variety"])
    # print(df["sepal.length"].head())

    print(df["variety"])

    df["variety"] = df["variety"].map({"Setosa" : 0, "Versicolor" : 1, "Virginica" : 2 }) # encode/pre-processing needs value in integer.
    print(df["variety"])

    x = df.drop("variety",axis = "columns")  # 1 : column , 0 : row The drop() function in Pandas is used to remove specified rows or columns from a DataFrame or Series. 
    y = df["variety"]

    print("Independent variable dimension : ",x.shape)
    print("Dependent variable dimension : ",y.shape)

if __name__ == "__main__":
    main()