#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import textwrap


# In[2]:


OdeOnDictionaries=open('OdeOnDictionaries.txt').read()
TV=open('TV.txt').read()
OdeOnDictionaries=OdeOnDictionaries.replace('\n',' ')
print(OdeOnDictionaries)


# In[3]:


OdeOnDictionaries=OdeOnDictionaries.replace('. ',', ')
OdeOnDictionaries=OdeOnDictionaries.replace('? ',', ')
OdeOnDictionaries=OdeOnDictionaries.replace(' or ',', ')
OdeOnDictionaries=OdeOnDictionaries.replace(' and ',', ')
wordsDic=OdeOnDictionaries.split(", ")
print(wordsDic)


# In[4]:


TV=TV.replace('. ','\n')
TV=TV.replace('? ','\n')
TV=TV.replace('! ','\n')
TV=TV.split("\n")
print(TV)


# In[5]:


connections = ['and','or','None']


# In[12]:


s=0
for i in range(5):
    tv_now=random.choice(TV)
    tv_now_split=tv_now.split()
    num_words=len(tv_now_split)
    l=random.randint(4, min(num_words-1,10))
    if i>0:
        s=random.randint(0, num_words-l-1)
        
        
    if s==0:
        tv_poem=" ".join(tv_now_split[:l])+"..."
        w=tv_poem[-4]
    elif s>0:
        tv_poem="..."+" ".join(tv_now_split[s:s+l])+"..."
        w=tv_poem[-4]
        
    random.shuffle(wordsDic)
    wordsDic_split=[item.split() for item in wordsDic if True]
    dic_poem="..."
    try:
        for i in range(len(wordsDic_split)):
            for j,word in enumerate(wordsDic_split[i]):
                if w==word[0] or w==word[0].lower():
                    wordsDic_split[i][j]=word.upper()
                    dic_poem=" ".join(wordsDic_split[i])
                    raise StopIteration
    except StopIteration:
        pass
    
    ch=random.choice(connections)
    if ch=="None":
        dic_poem+="."
    else:
        if dic_poem[-1]!=".":
            w=dic_poem[-1]
            dic_poem+=", "+ch+" "
            random.shuffle(wordsDic)
            wordsDic_split=[item.split() for item in wordsDic if True]
            try:
                for i in range(len(wordsDic_split)):
                    for j,word in enumerate(wordsDic_split[i]):
                        if w==word[0] or w==word[0].lower():
                            wordsDic_split[i][j]=word.upper()
                            dic_poem+=" ".join(wordsDic_split[i])+"."
                            raise StopIteration
            except StopIteration:
                pass
#         print(addAnother(wordsDic_split))
        
    print('"'+tv_poem+'"')
    print(dic_poem) 
    print(" ")
    print(" ")
    
#     dic_no


# In[ ]:




