# Introducing Data Transformation

import pandas as pd
import numpy as np

df = pd.read_csv('../data/peoples.csv')

## Applying functions (.apply, .map, .transform, .replace, ...)
df['col'].apply(lambda x: x**2)      # For each values in this column, we transform this **2
df['col'].map({'A':1, 'B':2})        # mapping dict
df[['a', 'b']].apply(np.sum, axis=1) # row-wise
df.transform(lambda x: x*10)         # returns same shape

## String and Datetime operations

### Strings
df['col'].str.upper()          # uppercase
df['col'].str.lower()          # lowercase
df['col'].str.contains('text') # check substring
df['col'].str.replace('old', 'new')
df['col'].str.len()            # string length

### Datetime
df['date'] = pd.to_datetime(df['date'])     # convert to datetime
df['date'].dt.year                          # extract year
df['date'].dt.month                         # extract month
df['date'].dt.day_name()                    # get weekday name
df['date'].dt.strftime('%Y-%m-%d')          # custom format
df.set_index('date').resample('M').mean()   # resample by month
