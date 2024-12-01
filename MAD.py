import numpy as np

# Given data
data = [25, 60, 30, 40, 30, 3, 5, 4, 6, 7]

def calculate_mad(data):
    mean = sum(data) / len(data)  # Calculate mean
    absolute_deviations = [abs(x - mean) for x in data]  # Absolute deviations
    mad = sum(absolute_deviations) / len(data)  # Mean absolute deviation
    return mad

def calculate_percentiles(data, percentile):
    sorted_data = sorted(data)  # Sort the data
    index = (len(data) - 1) * (percentile / 100)  # Calculate position
    lower = int(index)
    upper = lower + 1
    weight = index - lower
    return (1 - weight) * sorted_data[lower] + weight * sorted_data[upper]

# Calculate MAD
mad = calculate_mad(data)

# Calculate 25th and 75th Percentiles
p25 = calculate_percentiles(data, 25)
p75 = calculate_percentiles(data, 75)

print("Data:", data)
print("Mean Absolute Deviation (MAD):", mad)
print("25th Percentile:", p25)
print("75th Percentile:", p
