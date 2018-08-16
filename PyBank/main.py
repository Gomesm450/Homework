
# coding: utf-8

# In[1]:


import pandas as pd


# In[24]:


import os
os.chdir("C:/Users/gomes/Desktop/CWCL201807DATA2-Class-Repository-DATA/Homework/hmw3Python/PyBank/Resources")
df1 = pd.read_csv("budget_data.csv")
df1.head()


# In[26]:


print(len(df1["Date"]))


# In[29]:


df1["Profit/Losses"].sum()

