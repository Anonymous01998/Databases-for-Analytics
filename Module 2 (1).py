#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the packages
import re
#Defining the validateInsert which validates the SQL Insert statements
def validateInsert(val):
    line = val.split()
    line_2 = re.findall("\((.*?)\)", val)
    line_3 = ",".join(line_2)
    if (line[0] == "INSERT") and (line[1] == "INTO") and (line[3] == "VALUES") and (";" in line[-1]):
        return "Inserting (%s) into %s table" % (line_3, line[2])
    else:
        return "Invalid Insert"
#Printing the outputs
print(validateInsert('INSERT INTO Students VALUES (1, Jane, B+);'))
print(validateInsert('INSERT INTO Students VALUES (1, Jane, B+)'))
print(validateInsert('INSERT Students VALUES (1, Jane, B+);'))
print(validateInsert('INSERT INTO Phones VALUES (42, 312-667-1212);'))


# In[ ]:




