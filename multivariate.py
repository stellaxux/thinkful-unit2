# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:28:35 2016

@author: Xin
"""
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('LoanStats3b.csv', skiprows = 0, header = 1, nrows = 188123)

# Remove the '%' symbols from the int_rate column
df['int_rate'] = df['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

# Use income (annual_inc) to model interest rates (int_rate)
# X = df['annual_inc']
# y = df['int_rate']
# X = sm.add_constant(X)

model = smf.ols(formula = 'int_rate ~ annual_inc', data = df)
f = model.fit()
f.summary()

# Add home_ownership, first code it into numerical
homeownership = df['home_ownership']
homeownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in homeownership]
model1 = smf.ols(formula = 'int_rate ~ annual_inc + homeownership', data = df)
f1 = model1.fit()
f1.summary()


# Add the interaction of home ownership and incomes as a term
# model2 = smf.ols(formula = 'int_rate ~ annual_inc * homeownership', data = df)
model2 = smf.ols(formula = 'int_rate ~ annual_inc * C(home_ownership)', data = df)
f2 = model2.fit()
f2.summary()
