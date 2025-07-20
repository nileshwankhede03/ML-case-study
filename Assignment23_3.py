# Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.
# data = {
# 'Name': ['Amit', 'Sagar', 'Pooja'],
# 'Math': [85, 90, 78],
# 'Science': [92, 88, 80],
# 'English': [75, 85, 82]
# Note: Consider the same dataset for this as well as next assignment.
#output:
#     Name  Math  Science  English  Total
# 0   Amit    85       92       75    252
# 1  Sagar    90       88       85    263
# 2  Pooja    78       80       82    240

import pandas as pd
import numpy as np

data = {
    'Name' : ['Amit' , 'Sagar' , 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)
print(df)

print("New Column added! ")
df.insert(4, 'Total', df['Math'] + df['Science'] + df['English'])
print(df)