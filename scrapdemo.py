#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/index.html"
r = r = requests.get(url)
html = r.content
scraped = BeautifulSoup(html,"html.parser")

scraped.title

scraped.find('title')

scraped.title.text

scraped.title.text.strip()

title_text=scraped.title.text.strip()

link_text=scraped.article.h3.a.text


link_text=scraped.article.h3.a['title']


items=scraped.find_all("article",class_="product_pod")

items=scraped.find_all("article",class_="product_pod")

titles=[]
for item in items:
    print(item.h3.a["title"])
    titles.append(item.h3.a['title'])


title_links=scraped.find_all("a",title=True)
for link in title_links:
    print(link["title"])


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

