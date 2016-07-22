# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 21:30:39 2016

@author: Xin
"""

import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

data = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(data)

print(c)

# output frequencies of the data
count_sum = sum(c.values())

for k,v in c.iteritems():
    print("The frequency of number " + str(k) + " is " + str(float(v)/count_sum))
 
# output boxplot and histogram 
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.figure()
plt.boxplot(x)
plt.savefig("boxplot.png")

plt.figure()
plt.hist(x, histtype = 'bar')
plt.savefig("histogram,png")

# generate QQ-plot
plt.figure()
norm_data = np.random.normal(size = 1000)
graph1 = stats.probplot(norm_data, dist = "norm", plot = plt)
plt.savefig("QQ-plot of normally distributed data")

plt.figure()
uni_data = np.random.uniform(size = 1000)
graph1 = stats.probplot(uni_data, dist = "norm", plot = plt)
plt.savefig("QQ-plot of uniformly distributed data")


