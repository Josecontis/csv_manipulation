import pandas as pd

'''outer join of 2 csv files'''

# read in the first csv
df1 = pd.read_csv('CSV/Filename.csv')
# read in the second csv
df2 = pd.read_csv('CSV/Filename2.csv')

df1.update(df2, join='outer')  # join between df1 and df2 with outer join
# for other join methods see the doc of update method on join parameter

# write out the csv
df1.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values