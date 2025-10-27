import pandas as pd

df=pd.read_csv("../../data/uppsala_tm_1722-2022.dat",sep='\s+')
print(df)
df.columns=['Year','Month','Day','T','Tcorr','Data id']
print(df.Tcorr)
