#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Opens the directory where animal.txt and reads it
file = open('C:/Users/admin/Downloads/animal.txt', 'r')
animal = file.readlines()
#This will iterate through the animals.txt and checks if the bear word is not in the second element
for x in animal:
    word = x.strip()
#If it cannot the find the bear name it will print the animal name and it's category respectively
    if 'bear' not in word.split(', ')[1]:
        print(word.split(', ')[1], word.split(', ')[2])


# In[24]:


#Opens the directory where animal.txt and reads it
file = open('C:/Users/admin/Downloads/animal.txt', 'r')
animal = file.readlines()
for x in animal:
    word = x.strip()
#Checking to if the animal tiger is present and is only showing animals that are not common
    if 'tiger' in word.split(', ')[1] and word.split(', ')[2] != 'common':
        # Print the animal name if the conditions are met
        print(word.split(', ')[1])


# In[ ]:




