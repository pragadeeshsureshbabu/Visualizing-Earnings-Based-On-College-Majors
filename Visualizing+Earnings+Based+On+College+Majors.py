
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
recent_grads= pd.read_csv("recent-grads.csv")
print(recent_grads.head(2))
get_ipython().magic('matplotlib inline')


# In[3]:


recent_grads.describe()


# In[4]:


recent_grads= recent_grads.dropna()


# In[7]:


fig,ax= plt.subplots()
ax.scatter(recent_grads["Sample_size"], recent_grads["Median"])


# In[8]:


fig, ax1 = plt.subplots()
ax1.scatter(recent_grads["Sample_size"], recent_grads["Unemployment_rate"])


# In[18]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[11]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# In[16]:



recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[17]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# In[34]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(8,20))
for r in range(1,8):
    ax = fig.add_subplot(8,1,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=0)


# In[35]:


from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))


# In[36]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# In[38]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen')
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[39]:


recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate')
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate', legend=False)

