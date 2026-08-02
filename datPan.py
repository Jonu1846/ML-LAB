import pandas as pd

# User input
n = int(input("Enter the number of students: "))

data = []

for i in range(n):
    print("\nEnter details of Student", i + 1)
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))

    data.append([name, age, marks])

# Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
df.index=range(1,len(df)+1)
print("\nStudent DataFrame")
print(df)