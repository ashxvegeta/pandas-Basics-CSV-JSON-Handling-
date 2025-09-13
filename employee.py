import pandas as pd
df = pd.read_csv('employees.csv')
missing_data_rows = df[df.isnull().any(axis=1)]
# print missing_data_rows
print(missing_data_rows)
# Fill missing salary values with 0
df["salary"] =  df["salary"].fillna(0)
print(df)

# Drop duplicate rows
df = df.drop_duplicates()
print("DataFrame after dropping duplicate rows:")
print(df)

# # Fill missing age with a default value (e.g., 0)
df["age"] = df["age"].fillna(0)
print(df)