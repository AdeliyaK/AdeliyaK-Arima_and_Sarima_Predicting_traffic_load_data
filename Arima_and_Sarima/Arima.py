import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('dataset2.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

model = ARIMA(df['Брой автомобили'], order=(2, 1, 1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=10)

for value in forecast:
    print(f"{value:.10f}".replace('.', ','))
