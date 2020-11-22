import pandas as pd

# read in the csv
df = pd.read_csv('CSV/Filename.csv')
# save xlsx file
df1 = pd.ExcelWriter('CSV/outputFilename.xlsx')
df.to_excel(df1, index=False)
df1.save()
