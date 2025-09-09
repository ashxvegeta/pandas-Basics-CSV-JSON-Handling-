
import pandas as pd
df = pd.read_json('newstudent.json')
df["avg"] = df[["math", "english", "science"]].mean(axis=1)
print(df)

# axis=1 ensures the operation is row-wise (across columns).
# If axis=0 were used, the mean would be calculated column-wise (down the rows for each column).