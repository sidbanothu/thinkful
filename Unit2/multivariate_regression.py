# import pandas as pd
# import numpy as np
# import statsmodels.api as sm
# import statsmodels.formula.api as smf

# df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
# X = df_adv[['TV', 'Radio']]
# y = df_adv['Sales']
# print df_adv.head()

# ##Option1
# X = sm.add_constant(X)
# est = sm.OLS(y, X).fit()
# print est.summary()
# ##Option2 
# est = smf.ols(formula='Sales ~ TV + Radio', data=df_adv).fit()
# print est.summary()
###################################################
# df = pd.read_csv('http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data', index_col=0)

# X = df.copy()
# y = X.pop('chd')

# print df.head()
# print y.groupby(X.famhist).mean()

# df['famhist_ord'] = pd.Categorical(df.famhist).labels
# est = smf.ols(formula="chd ~ famhist_ord", data=df).fit()

# print est.summary()
###################################################


import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('LoanStats3a.csv', skiprows=1)
# Drop null rows
print loansData.dtypes

print loansData.head()
### This messes it up?? 
##loansData.dropna(inplace=True)

### cleanInterestRate
# cleanInterestRate = loansData['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
# type(cleanInterestRate)
# loansData['int_rate']= cleanInterestRate
# print loansData['int_rate'].describe() 

# ###Clean Fico Range
# cleanFICORange = loansData['FICO.Range'].map(lambda x: int(str(x).split('-')[0]))
# type(cleanFICORange)
# loansData['FICO.Range']= cleanFICORange
# # print type(loansData['FICO.Range'].values[0])

# ####clean Amount.Requested
cleanAmountRequested = loansData['Loan.Length'].map(lambda x: int( str(x.rstrip(' months')) ))
type(cleanAmountRequested)
loansData['Loan.Length']= cleanAmountRequested
print cleanAmountRequested.head
# ######################################################
# ##What do I here for values.. how to use ::
# # print loansData['FICO.Range'].values[:][1]

# ##How to read into the cells
# #print loansData['FICO.Range'][0:5].values[0][1]

# # plt.figure()
# # p = loansData['Loan.Length'].hist()
# # plt.show()
# ######################################################
# # a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

# # plt.show()


# intrate = loansData['Interest.Rate']
# loanamt = loansData['Amount.Requested']
# fico = loansData['FICO.Range']


# # The dependent variable
# y = np.matrix(intrate).transpose()
# # The independent variables shaped as columns
# x1 = np.matrix(fico).transpose()
# x2 = np.matrix(loanamt).transpose()

# x = np.column_stack([x1,x2])

# X = sm.add_constant(x)
# model = sm.OLS(y,X)
# f = model.fit()

# print f.summary()

# #### How do I read the summary