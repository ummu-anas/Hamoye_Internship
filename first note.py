#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy 
import numpy as np
a=([1,3,5,7],[2,4,6,8])
a=np.array(a)
print (type(a))
print (a.shape)
print (a.dtype)
print (a.ndim)


# In[2]:


a[0,1:3]


# In[3]:


np.zeros((1,2))


# 
# print (np.matmul(a,b))
# 

# In[ ]:





# b=np.array(([2,4,8,16],[3,6,9,12],[4,8,12,16],[5,10,15,20]))
# 
# 

# In[ ]:





# In[4]:


np.ones((3,3,5))


# In[5]:


a=np.array(([1,3,5,7],[2,4,6,8]))
b=np.array(([2,4,8,16],[3,6,9,12]))
print (a*b)


# In[6]:


np.identity(3)


# In[7]:


# importing pandas
import pandas as pd
days=pd.Series(["monday","tuesday",'wednesday'],index=[1,2,3])
print (days)


# In[8]:


dfdict= {'Country': ['Ghana', 'Kenya', 'Nigeria', 'Togo'],
           'Capital': ['Accra', 'Nairobi', 'Abuja', 'Lome'],
           'Population': [10000, 8500, 35000, 12000],
           'Age': [60, 70, 80, 75]}
df=pd.DataFrame(dfdict,index=[1,2,3,4])
print (df)


# In[9]:


df.iloc[2]


# In[10]:


df.loc[4]


# In[11]:


df['Age']


# In[12]:


df.at[3,"Capital"]


# In[13]:


df.iat[2, 1]


# In[14]:


df["Population"].sum()


# In[15]:


df.mean()


# In[16]:


dfdict2={'Name': ['James', 'Yemen', 'Caro', np.nan],
           'Profession': ['Researcher', 'Artist', 'Doctor', 'Writer'],
           'Experience': [12, np.nan, 10, 8],
           'Height': [np.nan, 175, 180, 150]}
df1=pd.DataFrame(dfdict2)
print(df1)


# In[17]:


df1.isnull()


# df1.dropna()

# In[18]:


df1.dropna()


# In[19]:


df.describe()


# In[21]:


url='https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
fuel_data=pd.read_csv(url,error_bad_lines=False)
fuel_data.describe(include="all")


# In[22]:


fuel_data.isnull().sum()


# In[39]:


fuel_data.groupby("fuel_unit").count()
fuel_data['fuel_unit']=fuel_data["fuel_unit"].fillna(value='mcf')


# In[40]:


fuel_data.isnull().sum()


# In[38]:


fuel_unit.describe()


# In[29]:


fuel_unit.describe()


# In[30]:


fuel_data.groupby("fuel_unit")


# In[37]:


fuel_data.groupby(['fuel_unit'])['fuel_unit'].count()


# In[41]:


fuel_data.groupby('report_year')['report_year'].count()


# In[43]:





# In[46]:


fuel_df1 = fuel_data.iloc[0:19000].reset_index(drop=True)
fuel_df2 = fuel_data.iloc[19000:].reset_index(drop=True)
assert len(fuel_data) == (len(fuel_df1) + len(fuel_df2))
pd.merge(fuel_df1, fuel_df2, how="inner")


# In[47]:


pd.merge(fuel_df1, fuel_df2, how="outer")


# In[48]:


pd.merge(fuel_df1, fuel_df2, how="left")


# In[49]:


fuel_data.duplicated().any()


# In[51]:


pd.concat([fuel_df1,fuel_df2]).reset_index(drop=True)


# In[54]:


#importing plotting library
import matplotlib.pyplot as plt
plt.figure(figsize=(7,4))
plt.xticks(rotation=90)
fuel_unit = pd.DataFrame({'unit':['BBL', 'GAL', 'GRAMSU', 'KGU', 'MCF', 'MMBTU', 'MWDTH', 'MWHTH', 'TON'],
            'count':[7998, 84, 464, 110, 11354, 180, 95, 100, 8958]})

import seaborn as sns
g = sns.barplot(data=fuel_unit, x='unit', y='count')
g.set_ylim(1, 12000)
plt.xlabel('Fuel Unit')


# In[56]:


import matplotlib.pyplot as plt
plt.figure(figsize=(7,4))
plt.xticks(rotation=90)
fuel_unit = pd.DataFrame({'unit':['BBL', 'GAL', 'GRAMSU', 'KGU', 'MCF', 'MMBTU', 'MWDTH', 'MWHTH', 'TON'],
            'count':[7998, 84, 464, 110, 11354, 180, 95, 100, 8958]})

import seaborn as sns
g = sns.barplot(data=fuel_unit, x='unit', y='count')
g.set_ylim(1, 12000)
g.set_yscale("log")
g.set_ylim(1, 12000)
plt.xlabel('Fuel Unit')


# In[57]:


#box plot
sns.boxplot(x="fuel_type_code_pudl", y="utility_id_ferc1",
            palette=["m", "g"], data=fuel_data)


# In[58]:


#kde plot
sample_df = fuel_data.sample(n=50, random_state=4)
sns.kdeplot(sample_df['fuel_cost_per_unit_burned'], shade=True, color="b")


# In[59]:


#reg plot
sns.regplot(x=sample_df["utility_id_ferc1"], y=sample_df["fuel_cost_per_mmbtu"], fit_reg=False)


# In[ ]:




