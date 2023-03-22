#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Importing the necessary package
import pandas as pd
#Reading the employee.txt file
emp = pd.read_csv("C:/Users/admin/Downloads/Employee.txt",
                   names= ["First Name", "Middle Initial", "Last Name", "ID", "DOB", "Street", "City",
                           "State", "Sex", "Salary", "SSN", "Years of Service"])
#Finding for the female employees
female_employees = emp[emp["Sex"] == "F"]
print("Displaying all female employees")
#Printing all the female employees
print(female_employees)


# In[6]:


#Highest Male Salary
max_male_salary = data[data["Sex"] == "M"]["Salary"].max()
print("Maximum male salary")
print(max_male_salary)


# In[7]:


#Grouping it by middle name
group_by_mid_name = []
for s in data["Salary"].groupby(by= emp["Middle Initial"]):
    group_by_mid_name.append(s)
#Printing the middle name
    print(str(s).replace("Name: Salary, dtype: int64)", "").replace("(", ""))


# In[ ]:




