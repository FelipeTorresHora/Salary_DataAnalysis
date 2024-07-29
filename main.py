import pandas as pd

data = pd.read_csv("salaries_by_college_major.csv")
print(data.describe())
print(data.info())
print(data.head())
# print(data.tail())
data_clean = data.drop(50)
print(data_clean.tail())

