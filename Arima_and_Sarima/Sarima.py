import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

df = pd.read_csv('dataset2.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

model = SARIMAX(df['Брой автомобили'],
                order = (1, 0, 1),
                seasonal_order =(0, 1, 2, 4))

results = model.fit()
forecast = results.forecast(steps=10)
for value in forecast:
    print(f"{value:.10f}".replace('.', ','))