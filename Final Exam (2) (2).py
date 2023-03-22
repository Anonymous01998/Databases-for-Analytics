#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the packages
#Running it
import urllib.request
import pandas as pd
import time
import sqlite3
import matplotlib.pyplot as plt
import json
import collections
import pandas as pd
import re


# In[3]:


#The tweets are downloaded from the web and inserted into a new file 120000tweets.txt
#The 120000 has iterations and using the readlines() the file is downloaded
url = urllib.request.urlopen("http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt")
st = time.time()
counter = 0
for counter in range(120000):  
    txt = url.readline().decode("utf8")
    with open("120000tweets.txt", "a", encoding = "utf-8") as f:
#Using the write() the new file consists of the texts
        f.write(txt) 
#The variable counter is used outside the loop
    counter += 1    
ft = time.time()


# In[4]:


#Printing the time taken for 120000 tweets
print("Time taken to run 120,000 tweets", ft - st)


# In[4]:


#The URL is written into the 600000tweets.txt
#That 600000 loops throught the iteration and using the readline() it is downloaded
#The time fn measures the time taken
st = time.time()
#st = start time
#ft = finish time
counter = 0
#Using the for loop we can insert the range()fn that performs better
for counter in range(600000):
    txt = url.readline().decode("utf8")
    with open("600000tweets.txt", "a", encoding = "utf-8") as f:
        f.write(txt) 
    counter += 1
ft = time.time()
#Prints the time taken for 600000 tweets
#Using '-' operator to separate between finish and start time
print("Time taken to run 600,000 tweets", ft - st)


# In[6]:


#Connecting to the sqlite database 
#For 120000
conn = sqlite3.connect('DSC  450.db')
#Start time
st = time.time()
c = conn.cursor()


# In[6]:


create_table_users = """
CREATE TABLE users(
    id VARCHAR2(38),
    name VARCHAR2(38),
    screen_name VARCHAR2(38),
    description VARCHAR2(38),
    friends_count INTEGER,
    CONSTRAINT id_PK
        PRIMARY KEY (id)
)
"""


# In[7]:


create_table_tweets = """
CREATE TABLE tweets(
    created_at VARCHAR2(38),
    id_str VARCHAR2(38),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR2(38),
    in_reply_to_screen_name VARCHAR2(38),
    in_reply_to_status_id NUMBER(20),
    retweet_count NUMBER(10),
    contributors VARCHAR2(38),
    user_id VARCHAR2(38),
    CONSTRAINT tweets_PK
        PRIMARY KEY (id_str) 
    CONSTRAINT tweets_FK
        FOREIGN KEY (id_str)
            REFERENCES users(id)
);
"""


# In[8]:


create_table_geo_table = """
CREATE TABLE geo_table(
    GeoID VRACHAR2(38),
    longitude NUMBER,
    latitude NUMBER,
    type VARCHAR2(38),
    CONSTRAINT GeoID_PK
        PRIMARY KEY (longitude, latitude)
    CONSTRAINT GeoID_FK
        FOREIGN KEY (GeoID)
            REFERENCES tweets(id_str)    
);
"""


# In[9]:


#Dropping geo_table
c.execute('DROP TABLE IF EXISTS geo_table;')
#Dropping Users
c.execute('DROP TABLE IF EXISTS Users;')
#Dropping Tweets
c.execute('DROP TABLE IF EXISTS tweets;')
#Create users
c.execute(create_table_users)
#Create Tweets
c.execute(create_table_tweets)
#Create geo_table
c.execute(create_table_geo_table)


# In[10]:


#Reading the tweets file and opening it via URL
url = urllib.request.urlopen("http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt")


# In[11]:


#An empty list is created in order to store the JSON parsed objects
tweets = []
#URL file is opened and using the 
#'with' ensures the loop is closed correctly
with url as url:
#Tweet stores the line that is read from the URL
    for i in range(120000):
        tweet = url.readline()
#The JSON text is decoded and added to the tweets list
#The except fn continues in case the decoding fails
        try:
            tweets.append(json.loads(tweet.decode('utf8')))
        except:
            continue
#The JSON objects is parsed through the loop
for feature in tweets:
#These variables from the JSON are assigned respectively
    nam_e = feature["user"]["name"]
    screen_name = feature["user"]["screen_name"]
    description = feature["user"]["description"]
    friends_count = feature["user"]["friends_count"]
    created_at = feature["created_at"]
    id_str = feature["id_str"]
    txt = feature["text"]
    sourc_e = feature["source"]
    reply_user_id = feature["in_reply_to_user_id"]
    reply_screen_name = feature["in_reply_to_screen_name"]
    reply_status_id = feature["in_reply_to_status_id"]
    retweet_count = feature["retweet_count"]
    contributors = feature["contributors"]
    user_id = feature["user"]["id"]
    geo_id = feature["id_str"]
#The id_str is assigned to the JSON object to the geo_id variable
    if feature["geo"] != None:
        longitude = feature["geo"]["coordinates"][1]
        latitude = feature["geo"]["coordinates"][0]
        type = feature["geo"]["type"]
    else:
        longitude = None
        latitude = None
        type = None
#These variables checks whether the geo field is NONE
#In case if it's not it checks the longitude, latitude, and type fields
#That are assigned to the variables that are set to NONE
#Using the INSERT statements that creates the lists that contains the extracted fields
    input_users = [user_id, nam_e, screen_name, description, friends_count]
    input_tweets = [created_at, id_str, txt, sourc_e, reply_user_id, reply_screen_name, 
                    reply_status_id, retweet_count, contributors, user_id]
    input_geo = [geo_id, longitude, latitude, type]
#These will execute the data into the tables
#'INSERT' OR 'IGNORE' removes any data that are unwanted 
#'DELETE' will eliminate the longitude or latitude data from the geo_table
    c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?)", input_users)
    c.execute("INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", input_tweets)
    c.execute("INSERT OR IGNORE INTO geo_table VALUES (?, ?, ?, ?)", input_geo)
    c.execute("DELETE FROM geo_table WHERE longitude IS NULL or latitude is NULL")


# In[12]:


#The SQL query is executed in order to count the number of rows
#Under the 'users' table
c.execute("SELECT count(*) FROM users")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the users table for the 120000 tweets
print("Length of users table for 120,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[13]:


#The SQL query is executed in order to count the number of rows
#Under the 'tweets' table
c.execute("SELECT count(*) FROM tweets")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the tweets table for the 120000 tweets
print("Length of tweets table for 120,0000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[14]:


#The SQL query is executed in order to count the number of rows
#Under the 'geo_table' table
c.execute("SELECT count(*) FROM geo_table")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the geo table for the 120000 tweets
print("Length of geo table table for 120,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
    print(row)


# In[15]:


#Final time is calculated
ft = time.time()
#Printing the final time that takes to run the 120000 tweets
#The '-' gives the difference between final time and start time
print("Time taken to run 120,000 tweets ", ft - st)


# In[32]:


#For 600,000
#Start time 
st = time.time()
#Connects the SQLite database
conn = sqlite3.connect('DSC__450.db') 
c = conn.cursor()


# In[33]:


create_table_users = """
CREATE TABLE users_1(
    id VARCHAR2(38),
    name VARCHAR2(38),
    screen_name VARCHAR2(38),
    description VARCHAR2(38),
    friends_count INTEGER,
    CONSTRAINT id_PK
        PRIMARY KEY (id)
)
"""


# In[34]:


create_table_tweets = """
CREATE TABLE tweets_1(
    created_at VARCHAR2(38),
    id_str VARCHAR2(38),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR2(38),
    in_reply_to_screen_name VARCHAR2(38),
    in_reply_to_status_id NUMBER(20),
    retweet_count NUMBER(10),
    contributors VARCHAR2(38),
    user_id VARCHAR2(38),
    CONSTRAINT tweets_PK
        PRIMARY KEY (id_str)
    CONSTRAINT tweets_FK
        FOREIGN KEY (id_str)
            REFERENCES users(id)
);
"""


# In[35]:


create_table_geo_table = """
CREATE TABLE geo_table_1(
    GeoID VRACHAR2(38),
    longitude NUMBER,
    latitude NUMBER,
    type VARCHAR2(38),
    CONSTRAINT GeoID_PK
        PRIMARY KEY (longitude, latitude)
    CONSTRAINT GeoID_FK
        FOREIGN KEY (GeoID)
            REFERENCES tweets(id_str)    
);
"""


# In[36]:


#Dropping geo_table_1
c.execute('DROP TABLE IF EXISTS geo_table_1;')
#Dropping Users_1
c.execute('DROP TABLE IF EXISTS Users_1;')
#Dropping tweets_1
c.execute('DROP TABLE IF EXISTS tweets_1;')
#Create users table
c.execute(create_table_users)
#Create tweets table
c.execute(create_table_tweets)
#Create geo_table
c.execute(create_table_geo_table)


# In[37]:


#Reading the tweets file using the URL
url = urllib.request.urlopen("http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt")


# In[38]:


#An empty list is created in order to store the JSON parsed objects
tweets = []
#URL file is opened and using the 
#'with' ensures the loop is closed correctly
with url as url:
#Tweet stores the line that is read from the URL
    for i in range(600000):
        tweet = url.readline()
#The JSON text is decoded and added to the tweets list
#The except fn continues in case the decoding fails
        try:
            tweets.append(json.loads(tweet.decode('utf8')))
        except:
            continue
#The JSON objects is parsed through the loop
for feature in tweets:
#These variables from the JSON are assigned respectively
    nam_e = feature["user"]["name"]
    screen_name = feature["user"]["screen_name"]
    description = feature["user"]["description"]
    friends_count = feature["user"]["friends_count"]
    created_at = feature["created_at"]
    id_str = feature["id_str"]
    txt = feature["text"]
    sourc_e = feature["source"]
    reply_user_id = feature["in_reply_to_user_id"]
    reply_screen_name = feature["in_reply_to_screen_name"]
    reply_status_id = feature["in_reply_to_status_id"]
    retweet_count = feature["retweet_count"]
    contributors = feature["contributors"]
    user_id = feature["user"]["id"]
    geo_id = feature["id_str"]
#The id_str is assigned to the JSON object to the geo_id variable
    if feature["geo"] != None:
        longitude = feature["geo"]["coordinates"][1]
        latitude = feature["geo"]["coordinates"][0]
        type = feature["geo"]["type"]
    else:
        longitude = None
        latitude = None
        type = None
#These variables checks whether the geo field is NONE
#In case if it's not it checks the longitude, latitude, and type fields
#That are assigned to the variables that are set to NONE
#Using the INSERT statements that creates the lists that contains the extracted fields
    input_users = [user_id, nam_e, screen_name, description, friends_count]
    input_tweets = [created_at, id_str, txt, sourc_e, reply_user_id, 
                    reply_screen_name, reply_status_id, retweet_count, contributors, user_id]
    input_geo = [geo_id, longitude, latitude, type]
#These will execute the data into the tables
#'INSERT' OR 'IGNORE' removes any data that are unwanted 
#'DELETE' will eliminate the longitude or latitude data from the geo_table
    c.execute("INSERT OR IGNORE INTO users_1 VALUES (?, ?, ?, ?, ?)", input_users)
    c.execute("INSERT OR IGNORE INTO tweets_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", input_tweets)
    c.execute("INSERT OR IGNORE INTO geo_table_1 VALUES (?, ?, ?, ?)", input_geo)
    c.execute("DELETE FROM geo_table_1 WHERE longitude IS NULL or latitude is NULL")


# In[39]:


#The SQL query is executed in order to count the number of rows
#Under the 'users_1' table
c.execute("SELECT count(*) FROM users_1")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the users table for the 600000 tweets
print("Length of users table for  600,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[40]:


#The SQL query is executed in order to count the number of rows
#Under the 'tweets_1' table
c.execute("SELECT count(*) FROM tweets_1")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the tweets table for the 600000 tweets
print("Length of tweets table for 600,0000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[41]:


#The SQL query is executed in order to count the number of rows
#Under the 'geo_table_1' table
c.execute("SELECT count(*) FROM geo_table_1")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the geo table for the 600000 tweets
print("Length of geo table table for 600,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
    print(row)
ft = time.time()


# In[42]:


#This prints the time taken in order to run the 60000 tweets 
#First time and start time is also give
print("Time taken to run 600,000 tweets ", ft - st)


# In[45]:


#Start time is calculated in order to see the runtime of the script
st = time.time()
#An empty list is created in order to store the tweets
#The tweets are stored in an empty list
tweets = []
##The file 120000tweets.txt is opened using the UTF-8
with open("C:/Users/admin/Downloads/120000tweets.txt", "r", encoding = "utf8") as file:
#Iterates through each line
    for tweet in file:
#Each line is loaded as the JSON object and added to the 'tweets' list
#The continue is used to skip the script to the next line
        try:
            tweets.append(json.loads(tweet))
        except:
            continue
#Conencts to the SQLite database
conn = sqlite3.connect('DSC   450.db') 
c = conn.cursor()
#Drop users table
c.execute('DROP TABLE IF EXISTS users;')
#Drop tweets table
c.execute('DROP TABLE IF EXISTS tweets;')
#Drop geo_table table
c.execute('DROP TABLE IF EXISTS geo_table;')


# In[46]:


create_table_users = """
CREATE TABLE users(
    id VARCHAR2(38),
    name VARCHAR2(38),
    screen_name VARCHAR2(38),
    description VARCHAR2(38),
    friends_count INTEGER,
    CONSTRAINT id_PK
        PRIMARY KEY (id)
)
"""


# In[47]:


create_table_tweets = """
CREATE TABLE tweets(
    created_at VARCHAR2(38),
    id_str VARCHAR2(38),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR2(38),
    in_reply_to_screen_name VARCHAR2(38),
    in_reply_to_status_id NUMBER(20),
    retweet_count NUMBER(10),
    contributors VARCHAR2(38),
    user_id VARCHAR2(38),
    
    CONSTRAINT tweets_PK
        PRIMARY KEY (id_str)
        
    CONSTRAINT tweets_FK
        FOREIGN KEY (id_str)
            REFERENCES users(id)
);
"""


# In[48]:


create_table_geo_table = """
CREATE TABLE geo_table(
    GeoID VRACHAR2(38),
    longitude NUMBER,
    latitude NUMBER,
    type VARCHAR2(38),
    
    CONSTRAINT GeoID_PK
        PRIMARY KEY (longitude, latitude)
        
    CONSTRAINT GeoID_FK
        FOREIGN KEY (GeoID)
            REFERENCES tweets(id_str)    
);
"""


# In[49]:


#Executing the users table
c.execute(create_table_users)
#Executing the tweets table
c.execute(create_table_tweets)
#Executing the geo_table 
c.execute(create_table_geo_table)
#The JSON objects is parsed through the loop
for feature in tweets:
#These variables from the JSON are assigned respectively
    nam_e = feature["user"]["name"]
    screen_name = feature["user"]["screen_name"]
    description = feature["user"]["description"]
    friends_count = feature["user"]["friends_count"]
    created_at = feature["created_at"]
    id_str = feature["id_str"]
    txt = feature["text"]
    sourc_e = feature["source"]
    reply_user_id = feature["in_reply_to_user_id"]
    reply_screen_name = feature["in_reply_to_screen_name"]
    reply_status_id = feature["in_reply_to_status_id"]
    retweet_count = feature["retweet_count"]
    contributors = feature["contributors"]
    user_id = feature["user"]["id"]
    geo_id = feature["id_str"]
#The id_str is assigned to the JSON object to the geo_id variable
    if feature["geo"] != None:
        longitude = feature["geo"]["coordinates"][1]
        latitude = feature["geo"]["coordinates"][0]
        type = feature["geo"]["type"]
    else:
        longitude = None
        latitude = None
        type = None
#These variables checks whether the geo field is NONE
#In case if it's not it checks the longitude, latitude, and type fields
#That are assigned to the variables that are set to NONE
#Using the INSERT statements that creates the lists that contains the extracted fields
    input_users = [user_id, nam_e, screen_name, description, friends_count]
    input_tweets = [created_at, id_str, txt, sourc_e, reply_user_id, reply_screen_name,
                    reply_status_id, retweet_count, contributors, user_id]
    input_geo = [geo_id, longitude, latitude, type]
#These will execute the data into the tables
#'INSERT' OR 'IGNORE' removes any data that are unwanted 
#'DELETE' will eliminate the longitude or latitude data from the geo_table
    c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?)", input_users)
    c.execute("INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", input_tweets)
    c.execute("INSERT OR IGNORE INTO geo_table VALUES (?, ?, ?, ?)", input_geo)
    c.execute("DELETE FROM geo_table WHERE longitude IS NULL or latitude is NULL")


# In[50]:


#The SQL query is executed in order to count the number of rows
#Under the 'users' table
c.execute("SELECT count(*) FROM users")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the users table for the 120000 tweets
print("Length of users table for 120,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[51]:


#The SQL query is executed in order to count the number of rows
#Under the 'tweets' table
c.execute("SELECT count(*) FROM tweets")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the tweets table for the 120000 tweets
print("Length of tweets table for 120,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[52]:


#The SQL query is executed in order to count the number of rows
#Under the 'geo_table' table
c.execute("SELECT count(*) FROM geo_table")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the geo table for the 120000 tweets
print("Length of geo table table for 120,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
    print(row)
ft = time.time()
#Time taken to run the 120000 tweets 
#Final time and start time is given
print("Time taken to run 120,000 tweets", ft - st)


# In[5]:


#Start time is calculated in order to see the runtime of the script
st = time.time()
#An empty list is created in order to store the tweets
#The tweets are stored in an empty list
tweets = []
#The file 600000tweets.txt is opened using the UTF-8
with open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding = "utf8") as file:
    for tweet in file:
#Each line is loaded as the JSON object and added to the 'tweets' list
#The continue is used to skip the script to the next line
        try:
            tweets.append(json.loads(tweet))
        except:
            continue
#Conencts to the SQLite database
conn = sqlite3.connect('DSC   450.db') 
c = conn.cursor()
#Drop users_1 table
c.execute('DROP TABLE IF EXISTS Users_1;')
#Drop tweets_1 table
c.execute('DROP TABLE IF EXISTS tweets_1;')
#Drop geo_table_1 table
c.execute('DROP TABLE IF EXISTS geo_table_1;')


# In[6]:


create_table_users = """
CREATE TABLE users_1(
    id VARCHAR2(38),
    name VARCHAR2(38),
    screen_name VARCHAR2(38),
    description VARCHAR2(38),
    friends_count INTEGER,
    CONSTRAINT id_PK
        PRIMARY KEY (id)
)
"""


# In[7]:


create_table_tweets = """
CREATE TABLE tweets_1(
    created_at VARCHAR2(38),
    id_str VARCHAR2(38),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR2(38),
    in_reply_to_screen_name VARCHAR2(38),
    in_reply_to_status_id NUMBER(20),
    retweet_count NUMBER(10),
    contributors VARCHAR2(38),
    user_id VARCHAR2(38),
    CONSTRAINT tweets_PK
        PRIMARY KEY (id_str) 
    CONSTRAINT tweets_FK
        FOREIGN KEY (id_str)
            REFERENCES users(id)
);
"""


# In[8]:


create_table_geo_table = """
CREATE TABLE geo_table_1(
    GeoID VRACHAR2(38),
    longitude NUMBER,
    latitude NUMBER,
    type VARCHAR2(38),
    CONSTRAINT GeoID_PK
        PRIMARY KEY (longitude, latitude)
    CONSTRAINT GeoID_FK
        FOREIGN KEY (GeoID)
            REFERENCES tweets(id_str)    
);
"""


# In[9]:


#Executes users table
c.execute(create_table_users)
#Executes tweets table
c.execute(create_table_tweets)
#Executes geo_table
c.execute(create_table_geo_table)
for feature in tweets:
#These variables from the JSON are assigned respectively
    nam_e = feature["user"]["name"]
    screen_name = feature["user"]["screen_name"]
    description = feature["user"]["description"]
    friends_count = feature["user"]["friends_count"]
    created_at = feature["created_at"]
    id_str = feature["id_str"]
    txt = feature["text"]
    sourc_e = feature["source"]
    reply_user_id = feature["in_reply_to_user_id"]
    reply_screen_name = feature["in_reply_to_screen_name"]
    reply_status_id = feature["in_reply_to_status_id"]
    retweet_count = feature["retweet_count"]
    contributors = feature["contributors"]
    user_id = feature["user"]["id"]
    geo_id = feature["id_str"]
#The id_str is assigned to the JSON object to the geo_id variable
    if feature["geo"] != None:
        longitude = feature["geo"]["coordinates"][1]
        latitude = feature["geo"]["coordinates"][0]
        type = feature["geo"]["type"]
    else:
        longitude = None
        latitude = None
        type = None
#These variables checks whether the geo field is NONE
#In case if it's not it checks the longitude, latitude, and type fields
#That are assigned to the variables that are set to NONE
#Using the INSERT statements that creates the lists that contains the extracted fields
    input_users = [user_id, nam_e, screen_name, description, friends_count]
    input_tweets = [created_at, id_str, txt, sourc_e, reply_user_id, reply_screen_name, 
                    reply_status_id, retweet_count, contributors, user_id]
    input_geo = [geo_id, longitude, latitude, type]
#These will execute the data into the tables
#'INSERT' OR 'IGNORE' removes any data that are unwanted 
#'DELETE' will eliminate the longitude or latitude data from the geo_table
    c.execute("INSERT OR IGNORE INTO users_1 VALUES (?, ?, ?, ?, ?)", input_users)
    c.execute("INSERT OR IGNORE INTO tweets_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", input_tweets)
    c.execute("INSERT OR IGNORE INTO geo_table_1 VALUES (?, ?, ?, ?)", input_geo)
    c.execute("DELETE FROM geo_table_1 WHERE longitude IS NULL or latitude is NULL")


# In[10]:


#The SQL query is executed in order to count the number of rows
#Under the 'users_1' table
c.execute("SELECT count(*) FROM users_1")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the users table for the 600000 tweets
print("Length of users table for 600,000 tweets")
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[11]:


#The SQL query is executed in order to count the number of rows
#Under the 'tweets_1' table
c.execute("SELECT count(*) FROM tweets_1")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the tweets table for the 600000 tweets
print("Length of tweets table for 600,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
#Prints the number of rows in the users table
    print(row)


# In[12]:


#The SQL query is executed in order to count the number of rows
#Under the 'geo_table_1' table
c.execute("SELECT count(*) FROM geo_table_1")
#The first row from the set is fetched and returned that will be assigned to the variable
rows = c.fetchone()
#Prints the length of the geo table for the 600000 tweets
print("length of geo table table for 600,000 tweets")
#A loop is started where the rows are selected and returned that will be executed once
for row in rows:
    print(row)


# In[13]:


#Time taken to run the 600000 tweets 
#Final time and start time is given
ft = time.time()
print("Time taken to run part for 600,000 tweets", ft - st)


# In[16]:


#Start time is calculated in order to see the runtime of the script
st = time.time()
#An empty list is created in order to store the tweets
#The tweets are stored in an empty list
tweets = []
#The file 120000tweets.txt is opened using the UTF-8
with open("C:/Users/admin/Downloads/120000tweets.txt", "r", encoding = "utf8") as file:
    for tweet in file:
#Each line is loaded as the JSON object and added to the 'tweets' list
#The continue is used to skip the script to the next line
        try:
            tweets.append(json.loads(tweet))
        except:
            pass
#Conencts to the SQLite database
conn = sqlite3.connect('DSC__450.db') 
c = conn.cursor()
#Drop users table
c.execute('DROP TABLE IF EXISTS Users;')
#Drop tweets table
c.execute('DROP TABLE IF EXISTS tweets;')
#Drop geo_table table
c.execute('DROP TABLE IF EXISTS geo_table;')


# In[17]:


create_table_users = """
CREATE TABLE users(
    id VARCHAR2(38),
    name VARCHAR2(38),
    screen_name VARCHAR2(38),
    description VARCHAR2(38),
    friends_count INTEGER,
    
    CONSTRAINT id_PK
        PRIMARY KEY (id)
)
"""


# In[18]:


create_table_tweets = """
CREATE TABLE tweets(
    created_at VARCHAR2(38),
    id_str VARCHAR2(38),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR2(38),
    in_reply_to_screen_name VARCHAR2(38),
    in_reply_to_status_id NUMBER(20),
    retweet_count NUMBER(10),
    contributors VARCHAR2(38),
    user_id VARCHAR2(38),
    
    CONSTRAINT tweets_PK
        PRIMARY KEY (id_str)
        
    CONSTRAINT tweets_FK
        FOREIGN KEY (id_str)
            REFERENCES users(id)
);
"""


# In[19]:


create_table_geo_table = """
CREATE TABLE geo_table(
    GeoID VRACHAR2(38),
    longitude NUMBER,
    latitude NUMBER,
    type VARCHAR2(38),
    
    CONSTRAINT GeoID_PK
        PRIMARY KEY (longitude, latitude)
        
    CONSTRAINT GeoID_FK
        FOREIGN KEY (GeoID)
            REFERENCES tweets(id_str)    
);
"""


# In[20]:


#Executes users
c.execute(create_table_users)
#Executes tweets
c.execute(create_table_tweets)
#Executes geo_table
c.execute(create_table_geo_table)
#start, stop, and counter represents the variables that are in the iteration
start = 0
stop = 6000
counter = 0
#Less than 200 variables
while counter < 200:
#Three empty lists that stores the data
    input_users = []
    input_tweets = []
    input_geo = []
#Iterates through each of the element
    for feature in tweets:
#Stored in different names from features to tweets
        counter += 1
        nam_e = feature["user"]["name"]
        screen_name = feature["user"]["screen_name"]
        description = feature["user"]["description"]
        friends_count = feature["user"]["friends_count"]
        created_at = feature["created_at"]
        id_str = feature["id_str"]
        txt = feature["text"]
        sourc_e = feature["source"]
        reply_user_id = feature["in_reply_to_user_id"]
        reply_screen_name = feature["in_reply_to_screen_name"]
        reply_status_id = feature["in_reply_to_status_id"]
        retweet_count = feature["retweet_count"]
        contributors = feature["contributors"]
        user_id = feature["user"]["id"]
        geo_id = feature["id_str"]
#The feature's gegographic info are taken
#If exists stored in longitude, latitude, and type variables and returns NONE if there is nothing
        if feature["geo"] != None:
            longitude = feature["geo"]["coordinates"][1]
            latitude = feature["geo"]["coordinates"][0]
            type = feature["geo"]["type"]
        else:
            longitude = None
            latitude = None
            type = None
#The feature gets the info 
        input_users.append([user_id, nam_e, screen_name, description, friends_count])
        input_tweets.append([created_at, id_str, txt, sourc_e, reply_user_id, 
                             reply_screen_name, reply_status_id, retweet_count, contributors, user_id])
        input_geo.append([geo_id, longitude, latitude, type])
#Executes data that through the SQL queries
#Executemany inserts multiple rows at the same time
        c.executemany("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?)", input_users)
        c.executemany("INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", input_tweets)
        c.executemany("INSERT OR IGNORE INTO geo_table VALUES (?, ?, ?, ?)", input_geo)
#If it's lesser than 100, incremented by 6000 tweets 
        if counter < 100:
            start += 6000
            stop += 6000
#Again three empty lists are created
        input_users = []
        input_geo = []
        input_tweets = []


# In[21]:


#the time is assigned to the final time (ft) variable
ft = time.time()
#Prints the time taken for 120000 tweets in order to run with the 6000 batch
print("Time taken to run 120,000 tweets with 6000 batch", ft - st)
#Delete the rows that have NULL values present in the following table
c.execute("DELETE FROM geo_table WHERE longitude IS NULL or latitude is NULL or GeoID is NULL or type is NULL")
#Fetches the users and counts the no of rows 
#Results in string
c.execute("SELECT count(*) FROM users")
rows = c.fetchone()
print("Length of users table with 120,000 tweets")
for row in rows:
    print(row)
#Selects the no of tweets 
#Result in string
c.execute("SELECT count(*) FROM tweets")
rows = c.fetchone()
print("Length of tweets table with 120,000 tweets")
for row in rows:
    print(row)
#Selects the no of rows in geo_table
#Result in string
c.execute("SELECT count(*) FROM geo_table")
rows = c.fetchone()
print("Length of geo table table with 120,000 tweets")
for row in rows:
    print(row)


# In[22]:


#the time module gives the current time that is stored in the start time (st) variable
st = time.time()
#An empty list is created
tweets = []
#Opening the 600000 tweets file 
with open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding = "utf8") as file:
    for tweet in file:
        try:
            tweets.append(json.loads(tweet))
        except:
            pass


# In[23]:


#Connecting to the SQLite database
conn = sqlite3.connect('DSC___450.db') 
#Executes the SQL
c = conn.cursor()
#Dropping the necessary tables from the database if they exists
c.execute('DROP TABLE IF EXISTS Users_1;')
c.execute('DROP TABLE IF EXISTS tweets_1;')
c.execute('DROP TABLE IF EXISTS geo_table_1;')


# In[24]:


create_table_users = """
CREATE TABLE users_1(
    id VARCHAR2(38),
    name VARCHAR2(38),
    screen_name VARCHAR2(38),
    description VARCHAR2(38),
    friends_count INTEGER,
    CONSTRAINT id_PK
        PRIMARY KEY (id)
)
"""


# In[25]:


create_table_tweets = """
CREATE TABLE tweets_1(
    created_at VARCHAR2(38),
    id_str VARCHAR2(38),
    text VARCHAR(140),
    source VARCHAR(60),
    in_reply_to_user_id VARCHAR2(38),
    in_reply_to_screen_name VARCHAR2(38),
    in_reply_to_status_id NUMBER(20),
    retweet_count NUMBER(10),
    contributors VARCHAR2(38),
    user_id VARCHAR2(38),
    CONSTRAINT tweets_PK
        PRIMARY KEY (id_str)   
    CONSTRAINT tweets_FK
        FOREIGN KEY (id_str)
            REFERENCES users(id)
);
"""


# In[26]:


create_table_geo_table = """
CREATE TABLE geo_table_1(
    GeoID VRACHAR2(38),
    longitude NUMBER,
    latitude NUMBER,
    type VARCHAR2(38),
    CONSTRAINT GeoID_PK
        PRIMARY KEY (longitude, latitude)   
    CONSTRAINT GeoID_FK
        FOREIGN KEY (GeoID)
            REFERENCES tweets(id_str)    
);
"""


# In[27]:


#Executes users
c.execute(create_table_users)
#Executes tweets
c.execute(create_table_tweets)
#Executes geo_table
c.execute(create_table_geo_table)
#start, stop, and counter represents the variables that are in the iteration
start = 0
stop = 6000
counter = 0
#Less than 200 variables
while counter < 200:
#Three empty lists that stores the data
    input_users = []
    input_tweets = []
    input_geo = []
#Iterates through each of the element
    for feature in tweets:
#Stored in different names from features to tweets
        counter += 1
        nam_e = feature["user"]["name"]
        screen_name = feature["user"]["screen_name"]
        description = feature["user"]["description"]
        friends_count = feature["user"]["friends_count"]
        created_at = feature["created_at"]
        id_str = feature["id_str"]
        txt = feature["text"]
        sourc_e = feature["source"]
        reply_user_id = feature["in_reply_to_user_id"]
        reply_screen_name = feature["in_reply_to_screen_name"]
        reply_status_id = feature["in_reply_to_status_id"]
        retweet_count = feature["retweet_count"]
        contributors = feature["contributors"]
        user_id = feature["user"]["id"]
        geo_id = feature["id_str"]
#The feature's gegographic info are taken
#If exists stored in longitude, latitude, and type variables and returns NONE if there is nothing
        if feature["geo"] != None:
            longitude = feature["geo"]["coordinates"][1]
            latitude = feature["geo"]["coordinates"][0]
            type = feature["geo"]["type"]
        else:
            longitude = None
            latitude = None
            type = None
#The feature gets the info 
        input_users.append([user_id, nam_e, screen_name, description, friends_count])
        input_tweets.append([created_at, id_str, txt, sourc_e, reply_user_id, reply_screen_name, reply_status_id, retweet_count, contributors, user_id])
        input_geo.append([geo_id, longitude, latitude, type])
#Executes data that through the SQL queries
#Executemany inserts multiple rows at the same time
        c.executemany("INSERT OR IGNORE INTO users_1 VALUES (?, ?, ?, ?, ?)", input_users)
        c.executemany("INSERT OR IGNORE INTO tweets_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)", input_tweets)
        c.executemany("INSERT OR IGNORE INTO geo_table_1 VALUES (?, ?, ?, ?)", input_geo)
        if counter < 200:
#If it's lesser than 100, incremented by 6000 tweets 
            start += 6000
            stop += 6000
#Again three empty lists are created
        input_users = []
        input_geo = []
        input_tweets = []


# In[28]:


#the time is assigned to the final time (ft) variable
ft = time.time()
#Prints the time taken for 600000 tweets in order to run with the 6000 batch
print("Time taken to complete 600,000 tweets with 6000 batch ", ft - st)
#Delete the rows that have NULL values present in the following table
c.execute("DELETE FROM geo_table_1 WHERE longitude IS NULL or latitude is NULL or GeoID is NULL or type is NULL")
#Fetches the users and counts the no of rows 
#Results in string
c.execute("SELECT count(*) FROM users_1")
rows = c.fetchone()
print("Length of users table with 600,000 tweets")
for row in rows:
    print(row)
#Selects the no of tweets 
#Result in string
c.execute("SELECT count(*) FROM tweets_1")
rows = c.fetchone()
print("Length of tweets table with 600,000 tweets")
for row in rows:
    print(row)
#Selects the no of rows in geo_table
#Result in string
c.execute("SELECT count(*) FROM geo_table_1")
rows = c.fetchone()
print("Length of geo table table with 600,000 tweets")
for row in rows:
    print(row) 


# In[29]:


#Plotting the two tweets of 120000 and 600000 respectively
#with their total time taken
plt.scatter([120000, 600000], [23.1,121.9])
#Xlabel
plt.xlabel("No of tweets")
#YLabel
plt.ylabel("Time Elapsed")
#Title
plt.title('A PLOT')
plt.show()


# In[30]:


#Plotting the two tweets of 120000 and 600000 respectively
#with their total time taken
plt.scatter([120000, 600000], [93.0, 470.6])
#Xlabel
plt.xlabel("Number of tweets")
#YLabel
plt.ylabel("Time Elapsed")
#Title
plt.title('B Plot')
plt.show()


# In[31]:


#Plotting the two tweets of 120000 and 600000 respectively
#with their total time taken
plt.scatter([120000, 600000], [100.7, 585.0])
#Xlabel
plt.xlabel("Number of tweets")
#YLabel
plt.ylabel("Time Elapsed")
#Title
plt.title('C Plot')
plt.show()


# In[32]:


#Plotting the two tweets of 120000 and 600000 respectively
#with their total time taken
plt.scatter([120000, 600000], [1286.7, 346.4])
#Xlabel
plt.xlabel("Number of tweets")
#YLabel
plt.ylabel("Time Elapsed")
#Title
plt.title('D Plot ')
plt.show()


# In[7]:


#The current time that calculated is stored in the varibale start time(st) 
st = time.time()
#Executes the SQL query using the cursor
#They are joined and grouped by user_id
c.execute("SELECT tw.user_id,avg(gt.longitude),avg(gt.latitude) from geo_table gt,tweets tw on tw.id_str=gt.GeoID group by tw.user_id  ;")
#Fetches all the rows
rows = c.fetchall()
ft = time.time()
#Finish time and the start time is printed
print("Time taken to run ", ft - st)


# In[8]:


#The current time that calculated is stored in the varibale start time(st) 
st = time.time()
#The query is executed 5 times and their respective ID are selected
#using the id_str the tables are joined
for i in range(5):
    c.execute("SELECT tw.user_id,avg(gt.longitude),avg(gt.latitude)  from geo_table gt,tweets tw on tw.id_str=gt.GeoID group by tw.user_id  ;")
#Fetchall() method fetches the results 
rows = c.fetchall()
#Final time
ft = time.time()
#Prints the query 5 times and it's time taken to execute it
print("Time taken to run 5 times", ft - st)
st = time.time()
#The query is executed 20 times and their respective ID are selected
for i in range(20):
    c.execute("SELECT tw.user_id,avg(gt.longitude),avg(gt.latitude)  from geo_table gt,tweets tw on tw.id_str=gt.GeoID group by tw.user_id  ;")
rows = c.fetchall()
ft = time.time()
#Prints the query 20 times and it's time taken to execute it
print("Time taken to run 20 times ", ft - st)


# In[9]:


#start time (st) stores the current time 
st = time.time()
#Opens the 600000tweets.txt and reads it
file = (open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding = "utf8")).readlines()
#An empty dictionary is created that stires the longitude and latitude
#For each ID
test_dict = {}
#Iterates through all the lines
for i in file:
#JSON obj is loaded and assigned to the variable 'tw' 
    tw =json.loads(i)
#Checks if the geo is in tw
    if tw['geo'] != None: 
        id=str(tw['user']['id'])
        if id not in test_dict: 
#Adds the longitude and latitude values and the count is given
            test_dict[id]=[tw['geo']['coordinates'][1]]
            test_dict[id].append(tw['geo']['coordinates'][0])
            test_dict[id].append(1)
        else:                                       
            list_trial=[]
            test_dict[id][0]= list_trial.append(tw['geo']['coordinates'][1]) 
            test_dict[id][1]= list_trial.append(tw['geo']['coordinates'][0]) 
            res = 0
#Calculates the average value of longitude and latitude
            for val in list_trial:                  
                  res += val
            res = res / len(list_trial)  
ft = time.time()
#Prints the time taken in order to run from the final time and start time
print("Time taken to run", ft - st)


# In[10]:


#start time (st) stores the current time 
st = time.time()
#Opens the 600000tweets.txt and reads it
file = (open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding = "utf8")).readlines()
#Using the range of 5 and iteration is done
for i in range(5):
#An empty dictionary is created that stires the longitude and latitude
#For each ID
 test_dict = {}
 for i in file:
#JSON obj is loaded and assigned to the variable 'tw' 
    tw =json.loads(i)
#Checks if the geo is in tw
    if tw['geo'] != None: 
        id=str(tw['user']['id'])
        if id not in test_dict: 
#Adds the longitude and latitude values and the count is given
            test_dict[id]=[tw['geo']['coordinates'][1]]
            test_dict[id].append(tw['geo']['coordinates'][0])
            test_dict[id].append(1)
        else:                                  
            list_trial=[]
            test_dict[id][0]= list_trial.append(tw['geo']['coordinates'][1]) 
            test_dict[id][1]= list_trial.append(tw['geo']['coordinates'][0]) 
            res = 0
#Calculates the average value of longitude and latitude
            for val in list_trial:                  
                  res += val
            res = res / len(list_trial)
ft = time.time()
#Prints the time taken for the query to be executed 5 times
print("Time taken to run 5 times", ft - st)
#start time (st) stores the current time 
st = time.time()
#Using the range of 20 and iteration is done
for i in range(20):
#An empty dictionary is created that stires the longitude and latitude
#For each ID
 test_dict = {}
 for i in file:
#JSON obj is loaded and assigned to the variable 'tw' 
    tw =json.loads(i)
#Checks if the geo is in tw
    if tw['geo'] != None: 
        id=str(tw['user']['id'])
        if id not in test_dict: 
#Adds the longitude and latitude values and the count is given
            test_dict[id]=[tw['geo']['coordinates'][1]]
            test_dict[id].append(tw['geo']['coordinates'][0])
            test_dict[id].append(1)
        else:                                      
            list_trial=[]
            test_dict[id][0]= list_trial.append(tw['geo']['coordinates'][1]) 
            test_dict[id][1]= list_trial.append(tw['geo']['coordinates'][0]) 
            res = 0
#Calculates the average value of longitude and latitude
            for val in list_trial:                
                  res += val
            res = res / len(list_trial)   
ft = time.time()
#Time taken for it to execute the query 20 times
#Final time and start time
print("Time taken to run 20 times", ft - st)


# In[20]:


#The required time is stored in the st (start time) variable
st = time.time()
#The regular expressions for user and geo is compiled
u_regex = re.compile(r'"user":{"id":(\d+)')
g_regex = re.compile(r'"geo":{.*?"coordinates":\[(.*?), (.*?)\]}')
#Opening the 600000tweets.txt file and reading
with open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding="utf8") as file:
#An empty list is created where the User ID's location is stored
    te_dict = {}
#The file is iterated
    for line in file:
        try:
            u_id_match = user_regex.search(line)
            g_match = geo_regex.search(line)
#The longitude and latitude values are added when both of it matches
            if u_id_match and g_match:
                u_id = u_id_match.group(1)
                lat = g_match.group(1).strip()
                long = g_match.group(2).strip()
                if user_id not in test_dict:
                    te_dict[u_id] = [float(lat), float(long), 1]
                else:
                    te_dict[u_id][0] += float(lat)
                    te_dict[u_id][1] += float(long)
                    te_dict[u_id][2] += 1
        except:
            continue
#Avg of the longitude and latitude is calculated
for u_id in te_dict:
    lat_sum, long_sum, count = te_dict[u_id]
    lat_avg = lat_sum / count
    long_avg = long_sum / count
    print(f"User ID: {user_id}, Latitude: {lat_avg}, Longitude: {long_avg}")
#Final time is stored 
ft = time.time()
#Printing the time taken to run
print("Time taken to run", ft - st)


# In[30]:


#The regular expressions for user and geo is compiled
u_regex = re.compile(r'"user":{"id":(\d+)')
g_regex = re.compile(r'"geo":{.*?"coordinates":\[(.*?), (.*?)\]}')
#Opening the 600000tweets.txt file and reading
with open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding="utf8") as file:
#The file is iterated
    for line in file:
#Running the Query for 5 times
        for i in range(5):
#The required time is stored in the st (start time) variable
            st = time.time()
#An empty list is created where the User ID's location is stored
            te_dict = {}
#Opening the 600000tweets.txt file and reading
    with open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding="utf8") as file:
#The file is iterated
        for line in file:
            try:
                u_id_match = user_regex.search(line)
                g_match = geo_regex.search(line)
#The longitude and latitude values are added when both of it matches
                if u_id_match and g_match:
                    u_id = u_id_match.group(1)
                    lat = g_match.group(1).strip()
                    long = g_match.group(2).strip()
                    if user_id not in test_dict:
                        te_dict[u_id] = [float(lat), float(long), 1]
                    else:
                        te_dict[u_id][0] += float(lat)
                        te_dict[u_id][1] += float(long)
                        te_dict[u_id][2] += 1
            except:
                pass
#Avg of the longitude and latitude is calculated
    for u_id in te_dict:
        lat_sum, long_sum, count = te_dict[u_id]
        lat_avg = lat_sum / count
        long_avg = long_sum / count
        te_dict[u_id] = [lat_avg, long_avg]
#Final time is stored 
    ft = time.time()
#Printing the time taken to run for 5 times
    print("Time taken to run 5 times: ", ft - st)
#Running the query for 20 times
for i in range(20):
#The required time is stored in the st (start time) variable
    st = time.time()
#An empty list is created where the User ID's location is stored
    te_dict = {}
#Opening the 600000tweets.txt file and reading
    with open("C:/Users/admin/Downloads/600000tweets.txt", "r", encoding="utf8") as file:
#The file is iterated
        for line in file:
            try:
                u_id_match = user_regex.search(line)
                g_match = geo_regex.search(line)
#The longitude and latitude values are added when both of it matches
                if u_id_match and g_match:
                    u_id = u_id_match.group(1)
                    lat = g_match.group(1).strip()
                    long = g_match.group(2).strip()
                    if user_id not in test_dict:
                        te_dict[u_id] = [float(lat), float(long), 1]
                    else:
                        te_dict[u_id][0] += float(lat)
                        te_dict[u_id][1] += float(long)
                        te_dict[u_id][2] += 1
            except:
                pass
#Avg of the longitude and latitude is calculated
        for key in te_dict:
            te_dict[key][0] /= te_dict[key][2]
            te_dict[key][1] /= te_dict[key][2]
#Final time is stored 
ft = time.time()
#Printing the time taken to run for 20 times
print("Time taken to run 20 times: ", ft - st)


# In[42]:


#Using this variable the three tables are combined together
#Using the UNION operator and two SELECT statements
c.execute("DROP VIEW IF EXISTS CombinedTable_view;")
combined_view = '''CREATE VIEW CombinedTable_view AS
    SELECT users_1.id, users_1.name, users_1.screen_name, users_1.description, users_1.friends_count, tweets_1.created_at, tweets_1.id_str, tweets_1.text, tweets_1.source, tweets_1.in_reply_to_user_id, tweets_1.in_reply_to_screen_name, tweets_1.in_reply_to_status_id, tweets_1.retweet_count, tweets_1.contributors, geo_table_1.longitude, geo_table_1.latitude, geo_table_1.type
    FROM users_1 LEFT OUTER JOIN tweets_1 ON users_1.id = tweets_1.id_str LEFT OUTER JOIN geo_table_1 ON geo_table_1.GeoID = tweets_1.id_str UNION
    SELECT users_1.id, users_1.name, users_1.screen_name, users_1.description, users_1.friends_count, tweets_1.created_at, tweets_1.id_str, tweets_1.text, tweets_1.source, tweets_1.in_reply_to_user_id, tweets_1.in_reply_to_screen_name, tweets_1.in_reply_to_status_id, tweets_1.retweet_count, tweets_1.contributors, geo_table_1.longitude, geo_table_1.latitude, geo_table_1.type
    FROM geo_table_1 LEFT OUTER JOIN tweets_1 ON geo_table_1.GeoID = tweets_1.id_str LEFT OUTER JOIN users_1 ON tweets_1.id_str = users_1.id
    '''
#The query is executed that is inside the combined_view 
viewer = c.execute(combined_view)
conn.commit()
#Prints the length of the joined view
print("Length of joined view")
#Executes the no of rows 
c.execute("SELECT count(*) FROM CombinedTable_view;")
#Using the loop the results are printed 
for item in c:
    print(str(item).strip(",)").strip("("))


# In[53]:


#It executes  the SQL query where all the columns are selected
#Returned to the query
#Stored in the row var
c.execute("SELECT * FROM CombinedTable_view")
rows = c.fetchall()
#Empty list is created and iteration is done
#tuple is created and is added on to the row_entry list
row_entry = []
for i in rows:
    all = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10],
           i[11], i[12], i[13], i[14], i[15], i[16])
    row_entry.append(all) 
#the row_entry is converted into a string JSON
#file1.js is opened with write mode that is added to the file
j_son = json.dumps(row_entry)
with open("file1.js", "w") as file:
    file.write(j_son)
#An empty list of obj is created
obj = []
#Looping through each row
for n in rows:
#ordered_dict is an ordered dictionary that contains the key-value pairs
#corresponding to each column in the row
    ordered_dict = collections.OrderedDict()
    ordered_dict["id"] = n[0]
    ordered_dict["name"] = n[1]
    ordered_dict["screen_name"] = n[2]
    ordered_dict["description"] = n[3]
    ordered_dict["friends_count"] = n[4]
    ordered_dict["created_at"] = n[5]
    ordered_dict["id_str"] = n[6]
    ordered_dict["text"] = n[7]
    ordered_dict["source"] = n[8]
    ordered_dict["in_reply_to_uder_id"] = n[9]
    ordered_dict["in_reply_to_screen_name"] = n[10]
    ordered_dict["in_reply_to_status_id"] = n[11]
    ordered_dict["retweet_count"] = n[12]
    ordered_dict["contributors"] = n[13]
    ordered_dict["longitude"] = n[14]
    ordered_dict["latitiude"] = n[15]
    ordered_dict["type"] = n[16]    
    obj.append(ordered_dict)
#The json.dumps method converts the obj list to a JSON string
final_file = json.dumps(obj)
with open("file1.js", "w") as x:
    x.write(final_file)


# In[ ]:


df = pd.read_json ('C:/Users/admin/Downloads/file1.js')
df.to_csv ('file1.csv', index = None)

