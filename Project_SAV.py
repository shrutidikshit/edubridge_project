#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as mp


# In[3]:


#Loading CSV
data=pd.read_csv('cars.csv')
data.head()


# In[4]:


data.info()


# In[3]:


#Checking Null Values
data.isnull()


# In[4]:


#remove dupicate
data.duplicated()


# In[7]:


#Reading specific columns using multy axex indexing
print (data.loc[[1,2,3,4,5,6,7,8,9,10],['Brand','Price']])


# In[9]:


#Grouping Function
grouped=data.groupby('Year')
print(grouped.get_group(2014))


# In[27]:


#data analysis
#mean
import statistics
print (np.mean(data.Mileage))


# In[34]:


#mode
print(data.mode)


# In[35]:


#Data Visualisation
#box plot
data.plot.box(grid='True')
mp.savefig('boxplot.png')


# In[51]:


mp.scatter(data.Brand,data.Mileage,color='red')
mp.xlabel('Brand')
mp.ylabel('Mileage')
mp.title('Mileage_Brand')
mp.savefig('scatter.png')


# In[49]:


#bar plot
data.plot(x='Brand',y='Price',color='blue')
mp.title('Brand_wise_Price')
mp.savefig('bar.png')


# In[ ]:




