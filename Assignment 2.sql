CREATE TABLE Authors
(
LASTNAME VARCHAR2(25),
FIRSTNAME VARCHAR2(25),
ID NUMBER(*,0),
BIRTHDATE DATE,

    CONSTRAINT Authors_PK
    PRIMARY KEY (ID)
);

CREATE TABLE Publishers
(
NAME VARCHAR2(50),
PUBNUMBER NUMBER(*,0),
ADDRESS VARCHAR2(100),

    CONSTRAINT Publishers_PK
    PRIMARY KEY (PUBNUMBER)
);

CREATE TABLE BOOKS
(
ISBN VARCHAR2(25),
TITLE VARCHAR2(75),
PUBLISHER NUMBER(*,0),

    CONSTRAINT Books_PK
    PRIMARY KEY (ISBN)
);

CREATE TABLE Book_Author
(
AuthorID NUMBER(*,0),
ISBN VARCHAR2(25),
Position NUMBER (1),

    CONSTRAINT Book_Author_PK
    PRIMARY KEY (AuthorID, ISBN),
        
    CONSTRAINT Book_Author_FK1
     FOREIGN KEY (AuthorID)
       REFERENCES Authors(ID),
       
    CONSTRAINT Book_Author_FK2
     FOREIGN KEY (ISBN)
       REFERENCES BOOKS(ISBN)
);

INSERT INTO Authors VALUES ('King', 'Stephen', 2, to_date('September 9 1947', 'Month dd, YYYY'));
INSERT INTO Authors VALUES ('Asimov', 'Isaac', 4, to_date('January 2 1921', 'Month dd, YYYY'));
INSERT INTO Authors VALUES ('Verne', 'Jules', 7, to_date('February 8 1828', 'Month dd, YYYY'));
INSERT INTO Authors VALUES ('Rowling', 'Joanne', 37, to_date('July 31 1965', 'Month dd, YYYY'));

INSERT INTO Publishers VALUES ('Bloomsbury Publishing', 17, 'London Borough of Camden');
INSERT INTO Publishers VALUES ('Arthur A. Levine Books', 18, 'New York City');

INSERT INTO BOOKS VALUES ('1111-111', 'Databases from outer space', 17);
INSERT INTO BOOKS VALUES ('2223-233', 'Revenge of SQL', 17);
INSERT INTO BOOKS VALUES ('3333-323', 'The night of the living databases', 18);

INSERT INTO Book_Author VALUES (2, '1111-111', 1);
INSERT INTO Book_Author VALUES (4, '1111-111', 2);
INSERT INTO Book_Author VALUES (4, '2223-233', 1);
INSERT INTO Book_Author VALUES (7, '2223-233', 2);
INSERT INTO Book_Author VALUES (37, '3333-323', 1);
INSERT INTO Book_Author VALUES (2, '3333-323', 2);

SELECT * FROM Authors;
SELECT * FROM Publishers;
SELECT * FROM BOOKS;
SELECT * FROM Book_Author;

CREATE TABLE Departments
(
DEPARTMENT_NAME VARCHAR2(50),
CHAIR VARCHAR2(25),
ENDOWMENT NUMBER(*,0),

    CONSTRAINT Departments_PK
    PRIMARY KEY (DEPARTMENT_NAME)
);

CREATE TABLE Advisors
(
ID NUMBER (*,0),
ADVISOR_NAME VARCHAR2(25),
ADDRESS VARCHAR2(100),
RESEARECH_AREA VARCHAR2(25),
REFERENCE_LINK VARCHAR2(25),

    CONSTRAINT Advisors_PK
    PRIMARY KEY (ID),
    CONSTRAINT Advisors_FK
    FOREIGN KEY (REFERENCE_LINK)
    REFERENCES Departments(DEPARTMENT_NAME)
);

CREATE TABLE Students
(
STUDENT_ID NUMBER(*,0),
FIRSTNAME VARCHAR2(25),
LASTNAME VARCHAR2(25),
DOB DATE,
TELEPHONE VARCHAR2(12),
REFERENCE_ADVISOR NUMBER (*,0),

    CONSTRAINT Students_PK
    PRIMARY KEY (STUDENT_ID),
    CONSTRAINT Students_FK
    FOREIGN KEY (REFERENCE_ADVISOR)
    REFERENCES Advisors(ID)
);


