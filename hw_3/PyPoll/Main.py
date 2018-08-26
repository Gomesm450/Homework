
# coding: utf-8

# In[15]:


import pandas as pd


# In[34]:


import os
csvpath = os.path.join('Resources', 'election_data.csv')
df1 = pd.read_csv(csvpath)
df1.head()


# In[36]:


votecount = df1['Candidate'].count()
votecount


# In[37]:


df1['Candidate'].unique()


# In[43]:


df1['Candidate'].value_counts()


# In[56]:


khan_count = 2218231
correy_count = 704200
li_count = 492940
OT_count = 105630

khan_percent = round((khan_count/votecount)*100) 
correy_percent = round((correy_count/votecount)*100)
li_percent = round((li_count/votecount)*100)
OT_percent = round((OT_count/votecount)*100)


# In[58]:


print("Total Votes:", votecount)
print("Khan:", khan_percent, "%", (khan_count))
print("Correy:", correy_percent, "%", (correy_count))
print("Li:", li_percent, "%", li_count)
print("O'Tooley", OT_percent, "%", OT_count)
print("Winner: Khan")

