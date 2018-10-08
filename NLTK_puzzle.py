
# coding: utf-8

# In[1]:


import nltk


# In[2]:


puzzle= nltk.FreqDist('egivrvonl')


# In[3]:


mandate='r'


# In[4]:


word_list=nltk.corpus.words.words()


# In[5]:


word_list


# In[8]:


puz=[w for w in word_list if len(w)>=6 and mandate in w and nltk.FreqDist(w)<puzzle]


# In[9]:


puz

