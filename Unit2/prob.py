## Output Frequency, boxplot, histogram, qq plot. Save all them as png files

import collections
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

x_freq = collections.Counter(x);

print x_freq

plt.boxplot(x)
plt.savefig("boxplot.png")
plt.show()

plt.hist(x, histtype = "bar")
plt.savefig("histogram.png")
plt.show()

qq_norm = stats.probplot(x, dist="norm", fit = True, plot = plt)
plt.savefig("qq_norm.png")
plt.show()