
# coding: utf-8

# In[1]:

a = 2 
b = 2.0
c = "cadena"


# In[2]:

print c


# In[3]:

arr = [1,2,3,4]
arr


# In[4]:

import numpy as np
vec = np.array([0., 1., 3., 4.])
vec


# In[17]:

vec2 = np.arange(0,9,1, dtype=int)
vec2


# In[6]:

print np.zeros(10)


# In[16]:

vec3 = np.loadtxt("datos.txt", delimiter=",", dtype=int)
print vec3[3]
print len(vec3)
vec3


# In[18]:

mapr = np.array(map(lambda x,y: x+y, vec3,vec2))
print mapr


# In[21]:

print vec3.mean()
print vec3.min()
print vec3.max()


# In[32]:

col1 = np.genfromtxt("football.csv", usecols=(7), delimiter=",", dtype=None)
col1


# In[26]:

dt = np.genfromtxt("football.csv", usecols=(0,5,6,7), delimiter=",",
                   dtype=("|S10",float,float,float), names=True)
dt


# In[28]:

dt["Pts"].min()


# In[31]:

dt[7]


# In[34]:

mayor = reduce(lambda a,b: a if(a<b) else b, col1[1:] )
mayor


# In[39]:

di = dict(zip(dt["Team"],abs(dt["F"] - dt["A"])))
param = min(di.values())
resultado = [key for key,value in di.iteritems() if value == param]
resultado


# In[41]:

import json 
data = json.loads(open("pokemon.json","r").read())
print data[0]["name"]


# In[42]:

for poke in data:
    print poke["name"]


# In[ ]:



