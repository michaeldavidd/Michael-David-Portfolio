#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets 
iris = datasets.load_iris()  


# In[2]:


iris


# In[12]:


df = pd.DataFrame(iris.data, columns = iris.feature_names)
df


# In[13]:


#Extract the first 2 features
data = df.drop(["petal length (cm)", "petal width (cm)"], axis = "columns")
data


# In[17]:


plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width")
plt.scatter(data["sepal length (cm)"], data["sepal width (cm)"], color="purple")


# Looking at the plot, I think 2 clusters would be a good amount.

# In[58]:


#Create the k-Means object with n clusters
km = KMeans(n_clusters=2)
km


# In[59]:


y_predicted = km.fit_predict(data)
y_predicted


# In[60]:


km.cluster_centers_


# In[61]:


#Plotting the clusters
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1])


# In[62]:


#Plotting the clusters and the datapoints
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width")
plt.scatter(data["sepal length (cm)"], data["sepal width (cm)"], color="purple")
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], color="red")


# In[ ]:




