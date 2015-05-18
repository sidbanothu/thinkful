import matplotlib.pyplot as plt 
import pandas as pd
import scipy.stats as stats


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#drop rows with null values
loansData.dropna(inplace=True)

data = [i.split(', ') for i in loansData]
cols = data[0::]
print cols

##Why is opening on csv off by column?
##Why cant i read it as loansData[0][1]
#print loansData['Amount.Requested']
#how can i pop-up both plots at same time?


## Analyze amount funded by investors
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

#what does plot.figure do?
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()


## Analyze amount reequested
loansData.boxplot(column='Amount.Requested')
plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()


# See how they compare
### How can i visualze data on top of each other?

# print("Mean for Amount.Requested:", (loansData['Amount.Requested'].mean()))
# print("Median for Amount.Requested:", (loansData['Amount.Requested'].median()))
# print("Mode for Amount.Requested:", (loansData['Amount.Requested'].mode()))
# print("Range for Amount.Requested:", ( max(loansData['Amount.Requested']) - min(loansData['Amount.Requested']) ) )
# print("Variance for Amount.Requested:", (loansData['Amount.Requested'].var()))
# print("Standard Deviation for Amount.Requested:", (loansData['Amount.Requested'].std()))

# print("\n")
# print("Mean for Amount.Funded.By.Investors:", (loansData['Amount.Funded.By.Investors'].mean()))
# print("Median for Amount.Funded.By.Investors:", (loansData['Amount.Funded.By.Investors'].median()))
# print("Mode for Amount.Funded.By.Investors:", (loansData['Amount.Funded.By.Investors'].mode()))
# print("Range for Amount.Funded.By.Investors:", ( max(loansData['Amount.Funded.By.Investors']) - min(loansData['Amount.Funded.By.Investors']) ) )
# print("Variance for Amount.Funded.By.Investors:", (loansData['Amount.Funded.By.Investors'].var()))
# print("Standard Deviation for Amount.Funded.By.Investors:", (loansData['Amount.Funded.By.Investors'].std()))


cols = ["Stat", "Amount Requested", "Amount Funded"]
data_rows = [	["Mean", loansData['Amount.Requested'].mean(), loansData['Amount.Funded.By.Investors'].mean()],
				["Median", loansData['Amount.Requested'].median(), loansData['Amount.Funded.By.Investors'].median()],
#				["Mode", loansData['Amount.Requested'].mode(), loansData['Amount.Funded.By.Investors'].mode()],
				["Range", max(loansData['Amount.Requested']) - min(loansData['Amount.Requested']) ,  max(loansData['Amount.Funded.By.Investors']) - min(loansData['Amount.Funded.By.Investors']) ],
				["Variance", loansData['Amount.Requested'].var(), loansData['Amount.Funded.By.Investors'].var()],
				["Standard Deviation", loansData['Amount.Requested'].std(), loansData['Amount.Funded.By.Investors'].std()]

			]
table = pd.DataFrame(data_rows, columns = cols)

print table