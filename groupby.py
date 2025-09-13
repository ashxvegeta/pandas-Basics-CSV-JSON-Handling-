import pandas as pd
df = pd.read_csv('groupbyemployees.csv')
# ensure salary is numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
# overall average salary
overall_avg_salary = df["salary"].mean()
print("Overall Average Salary:", round(overall_avg_salary, 2))
# Average salary per department:
group_avg =  df.groupby("department")["salary"].mean().round(2)
print("Average Salary per Department:")
print(group_avg)

# maximum salary per department
group_max =  df.groupby("department")["salary"].max().round(2)
print("Maximum Salary per Department:")
print(group_max)

print ("Departments sorted by average salary")
print(df.sort_values(by=["department", "salary"], ascending=[True, False]))