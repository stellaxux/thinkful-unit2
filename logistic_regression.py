# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:47:13 2016

@author: Xin
"""

import pandas as pd
import statsmodels.api as sm
from math import exp
import matplotlib.pyplot as plt

data = pd.read_csv('loansData_clean.csv')

# Add a column indicating whether the interest rate is < 12%
data['IR_TF'] = (data['Interest.Rate'] < 0.12).astype('int') 

data['constant'] = 1.0

ind_vars = ['constant', 'FICO.Score', 'Amount.Requested']

# Define the logistic regression model

logit = sm.Logit(data['IR_TF'], data[ind_vars])
result = logit.fit()

# Get the fitted coefficients
coeff = result.params
print(coeff)

# logistic function
def logistic_function(ficoscore, loanamt, coeff):
    p = 1/(1 + exp(- coeff[0] - coeff[1]*ficoscore - coeff[2]*loanamt))
    return p
    
# Determine the prob using logistic funtion
p = logistic_function(720, 10000, coeff)
print ('The probability that we can obtain a loan at <=12% interest for $10,000 \
with a FICO score of 720 is ' + str(p))

# Plot predicted probability
ficoscore = range(550, 950, 10)
y = []
for i, x in enumerate(ficoscore):
    y.append(logistic_function(x, 10000, coeff))

plt.figure()
plt.plot(ficoscore, y, 'g-')
plt.xlabel('Fico Score')
plt.ylabel('Probability and decision, yes = 1, no = 0')
plt.show()