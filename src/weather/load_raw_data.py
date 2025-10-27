"""
Function to load raw data
"""

column_names=['Date','Time','Temp']
df = pd.read_csv('data/smhi_opendata_1_97530_20250224_081022.csv', header=None, delimiter=";", names=column_names,skiprows = 10, usecols=[0, 1, 2])
print(df)
print(df.Date)
print(df.Time)
print(df.Temp)
