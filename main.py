import pandas as pd
df = pd.read_json('student.json')
print(df)
print(df.columns)
print(df['name'])
print(df[['name', 'marks']])
print(df.head())
print(df.describe())