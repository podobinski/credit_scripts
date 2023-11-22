import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the CSV file in the current working directory
df = pd.read_csv('input.csv')

# Extracting the columns
months_of_credit = df.iloc[:, 0]  # First column
interest_rate = df.iloc[:, 1]     # Second column
RSSO = df.iloc[:, 2]              # Third column

# Creating a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
scatter = ax.scatter(months_of_credit, interest_rate, RSSO, c=RSSO, cmap='viridis')

# Adding labels
ax.set_xlabel('Months of Credit')
ax.set_ylabel('Interest Rate')
ax.set_zlabel('RSSO')

# Adding a color bar
color_bar = fig.colorbar(scatter)
color_bar.set_label('RSSO')

# Showing the plot
plt.show()
