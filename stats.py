import statistics

n = int(input("Enter the number of elements in the dataset: "))

data = []

print("Enter the elements one by one:")
for i in range(n):
    value = float(input(f"Element {i+1}: "))
    data.append(value)

mean = statistics.mean(data)
median = statistics.median(data)

try:
    mode = statistics.mode(data)
except:
    mode = "No unique mode found"

variance = statistics.variance(data)
std_deviation = statistics.stdev(data)

print("\n----- Statistical Measures -----")
print("Dataset :", data)
print("Mean :", mean)
print("Median :", median)
print("Mode :", mode)
print("Variance :", variance)
print("Standard Deviation :", std_deviation)