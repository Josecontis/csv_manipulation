import pandas as pd
import numpy as np

'''count the number of occurrences on column of csv file'''

# read in the csv
df = pd.read_csv('CSV/Filename.csv')
# print(df.describe())  # describe csv file with max, min values and others..
# print(df.head())  # show the first 5 rows of csv

col = np.array(df['colName'])  # this method allows to convert a single column colName into array
i = 0  # index
c = 0  # counter
for i in range(0, len(col)):  # loop to read each single elem of array
    if col[i] == 'A':  # verify the matching with character to find
        c = c + 1  # count number of occurrences
        # print(i)
print('total: ', c)  # print the total of A character in colName