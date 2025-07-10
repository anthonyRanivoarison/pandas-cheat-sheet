import pandas as pd

# 🐼 Getting started with pandas

# Reading files: .csv, .json, .excel, .sql - # .read_xxx('file_path.xxx')
df_csv = pd.read_csv('file.csv')
df_json = pd.read_json('file.json')
df_excel = pd.read_excel('file.xlsx')
...

# Show the first rows of the dataframe (default: 5)
df_csv.head()             # You can also use .head(n) to show n rows
df_json.head(10)

# Show the last rows of the dataframe
df_csv.tail()             # Like .head(n), but from the end
df_json.tail(10)

# Show total number of rows and columns
df_csv.shape              # Returns a tuple: (rows, columns)

# Columns names
df_csv.columns            # Index of column names

# Data types of each column
df_csv.dtypes

# Quick statistics on numeric columns
df_csv.describe()

# Access to data and get dataframe description
df_csv.head()            # first 5 rows
df_csv.tail()            # last 5 rows
df_csv.shape             # (rows, columns)
df_json.columns          # column names
df_json.dtypes           # data types
df_json.info()           # summary of the dataframe

# Sort rows
df_csv.sort_values(by='column_name', ascending=True)

# Add a new column
df_csv['new_column'] = df_csv['col1'] + df_csv['col2']

# Drop (remove) a column
df_csv.drop(columns=['col1'], inplace=True)

# Save the dataframe to a new file
df_csv.to_csv('new_file.csv', index=False)

# (1) Pandas Dataframe 🐼

# What is this?
# 👉 A DataFrame is like a big dictionary or table with rows (index) and columns (labels)

# Getting started

# Creating a dictionary
data = {
    'name': ['Alice', 'Bob', 'Harry'],
    'age': [12, 25, 30],
    'city': ['London', 'Boston', 'Paris']
}

# Convert this dictionary into a DataFrame
df = pd.DataFrame(data)

print(df)

# Should have

#    name  age    city
# 0  Alice   12  London
# 1    Bob   25  Boston
# 2  Harry   30   Paris

# -> See **dataframe_operations.py** for more information on making operations to this data