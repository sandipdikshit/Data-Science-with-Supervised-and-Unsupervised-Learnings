#!/usr/bin/env python
# coding: utf-8

# # SANDIP DIKSHIT
# 

# Objective: To Perform Exploratory Data Analysis on the SampleSuperstore Dataset
# 

# In[66]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[91]:


superstore = pd.read_csv("Downloads/SampleSuperstore.csv")


# In[24]:


superstore.head()


# In[25]:


superstore.shape


# # There are 9994 columns and 13 rows in this dataset

# In[26]:


superstore.columns


# In[27]:


superstore.nunique(axis =0)


# In[32]:


superstore.describe()


# # Clean the Data
# isnull() finds out the null values so that we can remove them out of the dataset

# sum() summation of those values (ifany)

# duplicated() searches for duplicates in the data set to eliminate redundancy

# In[33]:


superstore.isnull().sum()


# In[34]:


superstore.duplicated().sum()


# Lets drop these 17 duplicated entries now. (shoot them out :p) using drop_duplicates()

# In[35]:


store.drop_duplicates()


# # Some columns can add to extraa space and not contribute in analysis so we will eliminate those

# In[36]:


superstore = superstore.drop(['Country', 'Postal Code'], axis =1)


# In[37]:


superstore


# # Lets Analyse the Relationship between each columns

# In[38]:


store.info()


# # quite difficult right ?? 
# Let me make it easier and use the correlation matrix and plot it visually ;)

# In[39]:


correlation = superstore.corr()
correlation


# In[42]:


plt.figure(figsize = (15,10))
sns.heatmap(correlation, annot = True)


# we have positive correlation between Sales and Profit, Sales and quantity and a negative correlation between Profit and Discount.

# # Visualize the Dataset for better clarity

# In[44]:


sns.pairplot(superstore)


# In[53]:


print (superstore['City'].value_counts())
plt.figure(figsize=(15,15))
sns.countplot(x=superstore['City'], order=(superstore['City'].value_counts().head(40)).index)
plt.xticks(rotation=90)


# # I have taken 40 datasets to show the distribution & the graph is right skewed which means most of the sales revenue quality data is in the left side

# In[54]:


print (superstore['Sub-Category'].value_counts())
plt.figure(figsize=(10,9))
sns.countplot(x=superstore['Sub-Category'], order=(superstore['Sub-Category'].value_counts().head(40)).index)
plt.xticks(rotation=90)


# In[82]:


plt.figure(figsize=(12,6))
plt.pie(superstore['Segment'].value_counts(), labels=superstore['Segment'].value_counts().index, startangle=180, radius=1, shadow = True)
plt.title('Segments of people who buy items')
plt.show()


# In[102]:


plt.figure(figsize=(12,6))
plt.pie(superstore['Category'].value_counts(), labels=superstore['Category'].value_counts().index, startangle=180, radius=1)
plt.title('Categories of Items for Sale')
plt.show()


# In[103]:


plt.figure(figsize=(12,12))
plt.pie(superstore['Region'].value_counts(), labels=superstore['Region'].value_counts().index, startangle=180, radius=1)
plt.title('Regions from where Sales is made')
plt.show()


# In[ ]:




