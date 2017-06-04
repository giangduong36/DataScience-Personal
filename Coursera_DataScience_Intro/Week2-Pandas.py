import pandas as pd
import numpy as np

# type
animals = ["dog", "cat", 'bird']
print(pd.Series(animals))
print(pd.Series(["string",None]))
print(pd.Series([1, 2, None]))

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
sport = pd.Series(sports)
print(sport.index)
print(pd.Series(["Corgi", "Garfield"], index=["dog", "cat"]))
print(pd.Series(["Corgi", "Garfield"], index=["dog", "cat"]))

# Query
# Get entry
print(sport.iloc[1])  # Look up based on position
print(sport.loc['Golf'])  # Look up based on label
print(sport[2], sport['Golf'])  # Implied, dangerous

# Iterate
s = pd.Series(np.random.randint(0,1000,10000))
print(s.head())
for label, value in s.iteritems():
    s.loc[label]= value+2
print(s.head())

# Add entry
s1 = pd.Series([1,2,3])
s1.loc['Animal'] = 'Dogs'

# Append two series
print(sport.append(s1))

# DataFrame Data Structure

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print(df)
print(df.loc['Store 1']['Cost'])

# Get all values in a column in 2 ways
print(df.T.loc['Item Purchased'])
print(df['Item Purchased'])

# Delete
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')  # Return a copy of data frame
del copy_df['Cost']
print(copy_df)

# Change values of a column
df['Cost'] *= df['Cost'] * 0.7
print(df)

# CSV
df = pd.read_csv('mpg.csv')
print(df.head())

# Skip rows
df = pd.read_csv('mpg.csv', index_col = 0)
# df = pd.read_csv('mpg.csv', index_col = 0, skiprows=1)
print(df.head())
print(df.columns)
for col in df.columns:
    if col == 'cty':
        df.rename(columns={col:'city'}, inplace = True)

print(df.head())

# Query

latest = df.where(df['year'] > 2000)
latest = df[df['year'] > 2000]
print(latest.head())
print(latest.dropna().head())
print(latest['manufacturer'].count())
print(set(df['manufacturer'][df['year']<2000]))

# Indexing
df = df.set_index('year')
df = df.reset_index()
print(df['year'].unique())
df = df.set_index('manufacturer', 'trans')
print(df.head())
print(df.loc['audi', 'city'])

