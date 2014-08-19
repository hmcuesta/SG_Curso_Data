
# coding: utf-8

# In[1]:

get_ipython().system(u'pip install twython')


# In[6]:

from twython import Twython

ConsumerKey  = "41E1twaPLNgsn0Q4VS5g"
ConsumerSecret = "augwZxzQGsJuyfzLzGn0ASpherv2YgpeLTKEXXFk"
AccessToken = "141340589-WhKonOAcDmCX1MVJNpd3UEB2gvzZt2nmPBJfMy3o"
AccessTokenSecret = "LDsdOa9Mex2yZ0AMud4eUe0mlcqvvsycwp0yneSWQw"


twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)

result = twitter.search(q="batman")

for status in result["statuses"]:
    print "Usuario:" + status["user"]["name"] +  "\n " + status["text"]


# In[10]:

time = twitter.get_user_timeline(screen_name = "RevistaSG", count = 5)
for tweet in time:
    print " \n User: " + tweet["user"]["name"] 
    print " \n Created: \n " + tweet["created_at"] 
    print " \n Text: \n " + tweet["text"]


# In[11]:

import json
with open("TL.json", "w") as archivo:
    json.dump(time,archivo)


# In[15]:

followers = twitter.get_followers_list(screen_name="hmcuesta")

for follower in followers["users"]:
    print " \n Usuario:" + follower["screen_name"] 
    print " \n        Nombre:" + follower["name"]
    print " \n        Numero de twitts:  " + str(follower["statuses_count"])
    


# In[18]:

tendencias = twitter.get_place_trends(id = 23424977 )

if tendencias:
    for trend in tendencias[0].get("trends", []):
        print "\n" + trend["name"]


# In[ ]:



