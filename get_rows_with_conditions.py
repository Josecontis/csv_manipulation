import pandas as pd

'''get rows with a specific condition'''

# read in the first csv
df = pd.read_csv('CSV/Filename.csv')

df1 = df[(df.nameCol == 'example')]  # get all rows where nameCol is equal to example

# as we have seen we can add multiple condition in & or in |, that is the example:
# df1 = df[(df.Electrical == 'SBrkr') & (df['SalePrice'] >= 10000) & (df['SalePrice'] <= 150000) &
# (df['YearBuilt'] >= 1800) & (df['YearBuilt'] <= 1980)]

# write out the csv
df1.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values