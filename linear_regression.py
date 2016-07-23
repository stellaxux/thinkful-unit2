# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:07:54 2016

@author: Xin
"""

import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range

# Remove the '%' symbols from the Interest.Rate column
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

# Remove the word 'months' from the Loan.Length column
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

# split each row at '-', getting a list of string
FICOScore= loansData['FICO.Range'].map(lambda x: x.split('-'))

# onvert string into a numerical value, and save it in a new column called FICOScore
FICOScore = FICOScore.map(lambda x: [int(n) for n in x])
FICOScore = FICOScore.map(lambda x: x[0])

# Add the new column FICO.Score into loansData
loansData['FICO.Score'] = FICOScore

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

# Create a scatterplot matrix
plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()
