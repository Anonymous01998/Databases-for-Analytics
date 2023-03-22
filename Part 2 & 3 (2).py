#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Importing the packages
import urllib.request
import json
import sqlite3

#Creating the var's for the created table from SQL
users_table = """
create table users (
   id                varchar(38),
   name              varchar(38),
   screen_name       varchar2(38),
   description       varchar2(38),
   friends_count     integer,
   constraint id_PK
       primary key (id)
);
"""
tweets_table = """
create table tweets (
    created_at                     varchar2(38),
    id_str                         varchar2(38),
    text                           varchar(140),
    source                         varchar(60),
    in_reply_to_user_id            varchar2(38),
    in_reply_to_screen_name        varchar2(38),
    in_reply_to_status_id          number(20),
    retweet_count                  number(10),
    contributors                   varchar2(38),
    user_id                        varchar2(38),
    constraint tweets_PK
        primary key (id_str),
    constraint tweets__PK
        foreign key (id_str)
            references users(id)
);
"""
#Connecting to the SQL database
conn = sqlite3.connect('DSC_450.db')
c = conn.cursor()
#Dropping Users
c.execute('Drop table if exists Users;')
#Dropping tweets
c.execute('Drop table if exists tweets;')
#Executing both the users and tweets table
c.execute(users_table)
c.execute(tweets_table)
#Creating an empty list
tweets = []
errors = []
allTweets = urllib.request.urlopen("http://dbgroup.cdm.depaul.edu/DSC450/Module7.txt")
for tweet in allTweets:
   try:
      tdict = json.loads(tweet.decode('utf8'))
   except ValueError:
      errors.append(tweet)
#Writing the txt file
with open("Module7_errors.txt", "w") as errors_file:
    for x in errors:
        errors_file.write(str(x))
with open("Module7_errors.txt", "r") as errors_file:
    contents = errors_file.read()
    print(contents)
#writing the errors in the file
for x in errors:
    errors.write(str(x))
#The tweets are copied to the table
for attributes in tweets:
    name = attributes["user"]["name"]
    screen_name = attributes["user"]["screen_name"]
    description = attributes["user"]["description"]
    friends_count = attributes["user"]["friends_count"]
    created_at = attributes["created_at"]
    id_str = attributes["id_str"]
    text = attributes["text"]
    source = attributes["source"]
    in_reply_to_user_id = attributes["in_reply_to_user_id"]
    in_reply_to_screen_name = attributes["in_reply_to_screen_name"]
    in_reply_to_status_id = attributes["in_reply_to_status_id"]
    retweet_count = attributes["retweet_count"]
    contributors = attributes["contributors"]
    user_id = attributes["user_id"]
    users_input = [id, name, screen_name, description, friends_count]
    tweets_input = [created_at, id_str, text, source, in_reply_to_user_id, in_reply_to_screen_name,
                    in_reply_to_status_id, retweet_count, contributors, user_id]
#The values are inputted onto the tables
c.execute("INSERT OR IGNORE INTO users VALUES (?,?,?,?,?)", users_input)
c.execute("INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tweets_input)
c.execute("SELECT * FROM users")
rows = c.fetchone()
#The user is displayed
print("Record from users table is displayed")
for r in rows:
    print(r, end=" ")
print("\n")
#The tweet is displayed
c.execute("SELECT * FROM tweets")
rows = cursor.fetchone()
print("Record is displayed from the users tweet")
for r in rows:
    print(r,end=" ")


# In[3]:


#importing package
import re
#Defining the fn checkcardvalidity and takes single argument as cardno
def checkcardvalidity(cardno):
#Using the regular expressions that matches the valid credit card number
#16 digit number divided by 4 
    regex = "(\d{4} ?){3}\d{4}"
    row = re.fullmatch(regex, cardno)
#Checks for the validity and responds with card number valid or invalid
    if row is not None:
        print( "The card number is valid:",cardno)
    else:
        print( "The card number is not valid:",cardno)
def unittest() : 
    print("Checking the cards validity")
    print("\n")
    checkcardvalidity("9010 8538 0000 6070")
    checkcardvalidity("9010853800006070")
    checkcardvalidity("5621/7357/2054/3463")
    checkcardvalidity("4241-5443-8652-6742")
    checkcardvalidity("4241-5443-8652-6742") 
#unittest fn is called to execute the tests 
#Results are printed
unittest()
print("\n")


# In[ ]:




