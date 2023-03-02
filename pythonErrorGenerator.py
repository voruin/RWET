#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random
import textwrap


# In[73]:


pictureBook=open('childBook.txt').read()
# pictureBookPara= pictureBook.replace('','.')
pictureBookPara=pictureBook.split('\n')
bookLines=[]
bookSentences=[]
for sentence in pictureBookPara:
#     reSentence= sentence.replace(',','.')
    bookLines.append(sentence.split('.'))

for line in bookLines:
    for shortLine in line:
        if (shortLine!=""):
            bookSentences.append(shortLine.strip())
# print(bookSentences)


# In[68]:


import spacy

nlp = spacy.load('en_core_web_sm')

paragraph = pictureBook

doc = nlp(paragraph)

# Create lists for each type of word
nouns = []
adjectives = []
adverbs = []
verbs = []

for token in doc:
    pos_tag = token.pos_
    if pos_tag == 'NOUN' and token.text.lower() not in nouns:
        nouns.append(token.text)
    elif pos_tag == 'ADJ' and token.text.lower() not in adjectives:
        adjectives.append(token.text)
    elif pos_tag == 'ADV' and token.text.lower() not in adverbs:
        adverbs.append(token.text)
    elif pos_tag == 'VERB' and token.text.lower() not in verbs:
        verbs.append(token.text)

# Print the lists for each type of word
print("Nouns:", nouns)
print("Adjectives:", adjectives)
# print("Adverbs:", adverbs)
print("Verbs:", verbs)


# In[38]:


doSomething=[]
for bookSentence in bookSentences:
    try: 
        for verb in verbs:
            if verb in bookSentence:
                index=bookSentence.find(verb)
                doSomething.append(bookSentence[index:])
                raise StopIteration
    except StopIteration:
        pass

print(doSomething)


# In[46]:


import inflect
p = inflect.engine()

singularNoun=[]

# Singularize the words
for myNoun in nouns:
    if p.singular_noun(myNoun) == False:
        singularNoun.append(myNoun)
    else:
        singularNoun.append(p.singular_noun(myNoun))
print(singularNoun)


# ## Error message format:
# 
# []Error: [Error Message]
# 
# [Description of the error, including any relevant information such as the invalid input value]
# 
# [Optional: Suggestions for resolving the error or troubleshooting steps to take]

# In[5]:


import tracery
from tracery.modifiers import base_english


# In[86]:


errorRules = {
    "CodeMessage": "#errorCode#: #errorMessage#",
    "errorCode": ["#noun.capitalize# Not Found",
                  "500 Internal #noun.capitalize# Error",
                  "#noun.capitalize# Timed Out",
                  "503 #noun.capitalize# Unavailable",
                  "#noun.capitalize# Error",
                  "#noun.capitalize# Denied",
                  "#noun.capitalize# Failed",
                  "Out of #noun.capitalize#",
                  "Unexpected Error",
                  "Bad #noun.capitalize#",
                  "#noun.capitalize# Timeout",
                  "#noun.capitalize# Not Implemented",
                  "#noun.capitalize# Cannot Be Displayed",
                  "Unauthorized #noun.capitalize#",
                  "Unknown #noun.capitalize#",
                  "Invalid #noun.capitalize#",
                  "Unexpected End of #noun.capitalize#",
                  "#noun.capitalize#Error"],
    "errorMessage":["#errorAdj.capitalize# #noun# for #noun# with #noun#",
                    "Expected #noun# does not match actual #noun#",
                    "Unsupported #noun# type(s) for #noun#",
                    "Could not find '#noun#'",
                    "Expected #noun# to be #adj#, but got #adj#.",
                    "#noun# out of range.",
                    "'#noun#' object has no attribute '#noun#'.",
                    "No #noun# named '#noun#'",
                    "No such '#noun#' or '#noun#'"],
    "errorDescription":["The #noun# attempted to #doSth# that does not exist or has #errorAdj.a# #noun#.",
                        "The #noun# attempted to convert #noun.a# to #noun.a#, but the #noun# is not #validAdj.a# #noun#.",
                        "The #noun# attempted to add #noun.a# and #noun.a#, which is not #validAdj.a# operation.",
                        "The #noun# contains #noun.a# error that prevents it from being #adj# or #adj#.",
                        "The #noun# encountered #noun.a# that failed to #doSth#.",
                        "The #noun# has #noun.a# error, which means that the #noun# does not #doSth# correctly.",
                        "The #noun# failed because the expected #noun# did not match the actual #noun#.",
                        "An error occurred in the #noun#, specifically in the #noun# where #noun.a# and #noun.a# #doSth#.",
                        "The #noun# expects #noun.a# and #noun.a# to #doSth#, but not #noun.a#.",
                        "The #noun# cannot process the request due to #errorAdj# #noun# or #errorAdj# #noun#.",
                        "#noun.a.capitalize# or #noun.a# times out while attempting to #doSth#.",
                        "#noun.a.capitalize# or #noun.a# is not yet implemented ot supported.",
                        "The #noun# does not have the necessary permissions or credentials to #doSth#.",
                        "There is a problem with the #noun#, such as #errorAdj# or #errorAdj# #noun#.",
                        "The #noun# couldn't find the #noun# you're looking for. It might #doSth#."],
    "suggestions":["To resolve this error, make sure that the #noun.s# are of the same #noun#, either both #noun.s# or both #noun.s#.",
                   "Double-check the #noun# and ensure that the expected #noun# is #adj#.",
                   "Check the length of the #noun# and make sure that the #noun# is within the #noun#.",
                   "Ensure that the #noun# is #noun.a# or modify the #noun# to #doSth#.",
                   "Check the #noun# and make sure that the #noun# exists in the #noun# and can be accessed from #noun#.",
                   "Update the #noun# and make sure that it is free of #noun#.",
                   "Verify the #noun# and make sure that the #noun# is not #noun#.",
                   "Contact #noun# for further assistance.",
                   "Re#doSth# and try again.",
                   "Clear your #noun# and #noun# and try again.",
                   "Increase the amount of #validAdj# #noun# or #noun#.",
                   "Try using a different #noun# or #noun# to see if the error persists."],
    "errorAdj":["invalid",
                "malformed",
                "slow",
                "missing",
                "incorrect",
                "corrupted", 
                "unauthorized", 
                "incompatible", 
                "unexpected",
                "unknown", 
                "broken", 
                "unavailable", 
                "expired", 
                "forbidden",
                "interrupted", 
                "failed", 
                "unresponsive", 
                "overloaded",
                "unrecognized", 
                "misconfigured"],
    "validAdj":["valid", "available", "correct", "accurate", "reliable",
               "complete", "verified", "functional", "acceptable",
               "suitable", "proper", "adequate", "sufficient",
               "legitimate", "authentic", "appropriate", "approved",
               "accepted", "usable", "accessible", "intact",
               "error-free", "working"],
    "adj":adjectives,
    "noun":singularNoun,
    "doSth":doSomething,
}


# In[72]:


from colorama import Fore, Style
def printOutErrorMessage():
    grammar = tracery.Grammar(errorRules)
    grammar.add_modifiers(base_english)
    print(Fore.RED + '---------------------------------------------------------------------------' + Style.RESET_ALL)
    errorCodeNow=grammar.flatten("#errorCode#")
    print(Fore.RED +errorCodeNow+ Style.RESET_ALL+" "*(42-len(errorCodeNow))+"Traceback (most recent call last)")
    print("Cell " + Fore.GREEN+ "In ["+ str(random.randint(1, 999))+"], line "+str(random.randint(1, 99))+ Style.RESET_ALL)
    print("")
    print(Fore.RED+errorCodeNow+": "+ Style.RESET_ALL+grammar.flatten("#errorMessage#"))
    print(grammar.flatten("#errorDescription#"))
    print(grammar.flatten("#suggestions#"))
    print("")
printOutErrorMessage()    


# In[75]:


printOutErrorMessage()


# In[78]:


printOutErrorMessage() 


# In[80]:


printOutErrorMessage() 


# In[82]:


printOutErrorMessage() 


# In[83]:


printOutErrorMessage() 


# In[84]:


printOutErrorMessage() 


# In[89]:


printOutErrorMessage() 


# In[90]:


printOutErrorMessage() 


# In[91]:


printOutErrorMessage() 


# In[93]:


printOutErrorMessage() 


# In[95]:


printOutErrorMessage() 

