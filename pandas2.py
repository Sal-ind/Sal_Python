import pandas as pd
df=pd.read_csv('C://Users/dyp/Desktop/hello1.csv')
ser=pd.Series(df['name'])
print(ser)