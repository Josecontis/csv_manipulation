import pandas as pd

'''merge of 2 csv files'''

# read in the first csv
df1 = pd.read_csv('CSV/Filename.csv')
# read in the second csv
df2 = pd.read_csv('CSV/Filename2.csv')

df = df1.merge(df2, on='colToMerge')  # merge df1 and df2 on common column named: colToMerge

# write out the csv
df1.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values
