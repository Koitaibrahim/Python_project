#!/usr/bin/env python
# coding: utf-8

# In[8]:


# importation of the packages for this project
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None



# Now we need to read in the data
movies = pd.read_csv(r'C:\Users\koita\Desktop\movies.csv')


# In[10]:


# Now let's take a look at the data

movies


# In[9]:


# Now let's take a look at the data

movies


# In[11]:


# looking at only the first 5 colums
movies.head()


# In[12]:


#selecting only few colums
movies [['name', 'score', 'budget']]


# In[13]:


#getting a summary of the data
movies.describe


# In[14]:


# Data Types for our columns

print(df.dtypes)


# In[15]:


# Are there any Outliers?

df.boxplot(column=['gross'])


# In[16]:


movies.drop_duplicates()


# In[17]:


# Order our Data a little bit to see

movies.sort_values(by=['gross'], inplace=False, ascending=False)


# In[18]:


sns.regplot(x="gross", y="budget", data=movies)


# In[19]:


sns.regplot(x="score", y="gross", data=movies)


# In[20]:


# Correlation Matrix between all numeric columns

movies.corr(method ='pearson')


# In[22]:


movies ['score'].mean


# In[23]:


movies ['score'].max


# In[24]:


movies ['score'].min


# In[25]:


#Getting Data lengh
len (movies)


# In[ ]:




