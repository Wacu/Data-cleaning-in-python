import pandas as pd
import numpy as np
Students=pd.read_csv("C:/Users/Izzo/Desktop/Eunice/Python practicals/Data/Students.csv")
Students.head()
data=pd.read_csv("C:/Users/Izzo/Desktop/Eunice/Python practicals/Data/Google.csv")
data.head(15)
data.tail()
data.describe()
data.info()
data.shape()
df.iloc[0]
df.iloc[-1]
df.iloc[:0]
df.iloc[:1]
df.iloc[:-1]
df.iloc[0:5]
df.iloc[:,0:2]
df.iloc[[0,3,6,24],[0,5,6]]
