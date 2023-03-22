import sqlite3

#Creating the Student Table
Std_Tb = '''CREATE TABLE Student(
StudentID Number(20) Primary Key,
Name VARCHAR2(125),
Address VARCHAR2(125),
GradYear Number(4)
);
'''

#Creating the course table
Crs_Tb = '''CREATE TABLE Course(
CName VARCHAR2(50) Primary Key,
Department VARCHAR2(50),
Credits Number(2)
);
'''

#Creating the Grade table
Gd_Tb = '''CREATE TABLE Grade(
CName VARCHAR2(50),
StudentID Number(20),
CGrade CHAR(2)
);
'''

#View School
School = '''CREATE VIEW School AS
SELECT student.StudentID, student.name, student.address, student.gradyear, course.cname, course.credits, course.department, grade.cgrade
FROM student
INNER JOIN Grade
    ON Student.StudentID = Grade.StudentID
INNER JOIN Course
    ON Course.CName = Grade.CName;
'''

#Connecting to the database
conn = sqlite3.connect("DSC__450")
c = conn.cursor()
c.execute("Drop table if exists Student")
c.execute(Std_Tb)
c.execute("Drop table if exists Course")
c.execute(Crs_Tb)
c.execute("Drop table if exists Grade")
c.execute(Gd_Tb)
c.execute("Drop View if exists School")
c.execute(School)

#Printing the Student table components
print ("INSERT INTO Student VALUES(38, 'Mark Callaway', 'Chicago', 2023);")
print ("INSERT INTO Student VALUES(73, 'Ronaldo Matrinez','New Texas', 2026);")
print ("INSERT INTO Student VALUES(12, 'Damon John',  'Seattle', 2023);")
print ("INSERT INTO Student VALUES(66, 'Ronaldo Brock','California', 2024);")
print ("INSERT INTO Student VALUES(88, 'Lucy Rohland','New Jersey', 2022);")
print ("INSERT INTO Student VALUES(39, 'Christopher Jack','Atlanta', 2025);")
print ("INSERT INTO Student VALUES(82, 'Gallaway Marcus','Michigan', 2021);")

#Executing the Student table components
c.execute ("INSERT OR IGNORE INTO Student VALUES(38, 'Mark Callaway', 'Chicago', 2023); ")
c.execute ("INSERT OR IGNORE INTO Student VALUES(73, 'Ronaldo Matrinez', 'New Texas', 2026); ")
c.execute ("INSERT OR IGNORE INTO Student VALUES(12, 'Damon John', 'Seattle', 2023); ")
c.execute ("INSERT OR IGNORE INTO Student VALUES(66, 'Ronaldo Brock',  'California', 2024); ")
c.execute ("INSERT OR IGNORE INTO Student VALUES(88, 'Lucy Rohland',   'New Jersey', 2022); ")
c.execute ("INSERT OR IGNORE INTO Student VALUES(39, 'Christopher Jack',  'Atlanta', 2025); ")
c.execute ("INSERT OR IGNORE INTO Student VALUES(82, 'Gallaway Marcus','Michigan', 2021);")

#Printing the Course table components
print ("INSERT INTO Course (CName, Department, Credits) VALUES ('SQL', 'Computer Science', 4);")
print ("INSERT INTO Course (CName, Department, Credits) VALUES ('JAVA', 'Computer Science', 2);")
print ("INSERT INTO Course (CName, Department, Credits) VALUES ('PYTHON', 'Computer Science', 4);")
print ("INSERT INTO Course (CName, Department, Credits) VALUES ('MicroProcessor', 'CyberSecurity', 2);")
print ("INSERT INTO Course (CName, Department, Credits) VALUES ('C++', 'Game Developer', 3);")

#Executing the Course table components
c.execute ("INSERT INTO Course (CName, Department, Credits) VALUES ('SQL', 'Computer Science', 4);")
c.execute ("INSERT INTO Course (CName, Department, Credits) VALUES ('JAVA', 'Computer Science', 2);")
c.execute ("INSERT INTO Course (CName, Department, Credits) VALUES ('PYTHON', 'Computer Science', 4);")
c.execute ("INSERT INTO Course (CName, Department, Credits) VALUES ('MicroProcessor', 'CyberSecurity', 2);")
c.execute ("INSERT INTO Course (CName, Department, Credits) VALUES ('C++', 'Game Developer', 3);")

#Printing the grade values
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('SQL', 73, 'B');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('PYTHON', 12, 'B');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('JAVA', 66, 'A');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('MicroProcessor', 38, 'A');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('PYTHON', 39, 'A');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('SQL', NULL, 'B');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('MicroProcessor', 88, 'B');")
print ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('C++', 82, 'B');")

#Executing the grade values
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('SQL', 73, 'B');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('PYTHON', 12, 'B');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('JAVA', 66, 'A');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('MicroProcessor', 38, 'A');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('PYTHON', 39, 'A');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('SQL', NULL, 'B');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('MicroProcessor', 88, 'B');")
c.execute ("INSERT INTO Grade (CName, StudentID, CGrade) VALUES ('C++', 82, 'B');")

#Getting the files from the school database
result_view = c.execute("select * from School").fetchall()
f = open("outputs.txt", "w")
#Whenever there is a NULL in the file it is joined
for Rows in result_view:
    if "NULL" in Rows:
        Rows = Rows.replace("NULL", "None")
    print(Rows)
    f.write(", ".join(map(str, Rows)) + "\n")
f.close()
conn.commit()
conn.close()
#Opening the text file and reading it
fd = open("outputs.txt", "r")
fd_datafile = fd.readlines()
#Reading the data from the outputs file that was created
#The data contains the comma separated info
for fd_data in fd_datafile:
    fd_datalist = fd_data.split(',')
#StudentID
    student_ID = fd_datalist[0]
#student_Name
    student_Name = fd_datalist[1]
#student_Addr
    student_Addr = fd_datalist[2]
#stuGrad_Year
    stuGrad_Year = fd_datalist[3]
#CName
    CName = fd_datalist[4]
#Credits
    Credits = fd_datalist[5]
#Department
    Department = fd_datalist[6]
#Grade
    Grade = fd_datalist[7]
#Importing Package
import statistics
query_dict = {}
for qy_data in fd_datafile:
    print(qy_data)
#The data is separated by commas and contains the respective information
    qy_datalist = qy_data.split(',')
#StudentID
    student_ID = qy_datalist[0]
#studentName
    student_Name = qy_datalist[1]
#studentAddr
    stuGrad_Year = qy_datalist[2]
#stuGradYear
    stuGrad_Year = qy_datalist[3]
    stuGrad_Year = int(stuGrad_Year)
#CName
    CName = qy_datalist[4]
#Credits
    Credits = qy_datalist[5]
#Department
    Department = qy_datalist[6]
#Grade
    Grade = qy_datalist[7]
#Checking if the dpt is in query_dict
#Adds the student's grad year
    if (Department) in query_dict:
        print("Yes, " + Department + " is in list.")
        query_dict[Department].append(stuGrad_Year)
#If the dpt is not in the dict, adds a new key
#New list is created to store the student's grad year
    else:
        query_dict.update({Department: stuGrad_Year})
        query_dict[Department] = list()
        query_dict[Department].append(stuGrad_Year)
#Printing the contents of the query_dict
    print(query_dict)
#Calculating the mean of the grad yrs for each of the dpt
for i in query_dict:
    print(i, query_dict[i])
    print(i, statistics.mean(query_dict[i]))
