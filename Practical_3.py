#!/usr/bin/env python
# coding: utf-8

# Prac3 : Write a program to extract features from text.

# In[5]:


import numpy as np
import re

'''The first function we will implement is to extract the words from a document using regular expressions.
 As we do so, we will be converting all words to lower case and exclude our stop words.'''

def tokenize_sentences(sentences):
    words = []
    for sentence in sentences:
        w = extract_words(sentence)
        words.extend(w)
        
    words = sorted(list(set(words)))
    return words


# In[6]:


'''Next, we implement our tokenize_sentences function. This function builds our vocabulary by looping through
 all our documents (sentences), extracting the words from each, removing duplicates using the set function and 
 returning a sorted list of words.'''

def extract_words(sentence):
    ignore_words = ['a']
    words = re.sub("[^w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned


# In[7]:


def bagofwords(sentence, words):
    sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i,word in enumerate(words):
            if word == sw: 
                bag[i] += 1
                
    return np.array(bag)


# In[10]:


'''Our last function is the implementation of the bag of words model. This function takes an input of a sentence 
and words (our vocabulary). It then extracts the words from the input sentence using the previously defined function. 
It creates a vector of zeros using numpy zeros function with a length of the number of words in our vocabulary.'''


sentences = ["This is example of freature extraction","The method used os bagofwords",
"It is one of the vectorization method"]


# In[11]:


vocabulary = tokenize_sentences(sentences)
bagofwords("Machine learning is great", vocabulary)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000) 

train_data_features = vectorizer.fit_transform(sentences)

vectorizer.transform(["Machine learning is great","Natural Language Processing is a complex field",
"Natural Language Processing is used in machine learning"]).toarray()


# In[ ]:




