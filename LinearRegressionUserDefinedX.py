import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables : ",X)
    print("Values of Dependent variables : ",Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_MEAN is : ",mean_X)
    print("Y_MEAN is : ",mean_Y)

    n = len(X)

    numerator = 0
    denomeenator = 0

#   Y = mx + C
    for i in range(n):
        numerator = numerator + (X[i] - mean_X) * (Y[i] - mean_Y)
        denomeenator = denomeenator + (X[i] - mean_X)**2

    m = numerator / denomeenator

    print("Slope of line ie m is : ",m)

    c = mean_Y - (m * mean_X)

    print("Y intercept of line is : ",c)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()