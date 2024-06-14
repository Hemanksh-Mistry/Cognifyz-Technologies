# Task 2
# Task: Create a Data Visualization Tool
# Build a tool that takes a dataset and generates interactive visualizations using libraries such as Matplotlib, Seaborn, or Plotly. This task will enhance their understanding of data visualization principles and plotting techniques.

# Importing the required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

# Loading the Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_data['species'] = iris.target

# Plotting the data
sns.pairplot(iris_data, hue='species')
plt.show()

# Saving the plot as an image
plt.savefig('iris_pairplot.png')