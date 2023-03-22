#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Creating the table
table = """CREATE TABLE IF NOT EXISTS CHAUFFEURS
(
  License_Number NUMBER(6, 0),
  Renewed  VARCHAR2(10),
  Status VARCHAR2(20),
  StatusDate DATE,
  DriverType VARCHAR2(20),
  LicenseType VARCHAR2(20),
  OriginalIssueDate  DATE,
  Fulln_  VARCHAR2(100),
  Sex  VARCHAR2(10),
  ChauffeurCity VARCHAR2(50),
  ChauffeurState VARCHAR2(2),
  RecordNumber VARCHAR2(20),
  
  CONSTRAINT Public_PK
PRIMARY KEY(License_Number)
);"""
#Importing the packages and running them
import csv
import sqlite3
from sqlite3 import IntegrityError
#Reading the csv file 
f_d = open('C:/Users/admin/Downloads/Public_Chauffeurs_Short_hw3.csv', 'r')
reader = csv.reader(f_d)
#Creating an empty list
lst = []
for row in reader:
    lst.append(row)
lst.pop(0)
fd.close()
#Connecting to the SQL database
conn = sqlite3.connect('DSC 450.db')
c = conn.cursor()
c.execute(table_public)
try:
    c.executemany(
        "INSERT INTO Chauffeurs(License_Number, Renewed, Status, StatusDate, DriverType, LicenseType, OriginalIssueDate, Fulln_, Sex, ChauffeurCity, ChauffeurState, RecordNumber) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        lst);
except IntegrityError:
    print("Duplicate key value")
c.execute("SELECT * FROM Chauffeurs")
print(list(c))
conn.commit()
conn.close()


# In[22]:


tab_tweet = """ 
CREATE TABLE Tweets (
    created_at VARCHAR2(50),
    id_str VARCHAR2(50),
    text VARCHAR2(280),
    source VARCHAR2(100),
    in_reply_to_user_id VARCHAR2(50),
    in_reply_to_screen_name VARCHAR2(50),
    retweet_count number,
    contributors VARCHAR2(50),
    
    CONSTRAINT Tweets_PK PRIMARY KEY(id_str)
); """


# In[41]:


import csv
import sqlite3
# Connect to the database
conn = sqlite3.connect("DSC 450.db")
c = conn.cursor()
# Read the CSV file
with open("C:/Users/admin/Desktop/Module5.txt", encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader) # skip the header row
    rows = [row for row in reader]
# Insert the data into the database table
c.executemany("INSERT INTO TWEETS(created_at, id_str, text, source, in_reply_to_user_id, in_reply_to_screen_name, retweet_count, contributors) VALUES (?,?,?,?,?,?,?,?)", rows)
# Commit the changes and close the connection
conn.commit()
conn.close()


# In[ ]:




