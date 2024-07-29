import pandas as pd
"""
A partir da analise, foi observado que na útima linha do dataframe "data" não tinha informações válidas
então a útima linha do dataframe foi removida.
"""
data = pd.read_csv("salaries_by_college_major.csv")
pd.options.display.float_format = '{:,.2f}'.format 
# print(data.describe())
# print(data.info())
# print(data.head())
# print(data.tail())
data_clean = data.drop(50)
# print(data_clean.tail())

# """
# A partir da analisado os melhores e piores salários em relação a senioridade do profissional e a profissão.
# """
# #TOP 5 MELHORES E PIORES SALÁRIOS INICIAIS
# high = data_clean[['Undergraduate Major', 'Starting Median Salary']]
# high_initial = high.sort_values(by='Starting Median Salary', ascending=False).iloc[:5].reset_index(drop=True)
# print(high_initial)
# low = data_clean[['Undergraduate Major', 'Starting Median Salary']]
# low_initial = low.sort_values(by='Starting Median Salary', ascending=True).iloc[:5].reset_index(drop=True)
# print(low_initial)
# #TOP 5 MELHORES E PIORES SALÁRIOS PLENOS
# mid = data_clean[['Undergraduate Major', 'Mid-Career 10th Percentile Salary']]
# mid_high = mid.sort_values(by='Mid-Career 10th Percentile Salary', ascending=False).iloc[:5].reset_index(drop=True)
# print(mid_high)
# mid = data_clean[['Undergraduate Major', 'Mid-Career 10th Percentile Salary']]
# mid_low = mid.sort_values(by='Mid-Career 10th Percentile Salary', ascending=True).iloc[:5].reset_index(drop=True)
# print(mid_low)
# """
# Spread é a diferença salarial entre as carreiras dos profissionais mais antigos
# """
# spread_col = data_clean['Mid-Career 90th Percentile Salary'] - data_clean['Mid-Career 10th Percentile Salary']
# data_clean.insert(5, 'Spread', spread_col)
# data_clean.head()
# """
# Low-Risk é classficado como os empregos de menor spread, ou seja, menor diferença entre maior e menor salário.
# """
# low_risk_df = data_clean[['Undergraduate Major', 'Spread']]
# low_risk = low_risk_df.sort_values(by='Spread', ascending=True).iloc[:5].reset_index(drop=True)
# print(low_risk)

print(data_clean.groupby("Group").mean())

