import pandas as pd
"""
A partir da analise, foi observado que na útima linha do dataframe "data" não tinha informações válidas
então a útima linha do dataframe foi removida.
"""
data = pd.read_csv("salaries_by_college_major.csv")
# print(data.describe())
#print(data.info())
# print(data.head())
# print(data.tail())
data_clean = data.drop(50)
# print(data_clean.tail())
#Undergraduate Major, Starting Median Salary, Mid-Career 10th Percentile Salary
# TOP 5 MELHORES E PIORES CARREIRAS INICIAIS
# high = data_clean[['Undergraduate Major', 'Starting Median Salary']]
# high_initial = high.sort_values(by='Starting Median Salary', ascending=False).iloc[:5].reset_index(drop=True)
# print(high_initial)
# low = data_clean[['Undergraduate Major', 'Starting Median Salary']]
# low_initial = low.sort_values(by='Starting Median Salary', ascending=True).iloc[:5].reset_index(drop=True)
# print(low_initial)
# TOP 5 MELHORES E PIORES CARREIRAS MÉDIAS
mid = data_clean[['Undergraduate Major', 'Mid-Career 10th Percentile Salary']]
mid_high = mid.sort_values(by='Mid-Career 10th Percentile Salary', ascending=False).iloc[:5].reset_index(drop=True)
print(mid_high)
mid = data_clean[['Undergraduate Major', 'Mid-Career 10th Percentile Salary']]
mid_low = mid.sort_values(by='Mid-Career 10th Percentile Salary', ascending=True).iloc[:5].reset_index(drop=True)
print(mid_low)