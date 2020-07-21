#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

url= 'https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'
US_fuel_data= pd.read_csv(url, error_bad_lines=False) 


US_fuel_data.describe(include='all')

# Question 1
A = [1,2,3,4,5,6]
B = [13, 21, 34]
A_B = A.extend(B)
print(A_B)

#Question 2

np.identity(3)

np.array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

#question 3
US_fuel_data.groupby('fuel_type_code_pudl').mean()


#question 4a
US_fuel_data.dropna().loc[:,'fuel_mmbtu_per_unit'].std()


#question 4b
US_fuel_data.dropna().loc[:,'fuel_mmbtu_per_unit'].quantile(0.75)

#question 5
US_fuel_data.loc[:,'fuel_qty_burned'].kurtosis()

US_fuel_data.loc[:,'fuel_qty_burned'].skew()

#question 6
US_fuel_data.isnull().sum()

US_fuel_data.dropna()

#question 9
US_fuel_data.groupby(['fuel_type_code_pudl', 'report_year'])[ 'fuel_qty_burned'].sum()

# question 9
perc_change = (8.98 - 7.17)/8.98
print(perc_change)

#question10
US_fuel_data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()




