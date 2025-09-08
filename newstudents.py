import pandas as pd
df = pd.read_json('newstudent.json')
print(df)
# students with math marks greater than 75
print(df[["math"] > 75])
# print data with true and false values
print(df["math"] > 75)

# print names and english marks of students 
print(df[["name", "english"]])