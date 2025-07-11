# Data cleaning with Pandas

import pandas as pd

df = pd.read_csv('../data/peoples.csv')

## Checking your data
df.info()
df.describe()
df.isnull().sum()
df.head()

## Removing or filling missing data

### Remove rows with at least one missing value
df.dropna()

### Remove columns with missing values - [axis=1 - column] - [axis=0 - row]
df.dropna(axis=1)

### Replace Nan into 0, or other values
df.fillna(0)

### Replace Nan into mean or median of the column
df['col'].fillna(df['col'].mean())
df['col'].fillna(df['col'].median())

### Replace Nan using previous or intermediate method
df.fillna(method='ffill') # forward fill
df.fillna(method='bfill') # backward fill

## Removing duplicates
df.drop_duplicates()  # drop duplicates rows
df.drop_duplicates(subset=['col1', 'col2'], keep='first') # drop with some columns

## Renaming and cleaning columns

### Rename a column
df.rename(columns={'old_name': 'new_name'}, inplace=True)

### Rename all columns
df.columns = ['col1', 'col2', 'col3']

### Cleaning columns' names (drop spaces...)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

### Changing data types
df['col'] = df['col'].astype(int)      # convert to int
df['col'] = pd.to_datetime(df['col']) # convert to datetime
df['col'] = df['col'].astype(str)     # convert to string

