from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# random_state=42 : data same dila jatoy

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train ,X_test , Y_train , Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = tree.DecisionTreeClassifier()

    model.fit(X_train , Y_train)

    predictions = model.predict(X_test)

    Accuracy = accuracy_score(predictions , Y_test)

    return Accuracy

def MarvellousCalculateAccuracyKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train ,X_test , Y_train , Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = KNeighborsClassifier()

    model.fit(X_train , Y_train)

    predictions = model.predict(X_test)

    Accuracy = accuracy_score(predictions , Y_test)

    return Accuracy

def main():
    Result = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of Decision Tree Classifier is : ", Result * 100)

    Result = MarvellousCalculateAccuracyKNN()
    print("Accuracy of KNN Classifier is : ", Result * 100)

if __name__ == "__main__":
    main()