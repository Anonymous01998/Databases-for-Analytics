/*
	company.sql
	Alexander Rasin (with thanks to Eric J. Schwabe)
	CSC 455 Fall 2016

*/

-- drop tables

DROP TABLE EMPLOYEE CASCADE CONSTRAINTS;
DROP TABLE DEPARTMENT CASCADE CONSTRAINTS;
DROP TABLE PROJECT CASCADE CONSTRAINTS;
DROP TABLE WORKS_ON CASCADE CONSTRAINTS;

-- create and populate tables

CREATE TABLE EMPLOYEE
(
	Fname		VARCHAR(20),
	Minit		CHAR(1),
	Lname		VARCHAR(20),
	Ssn		CHAR(9),
	Bdate		DATE,
	Address		VARCHAR(30),
	Sex		CHAR(1),
	Salary		NUMBER(5),
	Super_Ssn	CHAR(9),
	Dno		NUMBER(1),

	PRIMARY KEY (Ssn),
		
	FOREIGN KEY (Super_ssn)
		REFERENCES EMPLOYEE (Ssn)
);

INSERT INTO EMPLOYEE VALUES ('James', 'E', 'Borg', '888665555', DATE '1937-11-10', '450 Stone, Houston, TX', 'M', 55000, NULL, 1);
INSERT INTO EMPLOYEE VALUES ('Jennifer', 'S', 'Wallace', '987654321', DATE '1941-06-20', '291 Berry, Bellaire, Tx', 'F', 37000, '888665555', 4);
INSERT INTO EMPLOYEE VALUES ('Franklin', 'T', 'Wong', '333445555', DATE '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5);
INSERT INTO EMPLOYEE VALUES ('John', 'B', 'Smith', '123456789', DATE '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000, '333445555', 5);
INSERT INTO EMPLOYEE VALUES ('Alicia', 'J', 'Zelaya', '999887777', DATE '1968-01-19', '3321 castle, Spring, TX', 'F', 25000, '987654321', 4);
INSERT INTO EMPLOYEE VALUES ('Ramesh', 'K', 'Narayan', '666884444', DATE '1920-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, '333445555', 5);
INSERT INTO EMPLOYEE VALUES ('Joyce', 'A', 'English', '453453453', DATE '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5);
INSERT INTO EMPLOYEE VALUES ('Ahmad', 'V', 'Jabbar', '987987987', DATE '1969-03-29', '980 Dallas, Houston, TX', 'M', 22000, '987654321', 4);
INSERT INTO EMPLOYEE VALUES ('Melissa', 'M', 'Jones', '808080808', DATE '1970-07-10', '1001 Western, Houston, TX', 'F', 27500, '333445555', 5);

CREATE TABLE DEPARTMENT
(
	Dname		VARCHAR(20),
	Dnumber		NUMBER(1),
	Mgr_ssn		CHAR(9),
	Mgr_start_date	DATE,
	
	PRIMARY KEY (Dnumber),

	FOREIGN KEY (Mgr_ssn)
		REFERENCES EMPLOYEE (Ssn)
);

INSERT INTO DEPARTMENT VALUES ('Research', 5, '333445555', DATE '1988-05-22');
INSERT INTO DEPARTMENT VALUES ('Administration', 4, '987654321', DATE '1995-01-01');
INSERT INTO DEPARTMENT VALUES ('Headquarters', 1, '888665555', DATE '1981-06-19');

-- this alter is here because Employee table was created first

ALTER TABLE EMPLOYEE ADD FOREIGN KEY (Dno) REFERENCES DEPARTMENT (Dnumber);

CREATE TABLE PROJECT
(
	Pname		VARCHAR(20),
	Pnumber		NUMBER(2),
	Plocation	VARCHAR(20),
	Dnum		NUMBER(1),

	PRIMARY KEY (Pnumber)
);

INSERT INTO PROJECT VALUES ('ProductX', 1, 'Bellaire', 5);
INSERT INTO PROJECT VALUES ('ProductY', 2, 'Sugarland', 5);
INSERT INTO PROJECT VALUES ('ProductZ', 3, 'Houston', 5);
INSERT INTO PROJECT VALUES ('Computerization', 10, 'Stafford', 4);
INSERT INTO PROJECT VALUES ('Reorganization', 20, 'Houston', 1);
INSERT INTO PROJECT VALUES ('Newbenefits', 30, 'Stafford', 4);

CREATE TABLE WORKS_ON
(
	Essn		CHAR(9),
	Pno		NUMBER(2),
	Hours		NUMBER(3,1),
	
	PRIMARY KEY (Essn, Pno),

	FOREIGN KEY (Essn)
		REFERENCES EMPLOYEE (Ssn),

	FOREIGN KEY (Pno)
		REFERENCES PROJECT(Pnumber)
);

INSERT INTO WORKS_ON VALUES ('123456789', 1, 32.0);
INSERT INTO WORKS_ON VALUES ('123456789', 2, 8.0);
INSERT INTO WORKS_ON VALUES ('453453453', 1, 20.0);
INSERT INTO WORKS_ON VALUES ('453453453', 2, 20.0);
INSERT INTO WORKS_ON VALUES ('333445555', 1, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 2, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 3, 5.0);
INSERT INTO WORKS_ON VALUES ('333445555', 10, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 20, 10.0);
INSERT INTO WORKS_ON VALUES ('333445555', 30, 5.0);
INSERT INTO WORKS_ON VALUES ('999887777', 30, 30.0);
INSERT INTO WORKS_ON VALUES ('999887777', 10, 10.0);
INSERT INTO WORKS_ON VALUES ('987987987', 10, 35.0);
INSERT INTO WORKS_ON VALUES ('987987987', 30, 5.0);
INSERT INTO WORKS_ON VALUES ('987654321', 30, 20.0);
INSERT INTO WORKS_ON VALUES ('987654321', 20, 15.0);
INSERT INTO WORKS_ON VALUES ('888665555', 20, 10.0);


-- display contents of tables

SELECT * FROM EMPLOYEE;
SELECT * FROM DEPARTMENT;
SELECT * FROM PROJECT;
SELECT * FROM WORKS_ON;

SELECT fname, lname FROM employee WHERE super_ssn IN ( SELECT SSN
                                                        FROM employee   
                                                        WHERE fname = 'Franklin' 
                                                        AND lname = 'Wong')

SELECT PNAME, PNUMBER, SUM(HOURS) FROM project, works_on WHERE PNO = PNUMBER 
GROUP BY PNAME, PNUMBER ORDER BY SUM (Hours)

SELECT DNAME, DNUMBER, AVG(SALARY) FROM DEPARTMENT, EMPLOYEE WHERE DNO = DNUMBER 
GROUP BY DNAME, DNUMBER ORDER BY DNUMBER;

SELECT AVG(SALARY) AS AVG_SAL_FEMALE FROM employee WHERE sex = 'F';

SELECT DNAME, COUNT(*) AS Num_of_employees FROM department, employee
WHERE DNO = department.dnumber GROUP BY department.dname HAVING AVG(employee.salary) > 42000;

SELECT fname, lname FROM employee WHERE salary >= 22000 - (SELECT MAX(salary) "Maximum" FROM employee);

SELECT * FROM employee WHERE sex = 'F';

SELECT * FROM employee WHERE sex in (SELECT sex FROM employee WHERE sex = 'F');

SELECT fname, lname FROM employee WHERE ssn IN (SELECT ssn FROM employee MINUS SELECT essn FROM works_on 
GROUP BY works_on.essn);

DROP TABLE Chauffeurs;

CREATE TABLE Chauffeurs (
    License_Number NUMBER(6, 0),
    Renewed VARCHAR2(10),
    Status VARCHAR2(20),
    StatusDate DATE,
    DriverType VARCHAR2(20),
    LicenseType VARCHAR2(20),
    OriginalIssueDate DATE,
    Fulln_ VARCHAR2(100),
    Sex VARCHAR2(10),
    ChauffeurCity VARCHAR2(50),
    ChauffeurState VARCHAR2(2), 
    RecordNumber VARCHAR(20),
    
    CONSTRAINT PUBLIC_PK
PRIMARY KEY (License_Number)
);

SELECT COUNT (*) FROM Chauffeurs;

SELECT * FROM Chauffeurs;

DROP TABLE Tweets;
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
);
SELECT * FROM Tweets;