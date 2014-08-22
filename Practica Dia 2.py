
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
serie = pd.Series(np.arange(20,30))
serie


# In[3]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
serie.plot()


# In[8]:

ts = pd.read_csv("Gold.csv", index_col=0, parse_dates=True)
ts.plot()


# In[10]:

print ts.head()
print ts.tail()


# In[11]:

ts.describe()


# In[12]:

ts.std()


# In[14]:

ts["2010":"2012"].plot()


# In[15]:

muestra = ts.resample("A")
muestra


# In[18]:

muestra.plot(style = "r--")


# In[20]:

muestra2 = ts.resample("A", how=["mean", np.max, np.min])
muestra2.plot()


# In[21]:

muestra2.plot(subplots=True)


# In[22]:

mts = pd.read_csv("multiLine.csv", index_col=0, parse_dates=True)
mts.head()


# In[23]:

mts.plot()


# In[24]:

mts.corr()


# In[26]:

mts[:11]


# In[29]:

print np.tan(ts[:5])
print ts[:5]


# In[32]:

print mts["EUR"][:10]


# In[33]:

print np.tan(mts["EUR"][:10])


# In[39]:

mts.query("USD < 1 and EUR > 0.8")


# In[41]:

mts[(mts.USD < 1)&(mts.EUR > 0.8)]


# In[42]:

mts.duplicated(["USD","EUR"])


# In[46]:

ts[(ts.index.month == 4)]


# In[47]:

fun = lambda x: x.max() - x.min()
ts.apply(fun)


# In[48]:

plt.pie(pd.DataFrame([2,3,5,6]))


# In[51]:

jdata = pd.read_json("pokemons.json")
jdata.plot(kind="bar")


# In[53]:

jdata.plot(kind="area", stacked=False)


# In[55]:

plt.pie(jdata["amount"], labels= jdata["type"])


# In[56]:

iris = pd.read_csv("iris.csv")
iris.describe()


# In[57]:

pd.tools.plotting.radviz(iris,"name")


# In[59]:

pd.tools.plotting.andrews_curves(iris,"name", colormap="winter")


# In[63]:

iris.groupby("name").min()


# In[64]:

iris.groupby("name").describe()


# In[65]:

iris.corr()


# In[67]:

iris["SepalLength"].corr(iris["PetalLength"])


# In[70]:

iris[:10].plot(kind="bar", colormap="Greens")


# In[71]:

n = 100
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.plot(X,Y,"ro")


# In[72]:

casa = pd.read_csv("house.csv")
casa


# In[77]:

plt.plot(casa["size"],casa["price"],"ro", color="blue")


# In[ ]:



