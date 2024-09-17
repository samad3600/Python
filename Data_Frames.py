# Data Frame Operations Program

import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column
df['Salary'] = [70000, 80000, 60000, 90000]

# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]

# Group by City and calculate the average Salary
grouped_df = df.groupby('City')['Salary'].mean().reset_index()

# Display results
print("\nDataFrame after adding Salary column:")
print(df)

print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

print("\nGrouped DataFrame (Average Salary by City):")
print(grouped_df)
