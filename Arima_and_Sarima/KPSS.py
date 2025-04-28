import statsmodels.tsa.stattools as smt
import pandas as pd

df = pd.read_csv('dataset.csv', decimal=',')

data = df['Брой автомобили']

kpss_stat, p_value, _, critical_values = smt.kpss(data, regression='ct', nlags="auto")
print(f"KPSS Statistic: {kpss_stat}")
print(f"P-Value: {p_value}")
print(f"Critical Values: {critical_values}")