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


# In[14]:


# Below code will convert the table above back to HTML format
df.to_html()


# In[ ]:


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

### Hemispheres

# 1. Use browser to visit the URL 
#f hemispheres(browser)
#url = 'https://marshemispheres.com/'
#browser.visit(url + 'index.html')
#html = browser.html
#soup = soup(html, 'html.parser')


# 2. Create a list to hold the images and titles.
#hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.
#listImages = soup.find_all('img')

# Loop over listImages elements
#for img in imgs:
    # If img element has an anchor...
 #   if (img.a):
        # And the anchor has non-blank text...
  #      if (img.a.text):
            # Append the img to the list
   #         images.append(img)

#for (image in listImages) 
#imageUrl = image.get("src"); 
#hemisphere_image_urls.append({
#        imageUrl
        
 #   })


#listImages = soup.find_all(".item img") # List of images

#for (image in listImages) {
 #   imageUrl = image.get("src"); # https://google.com
  #  hemisphere_image_urls.append({
   #     imageUrl
        #title
    #})

#tds = soup.find_all('td')

# 4. Print the list that holds the dictionary of each image url and title.
#hemisphere_image_urls

# 5. Quit the browser
#browser.quit()


# In[15]:


def hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemisphere_image_urls = []
    for i in range(4):
        browser.find_by_css("a.product-item img")[i].click()
        hemi_data = scrape_hemisphere(browser.html)
        hemi_data['img_url'] = url + hemi_data['img_url']
        hemisphere_image_urls.append(hemi_data)
        browser.back()
        
    return hemisphere_image_urls
def scrape_hemisphere(html_text):
    hemi_soup = soup(html_text, "html.parser")
    try:
        title_elem = hemi_soup.find("h2", class_="title").get_text()
        sample_elem = hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        title_elem = None
        sample_elem = None
    hemispheres = {
       "title": title_elem,
       "img_url": sample_elem
   }
    return hemispheres 




        
        
    
    


# In[16]:


# 4. Print the list that holds the dictionary of each image url and title.
x=hemispheres(browser)


# In[17]:


# 5. Quit the browser
#browser.quit()
print(x)
        


# In[18]:


browser.quit()


# In[ ]:




