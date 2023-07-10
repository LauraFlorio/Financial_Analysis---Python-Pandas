#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dataset source: https://www.kaggle.com/datasets/nitindatta/finance-data?select=Finance_data.csv


# In[2]:


# !pip install numpy


# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


sns.set_style("darkgrid")


# In[5]:


df = pd.read_csv("D:\Mente\Programacao\Python\Financial Analysis\Projeto1\Finance_data.csv")


# In[6]:


df.head()


# In[7]:


condicoes = [(df['Mutual_Funds'] == 1), 
             (df['Equity_Market'] == 1), 
             (df['Debentures'] == 1),
             (df['Government_Bonds'] == 1),
             (df['Fixed_Deposits'] == 1),
             (df['PPF'] == 1),
             (df['Gold'] == 1)]
opcoes = ['Mutual_Funds', 'Equity_Market', 'Debentures', 'Government_Bonds', 'Fixed_Deposits', 'PPF', 'Gold']
df['Preferred_Inv_Option'] = np.select(condicoes, opcoes)
df


# In[8]:


data = df["gender"].value_counts()
colors = sns.color_palette("Set3")
plt.pie(data, labels=data.index, autopct='%.0f%%', colors=colors, shadow=True, explode=[0.05,0.05])
plt.title("GENDER OF THE PARTICIPANTS", fontsize=10)
plt.show()


# In[9]:


graph2 = sns.countplot(x="age", data=df, palette="Set2", linewidth=1, edgecolor="black")
for label in graph2.containers:
    graph2.bar_label(label, padding=3)
graph2.set(ylabel=None,xlabel=None,yticklabels=[])
plt.title("AGE OF THE PARTICIPANTS", fontsize=10)
plt.show()


# In[10]:


plt.figure(figsize=(17,7))
graph3=plt.subplot(1,2,1)
sns.countplot(x=df["gender"], hue=df["Investment_Avenues"], palette="summer", linewidth=3, edgecolor="white")
for label in graph3.containers:
    graph3.bar_label(label, size=13, padding=2)
graph3.set(ylabel=None,xlabel=None,yticklabels=[])
graph3.xaxis.set_tick_params(labelsize=12)
plt.legend(fontsize=14)
plt.title("INVESTMENT AVENUE", fontsize=12)

graph4=plt.subplot(1,2,2)
sns.countplot(x=df['gender'],hue=df["Stock_Marktet"], palette="hot", linewidth=3, edgecolor="white")
for label in graph4.containers:
    graph4.bar_label(label, size=13, padding=2)
graph4.set(ylabel=None,xlabel=None,yticklabels=[])
graph4.xaxis.set_tick_params(labelsize=12)
plt.legend(fontsize=14)
plt.title("STOCK MARKET", fontsize=12)

plt.show()


# In[11]:


graph5=sns.countplot(x=df["Factor"], palette="coolwarm", linewidth=2, edgecolor="black")
for label in graph5.containers:
    graph5.bar_label(label)
graph5.set(ylabel=None,xlabel=None,yticklabels=[])
plt.title("FACTOR CONSIDERED FOR INVESTING", fontsize=12)
plt.show()


# In[12]:


plt.figure(figsize=(10,5))
graph6=sns.pointplot(x="Purpose", y="age", data=df, linestyles="--", capsize=.3, color="Blue")
plt.title("INVESTMENT OBJECTIVE")
graph6.set(xlabel=None)
graph6.set_ylabel("Age",size=10)
graph6.xaxis.set_tick_params(labelsize=10)
graph6.yaxis.set_tick_params(labelsize=10)
plt.show()


# In[13]:


plt.figure(figsize=(15,5))
graph7=plt.subplot(1,2,1)
sns.countplot(y=df["Duration"], hue=df["gender"], palette="viridis", linewidth=2, edgecolor="black")
for label in graph7.containers:
    graph7.bar_label(label, size=12, padding=3)
graph7.set(ylabel=None,xlabel=None,xticklabels=[])
graph7.yaxis.set_tick_params(labelsize=13)
plt.legend(fontsize=12)
plt.title("DURATION", fontsize=15)

plt.subplot(1,2,2)
graph8=sns.countplot(y=df["Invest_Monitor"], hue=df["gender"], palette="seismic", linewidth=2, edgecolor="black")
for label in graph8.containers:
    graph8.bar_label(label, size=12, padding=3)
graph8.set(ylabel=None,xlabel=None,xticklabels=[])
graph8.yaxis.set_tick_params(labelsize=13)
plt.legend(fontsize=12)
plt.title("MONITORIZATION FREQUENCY", fontsize=15)

plt.show()


# In[14]:


plt.figure(figsize=(9,5))
graph9 = sns.countplot(y="Preferred_Inv_Option", data=df, palette="Set2", linewidth=1, edgecolor="black",
                      order = df['Preferred_Inv_Option'].value_counts().index)
for label in graph9.containers:
    graph9.bar_label(label, padding=3)
graph9.set(ylabel=None,xlabel=None,xticklabels=[])
graph9.xaxis.set_tick_params(labelsize=10)
plt.title("INVESTMENT OPTIONS")
plt.show()


# In[15]:


plt.figure(figsize=(18,8))
graph10=sns.countplot(x=df["Preferred_Inv_Option"], hue=df["gender"], palette="viridis", linewidth=2, edgecolor="black")
for label in graph10.containers:
    graph10.bar_label(label, size=12, padding=3)
graph10.set(ylabel=None,xlabel=None,yticklabels=[])
graph10.xaxis.set_tick_params(labelsize=13)
plt.title("FAVOURITE INVESTMENT OPTION")
plt.legend(fontsize=12)
plt.show()


# In[ ]:




