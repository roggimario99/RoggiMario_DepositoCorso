import pandas as pd
import numpy as np

# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=100, freq='M')

# Creiamo il DataFrame
df = pd.DataFrame({'date': date_range})

# Impostiamo la colonna 'date' come indice
df = df.set_index('date')
df["value"] = np.linspace(1,10,100)
print(df.head())

# Resampling mensile (M): calcoliamo per esempio la "media"
df_resampled = df.resample('Y').mean()

print(df_resampled.head())