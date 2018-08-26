
# coding: utf-8

# In[8]:


import pandas as pd


# In[10]:


import os
csvpath = os.path.join('Resources', 'budget_data.csv')
df1 = pd.read_csv(csvpath)
df1.head()


# In[11]:


month = print(len(df1["Date"]))


# In[12]:


sum1 = df1["Profit/Losses"].sum()


# In[20]:




