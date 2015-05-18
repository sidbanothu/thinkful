import pandas as pd

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

#split reach row into a list
data = data.split('\n')

#slit each line and load to list
data = [i.split(', ') for i in data]

#set up loading to panda data fame
cols = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = cols)

print data_rows

print("\n")

df['Tobacco'] = df['Tobacco'].astype(float)
df['Alcohol'] = df['Alcohol'].astype(float)

print("Mean for Alcohol dataset:", (df['Alcohol'].mean()))
print("Median for Alcohol dataset:", (df['Alcohol'].median()))
print("Mode for Alcohol dataset:", (df['Alcohol'].mode()))
print("Range for Alcohol dataset:", ( max(df['Alcohol']) - min(df['Alcohol']) ) )
print("Variance for Alcohol dataset:", (df['Alcohol'].var()))
print("Standard Deviation for Alcohol dataset:", (df['Alcohol'].std()))

print("\n")
print("Mean for Tobacco dataset:", (df['Tobacco'].mean()))
print("Median for Tobacco dataset:", (df['Tobacco'].median()))
print("Mode for Tobacco dataset:", (df['Tobacco'].mode()))
print("Range for Tobacco dataset:", ( max(df['Tobacco']) - min(df['Tobacco']) ) )
print("Variance for Tobacco dataset:", (df['Tobacco'].var()))
print("Standard Deviation for Tobacco dataset:", (df['Tobacco'].std()))

#### Questions #####

#Why is stats not definedd?
#how to append to the dataframe?
#print(stats.mode(df['Tobacco']))

df2 = pd.DataFrame([["Mean", df['Tobacco'].mean(), df['Alcohol'].mean()]], columns = ['Region', 'Alcohol', 'Tobacco'])
df2 = pd.DataFrame([["Mean", df['Tobacco'].mean(), df['Alcohol'].mean()]], columns = ['Region', 'Alcohol', 'Tobacco'])

df3 = pd.concat([df, df2])

print df3
