# Q2: Use the DataFrame from Q1 and print descriptive statistics using describe().
# data = {
# 'Name': ['Amit', 'Sagar', 'Pooja'],
# 'Math': [85, 90, 78],
# 'Science': [92, 88, 801],
# 'English': [75, 85, 82]
# Note: Consider the same dataset for this as well as next assignment.

import pandas as pd
data = {
    'Name' : ['Amit' , 'Sagar' , 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 801],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)
print(df)

# this function will display stastical data of DataFrame.
print(df.describe())