DROP TABLE N_ADDRESS;
DROP TABLE SAL_JOB;
DROP TABLE N_JOB;

CREATE TABLE N_ADDRESS
(
    FirstName VARCHAR2(25) NOT NULL,
    LastName VARCHAR2(25) NOT NULL,
    Address VARCHAR2(50) NOT NULL,
    
    CONSTRAINT First_Last_PK
        PRIMARY KEY(FirstName,LastName)
           
);

CREATE TABLE SAL_JOB
(
    JobName VARCHAR2(25) NOT NULL,
    Salary NUMBER(8,2) NOT NULL,
    Assistant VARCHAR2(10) NOT NULL,
    
    CONSTRAINT SJob_PK
        PRIMARY KEY(JobName)
           
);

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
