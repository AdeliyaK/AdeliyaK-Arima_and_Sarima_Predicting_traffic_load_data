import statsmodels.tsa.stattools as smt
import pandas as pd

df = pd.read_csv('dataset.csv',decimal=',')

data = df["Брой автомобили"]

result = smt.adfuller(data)
print("\nADF статистика преди първото диференциране:", result[0])
print("p-стойност преди първото диференциране:", result[1])
print("Критични стойности преди първото диференциране:", result[4])