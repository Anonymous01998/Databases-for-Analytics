#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Importing the package
import random
from random import seed
#Setting the seed
seed(1)
#Defining the fn randomgenerator
def randomGenerator(x):
#Creating an empty list
    lst = []
    for i in range(0, x):
        lst.append(random.randint(43, 100))
        i = i+1
    return lst


# In[24]:


#Importing the pandas package
import pandas as pd
#Using the previously used randomGen fn
#Creating an array lst that stores 90 of the rand no's
array = randomGenerator(90)
#Using the Pandas Series in order to find the no's that are lying below 55
ps = pd.Series(array)
ps
#Determining the no < 55
no = ps < 55
print(s[no])
len(ps[no])


# In[8]:


#Importing the numpy package
import numpy as np
#Using the same lst of 90 random no's
#Creating an array and reshaping it into 9x10
array_2 = np.reshape(array, (9, 10))
#Creating an empty lst in which the no's are represented by >= 55
lst_2 = (array_2 >=55)
array_2[lst_2] = 55
array_2


# In[ ]:




