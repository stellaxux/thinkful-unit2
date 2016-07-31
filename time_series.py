# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 15:52:11 2016

@author: Xin
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('LoanStats3b.csv', skiprows = 0, header = 1, nrows = 188123, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
resampled = dfts.resample('M', kind = 'period').count()
loan_count = resampled['issue_d']

# plot time series of loan count
plt.figure()
p = loan_count.plot() # not stationary
plt.xlabel('Time')
plt.ylabel('Loan Count')
plt.title('Time Series of Loan Count')
plt.show()

# plot ACF
plt.figure()
sm.graphics.tsa.plot_acf(loan_count)

# plot PACF
plt.figure()
sm.graphics.tsa.plot_pacf(loan_count)

# Differencing the time series and plot differenced time series
plt.figure()
loan_count_log = np.log(loan_count)
loan_count_log_diff = loan_count_log.diff()
loan_count_log_diff.dropna(inplace=True)
p = loan_count_log_diff.plot()

# plot ACF
plt.figure()
sm.graphics.tsa.plot_acf(loan_count_log_diff) # plot suggests MR(0)?

# plot PACF
plt.figure()
sm.graphics.tsa.plot_pacf(loan_count_log_diff) # plot suggests AR(0)?

# plots suggest no autocorrelated structures, would fit a random walk model
