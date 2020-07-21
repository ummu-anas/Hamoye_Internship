#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url= 'https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'
US_fuel_data= pd.read_csv(url, error_bad_lines=False) 


# In[2]:


US_fuel_data.describe(include='all')


# In[3]:


# Question 1
A = [1,2,3,4,5,6]
B = [13, 21, 34]
A_B = A.extend(B)
print(A_B)


# In[4]:


#Question 2
import numpy as np
import pandas as pd



np.identity(3)


# In[ ]:





# In[5]:


np.array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])


# In[6]:


#question 3
US_fuel_data.groupby('fuel_type_code_pudl').mean()


# In[ ]:





# In[ ]:





# In[7]:


#question 6
US_fuel_data.isnull().sum()


# In[ ]:





# In[8]:


US_fuel_data.dropna()


# In[ ]:





# In[9]:


#question 4
US_fuel_data.dropna().loc[:,'fuel_mmbtu_per_unit'].std()


# In[10]:


#question 4
US_fuel_data.dropna().loc[:,'fuel_mmbtu_per_unit'].quantile(0.75)


# In[11]:


#question 5
US_fuel_data.loc[:,'fuel_qty_burned'].kurtosis()


# In[12]:


US_fuel_data.loc[:,'fuel_qty_burned'].skew()


# In[13]:


#question10
US_fuel_data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()


# In[36]:


#question 9
US_fuel_data.groupby(['fuel_type_code_pudl', 'report_year'])[ 'fuel_qty_burned'].sum()


# In[39]:


# question 9
perc_change = (8.98 - 7.17)/8.98
print(perc_change)


# 
# 

# In[ ]:




