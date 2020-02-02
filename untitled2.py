import pandas as pd
import numpy as np

df1 = pd.read_csv('data.csv',nrows=90000)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
y = y.reshape(-1,1)



df1['char_count'] = df1['password'].str.len()
df1['numerics'] = df1['password'].apply(lambda x: len([str(x) for x in list(x) if str(x).isdigit()]))
df1['alpha'] = df1['password'].apply(lambda x: len([x for x in list(x) if x.isalpha()]))

vowels = ['a', 'e', 'i', 'o', 'u']
df1['vowels'] = df1['password'].apply(lambda x: len([x for x in list(x) if x in vowels]))
df1['consonants'] = df1['password'].apply(lambda x: len([x for x in list(x) if x not in vowels and x.isalpha()]))


 

