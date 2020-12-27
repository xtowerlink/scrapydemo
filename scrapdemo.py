#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup


# In[14]:


url = "http://books.toscrape.com/index.html"
r = r = requests.get(url)
html = r.content
scraped = BeautifulSoup(html,"html.parser")


# In[18]:


scraped


# In[22]:


scraped.title


# In[23]:


scraped.find('title')


# In[24]:


scraped.title.text


# In[25]:


scraped.title.text.strip()


# In[26]:


title_text=scraped.title.text.strip()


# In[30]:


link_text=scraped.article.h3.a.text


# In[32]:


link_text=scraped.article.h3.a['title']


# In[35]:


items=scraped.find_all("article",class_="product_pod")


# In[36]:


items


# In[45]:


items=scraped.find_all("article",class_="product_pod")

titles=[]
for item in items:
    print(item.h3.a["title"])
    titles.append(item.h3.a['title'])


# In[46]:


titles


# In[58]:


title_links=scraped.find_all("a",title=True)
for link in title_links:
    print(link["title"])


# In[64]:


all_divs=scraped.select("div")


# In[65]:


all_price_elements=scraped.select(".product_pod")


# In[68]:


all_messages=scraped.select("#messages")


# In[73]:


ee=scraped.select("article h3 a")


# In[ ]:


rr=scraped.select("article,h3,a")


# In[75]:


scraped.select(".instock.aviliability")


# In[76]:


scraped.select(".product_pod p.instock.aviliability,.price_color")

