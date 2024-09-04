import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# Adding an element to the array
arr = np.append(arr, 6)
print("Array after adding an element:", arr)

# Removing an element from the array
arr = np.delete(arr, 2)  # Removes the element at index 2
print("Array after removing an element:", arr)

# Reshaping the array
arr = np.reshape(arr, (2, 3))
print("Reshaped array:\n", arr)

# Accessing elements
print("Element at index (1, 2):", arr[1, 2])

# Slicing the array
print("Sliced array (first row):", arr[0, :])
