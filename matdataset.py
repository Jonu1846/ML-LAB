import pandas as pd
import matplotlib.pyplot as plt

# User input
n = int(input("Enter the number of students: "))

names = []
marks = []

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter Name: ")
    mark = int(input("Enter Marks: "))

    names.append(name)
    marks.append(mark)

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Display dataset
print("\nStudent Dataset")
print(df)

# Analysis
print("\nAverage Marks =", df["Marks"].mean())
print("Highest Marks =", df["Marks"].max())
print("Lowest Marks =", df["Marks"].min())
df.index=range(1,len(df)+1)
# Bar Graph
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()