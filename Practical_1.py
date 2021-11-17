#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Prac1 : Basic Text Processing operation on text document.


# In[ ]:


get_ipython().system('pip install selenium')


# In[ ]:


from selenium import webdriver
import time
import sys

driver = webdriver.Chrome('F:\ChromeDriver\chromedriver.exe')
driver.get(sys.argv[1])
time.sleep(3)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(sys.argv[2]):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
comment = driver.find_elements_by_class_name('gElp9 ')
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)

user_names.pop(0)
user_comments.pop(0)
import excel_exporter
excel_exporter.export(user_names, user_comments)

driver.close()


# In[12]:


import re
import string
def wordpre(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    print(text)


# In[13]:


wordpre("Hello, welcome home...")

