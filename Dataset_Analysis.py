import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'path_to_your_dataset.csv'  # Update with your file path
dataset = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First five rows of the dataset:")
print(dataset.head())

# Display the structure of the dataset
print("\nDataset structure:")
print(dataset.info())

# Check for missing values
print("\nMissing values in the dataset:")
print(dataset.isnull().sum())

# Display basic statistics of the dataset
print("\nBasic statistical summary:")
print(dataset.describe())

# Plotting the distribution of each numerical feature
for column in dataset.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 6))
    dataset[column].hist(bins=50)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.show()

# Correlation matrix
print("\nCorrelation matrix:")
correlation_matrix = dataset.corr()
print(correlation_matrix)

# Plotting the correlation matrix
plt.figure(figsize=(12, 8))
plt.matshow(correlation_matrix, fignum=1)
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Matrix', pad=50)
plt.show()
