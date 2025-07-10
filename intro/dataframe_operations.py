import pandas as pd

# Reading file

df = pd.read_csv('data/peoples.csv')

# Selecting data

df['name']             # one column (as Series)
df[['name', 'age']]    # several columns (as DataFrame)

df.iloc[0]             # first row (by index, as Series)
df.loc[0]              # same, by label (if index has labels)

df.iloc[0:2]           # first two rows

# Filtering rows

df[df['age'] > 20]               # rows where age > 20
df[df['city'] == 'Paris']        # rows where city is Paris

# Sorting: asc - desc

df.sort_values(by='age')                     # ascending
df.sort_values(by='age', ascending=False)    # descending

# Adding or modifying columns

df['country'] = 'USA'                # add constant value
df['age_more_10'] = df['age'] + 10   # compute a new column

# Removing column

df.drop(columns=['age_more_10'], inplace=True) # inplace=True means that you want to delete this in this dataframe

# Reset - Set Index

df.set_index('name', inplace=True)    # set 'name' as index
df.reset_index(inplace=True)                # reset to default integers

# Save and load

df.to_csv('my_data.csv', index=False)       # save
df2 = pd.read_csv('my_data.csv')                       # load again


