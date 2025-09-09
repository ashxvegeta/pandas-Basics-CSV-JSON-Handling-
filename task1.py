# 📌 Your Task:
# Create a CSV file sales.csv with this data:

# product,price,quantity
# Laptop,50000,3
# Phone,20000,5
# Tablet,15000,2


# Then write Python code to:

# Load it with pandas

# Add a new column total = price * quantity

# Print the product with the highest total


import pandas as pd
df = pd.read_csv('sales.csv')
df["total"] = df["price"] * df["quantity"]
# print(df["total"].max())



# add total column
df["total"] = df["price"] * df["quantity"]

#find the row with maximum total sales

# df["total"]:

# This accesses the total column of the DataFrame df.
# df["total"].idxmax():

# The idxmax() function returns the index of the row where the total column has its maximum value.
# For example, if the maximum value in the total column is in row 5, idxmax() will return 5.
# df.loc[...]:

# The .loc[] function is used to access rows or columns in the DataFrame by label (index).
# Here, it retrieves the row corresponding to the index returned by idxmax().
# max_row:

# The variable max_row now holds the entire row (as a Series) where the total column has the highest value.

max_row = df.loc[df["total"].idxmax()]
print("Product with maximum total sales:", max_row["product"])
print("Total sales amount:", max_row["total"])
print(df.sort_values(by="total", ascending=False))