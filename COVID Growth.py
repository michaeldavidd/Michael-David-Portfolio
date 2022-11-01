#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install datascience')


# In[6]:


pip install datascience


# In[7]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datascience import *


# In[8]:


#import file
data = pd.read_csv("worldometer_coronavirus_daily_data.csv")
data.head()


# In[9]:


#Reduce data to country: US and column: cumulative_total_deaths
USdataold = data.loc[data["country"] == "USA"]
USdata =USdataold.iloc[:,[0,5]]
USdata


# In[28]:


#Create subintervals of USdata to more closely inspect data and rates of change
monthly = pd.read_csv("MonthySummary - Sheet1.csv")

#All dataframe names indicate the 100k previous deaths and dates
#Import the subsection files
k100deaths = pd.read_csv("100kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k200deaths = pd.read_csv("200kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k300deaths = pd.read_csv("300kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k400deaths = pd.read_csv("400kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k500deaths = pd.read_csv("500kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k600deaths = pd.read_csv("600kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k700deaths = pd.read_csv("700kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k800deaths = pd.read_csv("800kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
k900deaths = pd.read_csv("900kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
M1deaths = pd.read_csv("1Mdeaths - Sheet1.csv", index_col="date", parse_dates=True)


# In[83]:


plt.figure(figsize=(20,10))
plt.title("Monthly US COVID Deaths")
sns.barplot(x=monthly["date"], y=monthly["cumulative_total_deaths"])


# In[29]:


plt.figure(figsize=(20,10))
plt.title("Monthly US COVID Deaths")
sns.barplot(x=monthly["date"], y=monthly["cumulative_total_deaths"])plt.figure(figsize=(20,10))
plt.title("Monthly US COVID Deaths")
sns.barplot(x=monthly["date"], y=monthly["cumulative_total_deaths"])


# Suspect increase in rate of change starting at:
# <br> October 2020
# <br> August 2021
# <br> - lets look more closely

# In[104]:


plt.figure(figsize=(20,10))
k100deaths = pd.read_csv("100kdeaths - Sheet1.csv", index_col="date", parse_dates=True)
sns.lineplot(data=k100deaths)


# In[108]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k200deaths)


# In[110]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k300deaths)


# In[111]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k400deaths)


# In[112]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k500deaths)


# In[113]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k600deaths)


# In[114]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k700deaths)


# In[115]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k800deaths)


# In[116]:


plt.figure(figsize=(20,10))
sns.lineplot(data=k900deaths)


# In[117]:


plt.figure(figsize=(20,10))
sns.lineplot(data=M1deaths)


# Analyzing the data more closely, we can see:
# <br>
# <br> an **increase** in the rate of change in/around:
# <br> March 1 2020
# <br> November 1 2020
# <br> August 8 2021
# <br>
# <br> a **decrease** in the rate of change in/around:
# <br> February 2 2022
# <br> March 7 2021

# In[ ]:




