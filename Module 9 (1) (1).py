#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Reading the Module 7
Data = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
#Importing the packages
import json
import urllib
import time
#The URL is opened using the required method
web_FD = urllib.request.urlopen(Data)
line = []
for ln in web_FD:
    line.append(ln.decode("utf-8"))
#Stored to the list 
lst = []
for i in range(0, 10000):
    try:
        obs = json.loads(line[i])
        a = obs['created_at']
        b = obs['id_str']
        c = obs['text']
        d = obs['source']
        e = obs['in_reply_to_user_id']
        f = obs['in_reply_to_screen_name']
        g = obs['in_reply_to_status_id']
        h = obs['retweet_count']
        j = obs['contributors']
        k = obs['id']
        lst.append((k, a, b, c, d, e, f, g, h, j))
        i = i + 1
#The error.txt contains the error that are not parsed to the value error
    except ValueError:
        with open("Error.txt", "wb") as out_file:
            out_file.write(line[i].encode())
end = time.time()
#789 and 987 time is printed
print("time taken to find the tweets the id_str contains “789” or “987” anywhere in column is {} seconds".format(end))


# In[2]:


#Creating the table, table 1 and table 2 that stores the specified variables
table = """
CREATE TABLE Geo
(
  ID    VARCHAR2(40),
  type    VARCHAR2(30),
  longitude    VARCHAR2(50),
  latitude VARCHAR2(50),

  CONSTRAINT Geo_PK
    PRIMARY KEY(ID)
);
"""

table1 = """
CREATE TABLE user_dict
(
  ID    VARCHAR2(50),
  name    VARCHAR2(50),
  screen_name    VARCHAR2(50),
  description VARCHAR2(1000),
  friends_count NUMBER(1000000),

  CONSTRAINT user_dict_PK
    PRIMARY KEY(ID)
);
"""

table2 = """
CREATE TABLE Tweets
(
  GeoID VARCHAR2(50),
  UserID  VARCHAR2(50),
  Created_at VARCHAR2(50),
  id_str    VARCHAR2(50),
  text VARCHAR2(280),
  source VARCHAR2(100),
  in_reply_to_user_id VARCHAR2(50),
  in_reply_to_screen_name VARCHAR2(100),
  in_reply_to_status_id VARCHAR2(50),
  retweet_count  number[10000000],
  Contributors  VARCHAR2(50),

  CONSTRAINT Tweets_PK
    PRIMARY KEY(id_str),

  CONSTRAINT Tweets_FK
      FOREIGN KEY (UserID)
          REFERENCES User_dict(ID),

  CONSTRAINT Geo_PK 
      FOREIGN KEY (GeoID)
          REFERENCES Geo(ID)

);
"""


# In[4]:


#Reading the Module 7
#Importing the packages
Data = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
import sqlite3
import urllib
import datetime
#The SQLite database is connected
conn = sqlite3.connect('DSC__450.db')
c = conn.cursor()
#JSON data text file is opened with the specified URL
web_FD = urllib.request.urlopen(Data)
#The output from the JSON text file is stored in a list
line = []
for ln in web_FD:
    line.append(ln.decode("utf-8"))
#Starting time is recorded
start = datetime.datetime.now()
#in_reply_to_user_id executed a SQL that counts the number
c.execute("SELECT COUNT(DISTINCT in_reply_to_user_id) FROM Tweets")
#Ending time is recorded
end = datetime.datetime.now()
#The total time is calculated
total_time = end-start
#Printing the time that executes the query
print("Time taken", total_time)


# In[5]:


Data = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
#Importing the packages
import urllib
import json
import datetime
import numpy as np
#The decoded lines from the URL are stored inside a list
webFD = urllib.request.urlopen(Data)
line = []
for ln in webFD:
    line.append(ln.decode("utf-8"))
#Two lists are created that stores the values of in_reply_to_user_id
lst1 = []
lst2 = []
#10000 lines are looped and parsed
for i in range(0, 10000):
    try:
        obs = json.loads(line[i])
        e = obs['in_reply_to_user_id']
#The e value is appended to the list that tells if it's whether None or not
        if e is None:
            lst1.append(e)
        else:
            lst2.append(e)
        i = i + 1
    except ValueError:
        with open("Error.txt", "wb") as out_file:
            out_file.write(line[i].encode())
#The starting time is recorded
start = datetime.datetime.now()
#The number of unique values are counted
len(np.unique(lst2))
#Recording the end time
end = datetime.datetime.now()
#The total time is calculated
total_time = end - start
#Unique values in lst2 is printed
print("Time taken ", total_time)


# In[6]:


#Importing the packages that handles the JSON data
import urllib
import json
import matplotlib.pyplot as plt
#Opening the URL that contains the data
Data = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
web_FD = urllib.request.urlopen(Data)
line = []
for ln in web_FD:
    line.append(ln.decode("utf-8"))
#Two empty lists are created in which each stores the length of the tweet and user's screen name
lst_tweet = []
lst_user_name = []
#Loops through 100 lines to parse each line 
#Extracts the tweet text and screen name of their lengths
for i in range(0, 100):
    try:
        obs = json.loads(line[i])
        a = obs['text']
        b = obs['user']['screen_name']
        lst_tweet.append(len(a))
        lst_user_name.append(len(b))
        i = i+1
#If it encounters a valueerror that can be appended into the error.txt file
    except ValueError:
        with open("Error.txt", "wb") as out_file:
            out_file.write(line[i].encode())
#Checking if the length is correct
len(lst_tweet)
len(lst_user_name)
#Plotting the scatter plot 
fig = plt.figure()
sp1 = fig.add_subplot(2,2,2)
sp1.scatter(lst_tweet, lst_user_name)


# In[7]:


#Creating the Table 1
table1 = """
CREATE TABLE user_dict
(
  ID    VARCHAR2(50),
  name    VARCHAR2(50),
  screen_name    VARCHAR2(50),
  description VARCHAR2(1000),
  friends_count NUMBER(1000000),

  CONSTRAINT user_dict_PK
    PRIMARY KEY(ID)
);
"""


# In[8]:


#Creating the Table 2
table2 = """
CREATE TABLE Tweets
(
  GeoID VARCHAR2(50),
  UserID  VARCHAR2(50),
  Created_at VARCHAR2(50),
  id_str    VARCHAR2(50),
  text VARCHAR2(280),
  source VARCHAR2(100),
  in_reply_to_user_id VARCHAR2(50),
  in_reply_to_screen_name VARCHAR2(100),
  in_reply_to_status_id VARCHAR2(50),
  retweet_count  number[10000000],
  Contributors  VARCHAR2(50),

  CONSTRAINT Tweets_PK
    PRIMARY KEY(id_str),

  CONSTRAINT Tweets_FK
      FOREIGN KEY (UserID)
          REFERENCES User_dict(ID),

);
"""


# In[9]:


#Opening the URL that contains the data
Data = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'
#The data is read using the specified URL that gets added to the list
webFD = urllib.request.urlopen(Data)
line = []
for ln in webFD:
    line.append(ln.decode("utf-8"))
lst1 = []
#Loops through 10000 lines
for i in range(0, 10000):
    try:
#Parsed thorugh each line with the specified field
        obs = json.loads(line[i])
        a = obs['created_at']
        b = obs['id_str']
        c = obs['text']
        d = obs['source']
        e = obs['in_reply_to_user_id']
        f = obs['in_reply_to_screen_name']
        g = obs['in_reply_to_status_id']
        h = obs['retweet_count']
        j = obs['contributors']
        k = obs['id']
        lst1.append((k, a, b, c, d, e, f, g, h, j))
        i = i + 1
#If it encounters a valueerror that can be appended into the error.txt file
    except ValueError:
        with open("Error.txt", "wb") as out_file:
            out_file.write(line[i].encode())
#Connects to the SQL database 
conn = sqlite3.connect('DSC__450.db', timeout=30)
c = conn.cursor()
#The data is inserted from lst1 to the tweets
c.executemany(
    "INSERT OR IGNORE INTO Tweets(User_ID, created_at, id_str, text,source, in_reply_to_user_id, in_reply_to_screen_name, in_reply_to_status_id, retweet_count, CONTRIBUTORS) VALUES (?,?,?,?,?,?,?,?,?,?)",
    lst1)
#SELECT* retrieves all the data from the tweets 
c.execute("SELECT * FROM Tweets")


# In[10]:


#Executing the INDEX from the Tweets
c.execute("CREATE INDEX ID_index ON Tweets(id_str);")


# In[11]:


#Creating an empty list (lst2)
lst2 = []
#Loops through the 10000 lines
for i in range(0, 10000):
    try:
#Extracting the info from each line
#ID, Name, Screen_name, description, friends_count
        obs = json.loads(line[i])
        l = obs['user']['id']
        m = obs['user']['name']
        n = obs['user']['screen_name']
        o = obs['user']['description']
        p = obs['user']['friends_count']
        lst2.append((l, m, n, o, p))
        i = i + 1
#If it encounters a valueerror that can be appended into the error.txt file
    except ValueError:
        with open("Error2.txt", "wb") as out_file:
            out_file.write(line[i].encode())


# In[12]:


#Executing The User_Dict
c.execute("CREATE TABLE IF NOT EXISTS User_dict(ID INTEGER PRIMARY KEY, name TEXT, screenName TEXT, Description TEXT, FriendsCnt INTEGER)")


# In[13]:


#Executing the RENAME COLUMN
c.execute("ALTER TABLE User_dict RENAME COLUMN screen_name TO screenName")


# In[19]:


c.execute('''CREATE TABLE IF NOT EXISTS User_dict(
                    ID TEXT PRIMARY KEY,
                    name TEXT,
                    screenName TEXT,
                    Description TEXT,
                    FriendsCnt INTEGER)''')


# In[22]:


c.execute("PRAGMA table_info(User_dict)")
print(c.fetchall())

