# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:17:39 2016

@author: Xin
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace = True)

print loansData[loansData.columns[0]]

# loansData.boxplot(column = 'Amount.Funded.By.Investors')
loansData.boxplot(column = 'Amount.Requested')
plt.show()


#loansData.hist(column = 'Amount.Funded.By.Investors')
loansData.hist(column = 'Amount.Requested')
plt.show()

plt.figure()
#gragh = stats.probplot(loansData['Amount.Funded.By.Investors'], dist = 'norm', plot = plt)
gragh = stats.probplot(loansData['Amount.Requested'], dist = 'norm', plot = plt)