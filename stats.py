# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:22:53 2016

@author: Xin
"""
import pandas as pd
from scipy import stats 

""" British survey of household spending on alcohol and tobacco """
data = """Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56"""


""" split the string on the newlines """
data = data.splitlines()

""" split each line on the commas """
data = [i.split(',') for i in data]

""" convert data into a pandas dataframe """
col_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=col_names)

""" convert Alcohol and Tobacco columns to float """
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

""" compute and print the mean, median and mode of Alcohol and Tobacco """
print ("The means of the Alcohol and Tobacco are {0} and {1},respectively".format(df['Alcohol'].mean(), df['Tobacco'].mean()))
print ("The medians of the Alcohol and Tobacco are {0} and {1},respectively".format(df['Alcohol'].median(), df['Tobacco'].median()))
print ("The modes of the Alcohol and Tobacco are {0} and {1},respectively".format(stats.mode(df['Alcohol']), stats.mode(df['Tobacco'])))

""" compute and print the range, var and std of Alcohol and Tobacco """
print ("The range of the Alcohol and Tobacco are {0} and {1},respectively".format(max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])))
print ("The standard deviation of the Alcohol and Tobacco are {0} and {1},respectively".format(df['Alcohol'].std(), df['Tobacco'].std()))
print ("The variance of the Alcohol and Tobacco are {0} and {1},respectively".format(df['Alcohol'].var(), df['Tobacco'].var()))