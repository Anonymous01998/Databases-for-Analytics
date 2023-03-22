#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the package
import sqlite3
#Connecting to the SQL database
conn = sqlite3.connect('DSC__450.db')
c = conn.cursor()
#Creating a table
table1 = '''
CREATE TABLE ADDRESS
(
    FirstName VARCHAR2(25) NOT NULL,
    LastName VARCHAR2(25) NOT NULL,
    Address VARCHAR2(50) NOT NULL,
    
    CONSTRAINT First_Last_PK
        PRIMARY KEY(FirstName,LastName)
           
);
'''
c.execute(table1)


# In[2]:


#Address values are inserted
c.execute("INSERT OR IGNORE INTO ADDRESS VALUES ('John','Smith','111 N. Wabash Avenue');");
c.execute("INSERT OR IGNORE INTO ADDRESS VALUES ('Jane','Doe','243 S. Wabash Avenue');");
c.execute("INSERT OR IGNORE INTO ADDRESS VALUES ('Mike','Jackson','1 Michigan Avenue');");
c.execute("INSERT OR IGNORE INTO ADDRESS VALUES ('Mary','Who','20 S. Michigan Avenue');");
c.execute("SELECT * FROM ADDRESS;");
print(list(c))


# In[4]:


#Creating a table
table2 = '''
CREATE TABLE SAL_JOB
(
    JobName VARCHAR2(25) NOT NULL,
    Salary NUMBER(8,2) NOT NULL,
    Assistant VARCHAR2(10) NOT NULL,
    
    CONSTRAINT SJob_PK
        PRIMARY KEY(JobName)
           
);
'''
c.execute(table2)


# In[5]:


#Roles and salary 
c.execute("INSERT OR IGNORE INTO SAL_JOB VALUES ('plumber',40000,'NULL');")
c.execute("INSERT OR IGNORE INTO SAL_JOB VALUES ('bouncer',35000,'NULL');")
c.execute("INSERT OR IGNORE INTO SAL_JOB VALUES ('waitress',50000,'Yes');")
c.execute("INSERT OR IGNORE INTO SAL_JOB VALUES ('accountant','NULL','Yes');")
c.execute("INSERT OR IGNORE INTO SAL_JOB VALUES ('risk analyst',80000,'Yes');")
c.execute("SELECT * FROM SAL_JOB;");
print(list(c))


# In[6]:


#Creating a table
table3 = '''
CREATE TABLE N_JOB
(
    N_FirstName VARCHAR2(25) NOT NULL,
    N_LastName VARCHAR2(25) NOT NULL,
    N_JobName VARCHAR2(10) NOT NULL,
    
    CONSTRAINT N_PK
        PRIMARY KEY(N_FirstName,N_LastName,N_JobName),
        
    CONSTRAINT N_PK1
        FOREIGN KEY(N_FirstName,N_LastName)
            REFERENCES N_ADDRESS(FirstName,LastName),
            
    CONSTRAINT N_PK2
        FOREIGN KEY(N_JobName)
            REFERENCES SAL_JOB(JobName)
           
);
'''
c.execute(table3)


# In[7]:


c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('John','Smith','plumber');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('John','Smith','bouncer');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Jane','Doe','waitress');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Jane','Doe','accountant');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Jane','Doe','bouncer');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Mike','Jackson','accountant');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Mike','Jackson','plumber');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Mary','Who','accountant');")
c.execute("INSERT OR IGNORE INTO N_JOB VALUES ('Mary','Who','risk analyst');")
c.execute("SELECT * FROM N_JOB;");
print(list(c))
conn.commit()
conn.close()


# In[ ]:




