import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.random.rand(100, 1)  # Input feature (e.g., experience)
y = 2 * X + 1 + np.random.randn(100, 1)  # Target (e.g., salary)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get model coefficients
slope = model.coef_[0][0]
intercept = model.intercept_[0]

# Plot the regression line
plt.scatter(X, y, label="Data points")
plt.plot(X, slope * X + intercept, color='red', label="Regression line")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Example")
plt.legend()
plt.show()

# Make predictions
new_experience = np.array([[0.8]])
predicted_salary = model.predict(new_experience)
print(f"Predicted salary for experience 0.8: {predicted_salary[0][0]}")
