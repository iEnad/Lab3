#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re


# In[5]:


sentence = 'Regular expression is a sequence of character(s) mainly used to find and replace patterns in a string or file'
start_word='Regular'
end_word='file'


x = re.search("^" +start_word+"*file$", sentence )
if x:
  print("Yes, the string starts with 'Regular'")
else:
  print("No match")


# In[19]:


replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')] 

class RegexReplacer(object):
    def __init__(self, patterns=replacement_patterns): 
        self.patterns = [(re.compile(regex), repl) for (regex, repl)in patterns] 
    def replace(self, text): 
        s = text  
        for (pattern, repl) in self.patterns: 
            (s, count) = re.subn(pattern, repl, s) 
        return s
    
    replacer = RegexReplacer()
text='''We'll see how to replace words using regular expressions such doesn't, can't and so on'''

print(replacer.replace(text))


# In[ ]:





# In[ ]:





# In[ ]:




