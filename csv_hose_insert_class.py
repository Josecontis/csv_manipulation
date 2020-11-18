import numpy as np
import pandas as pd

'''constraints on one column in csv (columnToConstraints) and saving choices on another column (columnToWrite)'''

# read in the csv
df = pd.read_csv('CSV/Filename.csv')
# print(df.describe())  # describe csv file with max, min values and others..
# print(df.head())  # show the first 5 rows of csv

col = 'columnToConstraints'  # name of column to constraints in this case is an integer
# constraints:
conditions = [(df[col] >= 35310) & (df[col] <= 78430),
              (df[col] > 78430) & (df[col] <= 121550),
              (df[col] > 121550) & (df[col] <= 164670),
              (df[col] > 164670) & (df[col] <= 207790),
              (df[col] > 207790) & (df[col] <= 250910),
              (df[col] > 250910) & (df[col] <= 294030),
              (df[col] > 294030) & (df[col] <= 337150),
              (df[col] > 337150) & (df[col] <= 380270),
              (df[col] > 380270) & (df[col] <= 423390),
              (df[col] > 423390) & (df[col] <= 466510), ]
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L"]  # array of choices respectively for each conditions
df["columnToWrite"] = np.select(conditions, choices, default=np.nan)  # match conditions-choices

# write out the csv
df.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values

''' 
# other method with increments
df = pd.read_csv('CSV/Filename.csv')
col = 'columnToConstraints'
min=153000
max=3600000
inc=(max-min)/10
print(inc)
conditions = [(df[col] >= min) & (df[col] <= min+(inc*1)),
              (df[col] > min+(inc*1)) & (df[col] <= min+(inc*2)),
              (df[col] > min+(inc*2)) & (df[col] <= min+(inc*3)),
              (df[col] > min+(inc*3)) & (df[col] <= min+(inc*4)),
              (df[col] > min+(inc*4)) & (df[col] <= min+(inc*5)),
              (df[col] > min+(inc*5)) & (df[col] <= min+(inc*6)),
              (df[col] > min+(inc*6)) & (df[col] <= min+(inc*7)),
              (df[col] > min+(inc*7)) & (df[col] <= min+(inc*8)),
              (df[col] > min+(inc*8)) & (df[col] <= min+(inc*9)),
              (df[col] > min+(inc*9)) & (df[col] <= min+(inc*10)),
              (df[col] > min+(inc*10))]
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "X"]
df["columnToWrite"] = np.select(conditions, choices, default=np.nan)

df.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
'''