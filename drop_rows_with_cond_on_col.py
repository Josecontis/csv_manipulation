import pandas as pd

'''drop rows that satisfy a single condition'''

# read in the csv
df = pd.read_csv('CSV/Filename.csv')
# print(df.describe())  # describe csv file with max, min values and others..
# print(df.head())  # show the first 5 rows of csv

# df = df[df.colName > 2.47e+006]  # return all rows that satisfy this condition
df = df[df.colName != 'A']
df = df[df.colName != 'B']
df = df[df.colName != 'C']
df = df[df.colName != 'D']
df = df[df.colName != 'E']
df = df[df.colName != 'F']
df = df[df.colName != 'G']
df = df[df.colName != 'H']
df = df[df.colName != 'I']
# df = df[df.colName != 'L'] in this case L character is excluded to drop rows
# the output will be all the whole csv without all rows that contains L as colName
# you can repeat the process with the other characters

# write out the csv
df.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values
