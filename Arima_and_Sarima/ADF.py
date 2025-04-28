import statsmodels.tsa.stattools as smt
import pandas as pd

df = pd.read_csv('dataset.csv',decimal=',')

data = df["Брой автомобили"]

result = smt.adfuller(data)
print("\nADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:", result[4])
