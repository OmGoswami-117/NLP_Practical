#!/usr/bin/env python
# coding: utf-8

# Prac 2 : Implement N‐gram Language model

# In[1]:


import re


# In[2]:


def N_Grams(text,n): 
    # split sentences into tokens
    tokens=re.split("\\s+",text)
    ngrams=[] 
    # collect the n-grams
    for i in range(len(tokens)-n+1):
         temp=[tokens[j] for j in range(i,i+n)]
         ngrams.append(" ".join(temp)) 
    return ngrams


# In[3]:


text1="The example of Ngram model.";


# In[4]:


N_Grams(text1,1)


# In[5]:


N_Grams(text1,2)


# In[6]:


N_Grams(text1,3)

