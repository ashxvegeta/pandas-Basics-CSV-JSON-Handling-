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
max_row = df.loc[df["total"].idxmax()]
print("Product with maximum total sales:", max_row["product"])
print("Total sales amount:", max_row["total"])
print(df.sort_values(by="total", ascending=False))