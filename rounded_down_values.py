import pandas as pd
import numpy as np

'''rounded down of float values in the csv (in this case from 0 to 10.5)'''

# read in the csv
df = pd.read_csv('CSV/Filename.csv')
# print(df.describe())  # describe csv file with max, min values and others..
# print(df.head())  # show the first 5 rows of csv

col = 'columnToConstraints'  # name of column to constraints in this case is an integer
conditions = [(df[col] > 0) & (df[col] <= 0.5),
              (df[col] > 0.5) & (df[col] <= 1.5),
              (df[col] > 1.5) & (df[col] <= 2.5),
              (df[col] > 2.5) & (df[col] <= 3.5),
              (df[col] > 3.5) & (df[col] <= 4.5),
              (df[col] > 4.5) & (df[col] <= 5.5),
              (df[col] > 5.5) & (df[col] <= 6.5),
              (df[col] > 6.5) & (df[col] <= 7.5),
              (df[col] > 7.5) & (df[col] <= 8.5),
              (df[col] > 8.5) & (df[col] <= 9.5),
              (df[col] > 9.5) & (df[col] <= 10.5)]
choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
df[col] = np.select(conditions, choices, default=np.nan)

# write out the csv
df.to_csv('CSV/outputFilename.csv', index=False, float_format='%.0f')
# index = false do not insert the index on output csv file,
# float format do not insert decimal in all the integer values
