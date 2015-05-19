import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import math
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


loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 0 if (x<0.12) else 1)


###Why dont I need to do this anymore?

# The dependent variable
# y = np.matrix(loansData['Interest.Rate']).transpose()

# The independent variables shaped as columns
# x1 = np.matrix(loansData['FICO.Range']).transpose()
# x2 = np.matrix(loansData['Amount.Requested']).transpose()

# x = np.column_stack([x1,x2])
# X = sm.add_constant(x)

###How do I add constant to end? or middle or beginning? How do I add 2 as constant
###What is logit? what is fit?
###What is optimization terminated successfully with function value = 0.049104?

loansData['intercept'] = 1
ind_vars = ['intercept','Amount.Requested', 'FICO.Range']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

result = logit.fit()
coeff = result.params
print coeff
### I dont think the coefficients are correct
		# intercept           60.171952
		# Amount.Requested     0.000174
		# FICO.Range          -0.087480
# print "\n"
# print coeff[0]
# print "\n"
# print coeff[1]
# print "\n"

def logistic_function( FicoScore,LoanAmount):
	p = 1/(1 + math.exp( coeff[0] + (coeff[1]*LoanAmount) - (coeff[2]*FicoScore) ) )
	return p

p = logistic_function(800, 100000)

print p
## value = 2.688 e-55 which is not right?
