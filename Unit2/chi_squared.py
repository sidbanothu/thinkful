from scipy import stats
import pandas as pd
import collections
import matplotlib.pyplot as plt 


# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

# freq = collections.Counter(loansData['Open.CREDIT.Lines'])
# print freq
#plt.figure()

plt.bar(freq.keys(), freq.values(), width = 1)
plt.show()

chi, p = stats.chisquare(freq.values())

print chi
print p

### why is the result p=0; How do I read this. 
# Assuming I reject he null hypothesis?