import pandas as pd

df = pd.read_csv('words.csv', index_col='Word')
df.head()

df.info

df.loc['microspectrophotometries']

df['Value'].max()

df.loc[['superheterodyne', 'pinfish', 'enfold', 'glowing', 'microbrew'], 'Char Count']

df['Char Count'].max()

df.loc[df['Value'] == 319]

[df['Value'].mode()]

df.loc[
    (df['Value'] == 274) & 
    (df['Char Count'] == df.loc[df['Value'] == 274, 'Char Count'].min())
]

df['Ratio'] = df['Value'] / df['Char Count']
df.head

df['Ratio'].max()

df.loc[df['Ratio'] == 10].count()

df.loc[df['Value'] == 10, 'Char Count'].max()

df.loc[df['Ratio'] == 10, 'Value']

df.loc[df['Value'] == 260,'Char Count'].min()

df.loc[
    (df['Value'] == 260) & 
    (df['Char Count'] == df.loc[df['Value'] == 260,'Char Count'].min())


]