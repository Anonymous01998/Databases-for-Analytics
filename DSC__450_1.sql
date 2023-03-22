CREATE TABLE Balance (
  BankBalance NUMBER(5,2),
  CONSTRAINT balance CHECK (BankBalance > 0 AND BankBalance < 999999.99)
);

CREATE TABLE Street (Street VARCHAR2(26) CHECK (Street LIKE 'strasse%'));

CREATE TABLE Student(
STUDENTID Number(20) Primary Key,
Name VARCHAR2(125),
Address VARCHAR2(125),
GradYear Number(4)
);

CREATE TABLE Course(
CName VARCHAR(50) Primary Key,
Department VARCHAR2(50),
Credits Number(2)
);

DROP TABLE GRADE;
CREATE TABLE Grade(
CName VARCHAR2(50),
StudentID Number(20),
CGrade CHAR(2),
CONSTRAINT Course_FK
Foreign KEY (CName)
REFERENCES Course(CName),
CONSTRAINT Student_FK
Foreign KEY (StudentID)
REFERENCES STUDENT(StudentID)
);

SELECT StudentID, Name 
FROM Student
WHERE GradYear >= (SELECT MIN(GradYear) FROM Student) 
AND GradYear < (SELECT MIN(GradYear) FROM Student)+2;

SELECT Name, CName, CGrade
FROM Student
LEFT JOIN Grade 
ON Student.StudentID = Grade.StudentID
WHERE Name LIKE '%Milton%'
ORDER BY CGrade DESC;

SELECT Name, GradYear
FROM Student
WHERE Student.StudentID
IN (SELECT Student.StudentID FROM Student
INNER JOIN Grade ON Student.StudentID = Grade.StudentID
GROUP BY Student.StudentID, CName
HAVING CName IS NULL OR Count(CName) = 1);

UPDATE Student
SET GradYear = GradYear + 3
WHERE Address LIKE '%Chicago%';

ALTER TABLE Course
ADD Chair VARCHAR2(22);

CREATE VIEW School AS
SELECT Student.STUDENTID, Student.Name, Student.Address, Student.GradYear, Course.CName, Course.Department, Course.Credits, Grade.CGrade
FROM student
INNER JOIN Grade
    ON Student.StudentID = Grade.StudentID
INNER JOIN Course
    ON Course.CName = Grade.CName;

UPDATE Course
SET Credits = 4
WHERE CName = 'SQL';

UPDATE Course
SET Credits = 2
WHERE CName = 'JAVA';

UPDATE Course
SET Credits = 4
WHERE CName = 'PYTHON';

UPDATE Course
SET Credits = 2
WHERE CName = 'MicroProcessor';

INSERT INTO Student VALUES(38, 'Mark Callaway', 'Chicago', 2023); 
INSERT INTO Student VALUES(73, 'Ronaldo Matrinez','New Texas', 2026); 
INSERT INTO Student VALUES(12, 'Damon John',  'Seattle', 2023); 
INSERT INTO Student VALUES(66, 'Ronaldo Brock','California', 2024); 
INSERT INTO Student VALUES(88, 'Lucy Rohland','New Jersey', 2022); 
INSERT INTO Student VALUES(39, 'Christopher Jack','Atlanta', 2025); 
INSERT INTO Student VALUES(85, 'Gallaway Marcus','Michigan', 2021);
INSERT INTO Course (CName, Department, Credits) VALUES ('SQL', 'Computer Science', 4);
INSERT INTO Course (CName, Department, Credits) VALUES ('JAVA', 'Computer Science', 2);
INSERT INTO Course (CName, Department, Credits) VALUES ('PYTHON', 'Computer Science', 4);
INSERT INTO Course (CName, Department, Credits) VALUES ('MicroProcessor', 'CyberSecurity', 2);
INSERT INTO Course (CName, Department, Credits) VALUES ('C++', 'Game Developer', 2);
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('SQL', 73, 'B');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('PYTHON', 12, 'B');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('JAVA', 66, 'A');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('MicroProcessor', 38, 'A');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('PYTHON', 39, 'A');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('SQL', NULL, 'B');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('MicroProcessor', 88, 'B');
INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('C++', 85, 'B');


DROP VIEW School;

SELECT *
From School;

SELECT MIN(gradyear), department
FROM School
GROUP BY department;

SELECT MAX(gradyear), department
FROM School
GROUP BY department;