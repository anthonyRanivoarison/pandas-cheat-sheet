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
    # First parameter of .plot(): kind - to specify what the type of your graph is - can be [bar, hist, scatter, pie, ...]
    # Second: you can also specify x= and y= for which columns to use in the plot

# Customizing your plots

    # xlabel: specify the label for the X-axis
    # ylabel: specify the label for the Y-axis
    # show: display the figure
    # title: specify the title of the figure
    # legend: add a legend
    # savefig: save the figure to a file

# Bar chart: categorical distribution
df['Sex'].value_counts().plot(kind='bar', title="Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Histogram chart: distribution of a numerical variable
df['Age'].plot(kind='hist', bins=5, title="Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Boxplot: detect outliers & summary stats
df.boxplot(column='Income')
plt.title("Income Boxplot")
plt.ylabel("Income")
plt.show()

# Scatter plot: relationship between two variables
df.plot(kind='scatter', x='Age', y='Income', title="Age vs Income")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

# Grouped bar chart: mean income by gender
avg_income = df.groupby('Sex')['Income'].mean()
avg_income.plot(kind='bar', color=['blue', 'pink'], title="Average Income by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Income")
plt.show()

# Multiple plots in a single figure: subplots can display more than one plot
fig, axs = plt.subplots(1, 2, figsize=(10,4))

# Save a figure to file
plt.figure()
df['Age'].plot(kind='hist', bins=5)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.close()
