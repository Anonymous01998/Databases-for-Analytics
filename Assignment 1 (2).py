#Name - Goutham Selvakumar
#ID - 2092286
#DSC 450 Database Processing for Large Scale Analytics

#defining the numbers
numbers = "5,6,12,56,1"
def function(vals):  #this defines the comma separated numbers and average numbers
    lst = vals.split(",")
    nums = []
    for line in range(0, len(lst)):
        lst[line] = int(lst[line])
        nums.append(lst[line])
#Returning the average and total numbers
    tot = sum(nums)
    avg = tot/len(nums)
    return avg
#printing the average number as the output
output = function(numbers)
print(output)


# In[3]:


#this generated and returns SQL INSERT statement
def generateInsert(x, y):
    line = ",".join(y)
    return "INSERT INTO %s VALUES (%s);" % (x, line)
#Printing the student info and phone info
print(generateInsert('Students', ['3', 'Goutham', 'A']))
print(generateInsert('Consoles', ['15', 'Xbox', 'Playstation', 'Nintendo']))
print(generateInsert('Phone', ['62','312-711-6547']))
print(generateInsert('Phone', ['75','312-721-7332']))


# In[ ]:




