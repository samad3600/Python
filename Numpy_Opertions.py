# Numpy Operations Program

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Perform element-wise addition
result_add = array_1d + 10

# Perform element-wise multiplication
result_multiply = array_2d * 2

# Calculate the mean of the 1D array
mean_1d = np.mean(array_1d)

# Calculate the sum of the 2D array
sum_2d = np.sum(array_2d)

# Transpose the 2D array
transpose_2d = np.transpose(array_2d)

# Print results
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print("Result of Addition:", result_add)
print("Result of Multiplication:\n", result_multiply)
print("Mean of 1D Array:", mean_1d)
print("Sum of 2D Array:", sum_2d)
print("Transposed 2D Array:\n", transpose_2d)
