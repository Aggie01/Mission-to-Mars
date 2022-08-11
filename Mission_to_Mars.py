#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#set up the HTML parser (10.3.3)
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


#We'll want to assign the title and summary text to variables we'll reference later
slide_elem.find('div', class_='content_title')


# In[6]:


# we are creating a new variable "news_title.  Also, Use the parent element to find the first `a` tag and save it as `news_title`- output will be everything nested within div
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# we need to get just the text, and the extra HTML stuff isn't necessary. Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# we want the full-size version of this image, so we know we'll want Splinter to click the "Full Image" button. From there, the page directs us to a slideshow. It's a little closer to getting the full-size feature image, but we aren't quite there yet.
# 
# This is a lot of clicking to get to the image we want. Let's start getting our code ready to automate all of the clicks.

# In[8]:


# set up the URL.  Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# new variable will hold our f string for better print image. to make the image show up in our browser, Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


#With this line, we're creating a new DataFrame from the HTML table that will show image specifications
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[16]:


# Below code will convert the table above back to HTML format
df.to_html()


# In[17]:


browser.quit()


# In[ ]:




