# Getting started with matplotlib combined with pandas - The goal is to analyze our data while visualizing them

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [23, 45, 12, 36, 27, 19, 50, 34, 42, 29],
    'Sex': ['M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F'],
    'Income': [3000, 4000, 1200, 3500, 2800, 2200, 4500, 3300, 4100, 2900]
}
df = pd.DataFrame(data)

# To create your graph, you need to continue the attribute using .plot()
    # First paramater of .plot(): kind - to specify what the type of your graph is - can be [bar, hist, scatter, pie, ...]

# Bar chart
df['Sex'].value_counts().plot(kind='bar', title="Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


# Histogram chart
df['Age'].plot(kind='hist', bins=5, title="Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()