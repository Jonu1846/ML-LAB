# Program to plot Histogram for the given dataset

import matplotlib.pyplot as plt

# Class intervals
class_intervals = ["10-15", "15-20", "20-25", "25-30", "30-35"]

# Frequencies
frequency = [5, 6, 9, 8, 2]

# Plot histogram (using bar graph representation of grouped data)
plt.bar(class_intervals, frequency, width=0.8)

# Title and Labels
plt.title("Histogram")
plt.xlabel("Class Interval")
plt.ylabel("Frequency")

# Display the graph
plt.show()