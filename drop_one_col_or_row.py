import pandas as pd

'''drop of single column or row in csv'''

# read in the csv
df = pd.read_csv('CSV/Filename.csv')
# print(df.describe())  # describe csv file with max, min values and others..
# print(df.head())  # show the first 5 rows of csv

df = df.drop('dropCol', 1)  # drop column dropCol (this is because there is 1)
df = df.drop('dropRow', 0)  # drop row dropRow (this is because there is 0)


# write out the csv
df.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values