# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:28:48 2016

@author: Xin
"""

from scipy import stats
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Drop null rows
loansData.dropna(inplace = True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width = 1)
plt.show()

# perform a chi-squared test
chi, p = stats.chisquare(freq.values())

