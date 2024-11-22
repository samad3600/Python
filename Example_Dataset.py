import pandas as pd

# Load dataset
file_path = 'path_to_your_dataset.csv'  # Update with your file path
dataset = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(dataset.head())

# Check for any missing values
print(dataset.isnull().sum())

# Display basic statistics of the dataset
print(dataset.describe())
