import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

### cleanInterestRate
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
type(cleanInterestRate)

loansData['Interest.Rate']= cleanInterestRate

###Clean Fico Range
cleanFICORange = loansData['FICO.Range'].map(lambda x: int(str(x).split('-')[0]))
type(cleanFICORange)
loansData['FICO.Range']= cleanFICORange
# print type(loansData['FICO.Range'].values[0])

####clean Amount.Requested
cleanAmountRequested = loansData['Loan.Length'].map(lambda x: int( str(x.rstrip(' months')) ))
type(cleanAmountRequested)
loansData['Loan.Length']= cleanAmountRequested
#print cleanAmountRequested[0:5]
######################################################
##What do I here for values.. how to use ::
# print loansData['FICO.Range'].values[:][1]

##How to read into the cells
#print loansData['FICO.Range'][0:5].values[0][1]

# plt.figure()
# p = loansData['Loan.Length'].hist()
# plt.show()
######################################################
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

# plt.show()


intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']


# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()

#### How do I read the summary