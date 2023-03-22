DROP TABLE STUDENT CASCADE CONSTRAINTS;
CREATE TABLE STUDENT(
	ID		CHAR(3),
	Name		VARCHAR2(20),
	Midterm	NUMBER(3,0) 	CHECK (Midterm>=0 AND Midterm<=100),
	Final		NUMBER(3,0)	CHECK (Final>=0 AND Final<=100),
	Homework	NUMBER(3,0)	CHECK (Homework>=0 AND Homework<=100),
	PRIMARY KEY (ID)
);
INSERT INTO STUDENT VALUES ( '445', 'Seinfeld', 86, 90, 99 );
INSERT INTO STUDENT VALUES ( '909', 'Costanza', 74, 72, 86 );
INSERT INTO STUDENT VALUES ( '123', 'Benes', 93, 89, 91 );
INSERT INTO STUDENT VALUES ( '111', 'Kramer', 99, 92, 93 );
INSERT INTO STUDENT VALUES ( '667', 'Newman', 78, 82, 84 );
INSERT INTO STUDENT VALUES ( '889', 'Banya', 51, 65, 50 );
SELECT * FROM STUDENT;

DROP TABLE WEIGHTS CASCADE CONSTRAINTS;
CREATE TABLE WEIGHTS(
	MidPct	NUMBER(2,0) CHECK (MidPct>=0 AND MidPct<=100),
	FinPct	NUMBER(2,0) CHECK (FinPct>=0 AND FinPct<=100),
	HWPct	NUMBER(2,0) CHECK (HWPct>=0 AND HWPct<=100)
);
INSERT INTO WEIGHTS VALUES ( 30, 30, 40 );
SELECT * FROM WEIGHTS;
COMMIT;

SET SERVEROUTPUT ON;

DECLARE
    cursor cs is SELECT * FROM Student;
    cursor cw is SELECT * FROM Weights;
    Total NUMBER;
    finalgrade VARCHAR2(1);
    midterm NUMBER;
    finals NUMBER;
    homeworks NUMBER;
    studentrecord Student%rowtype;
    midterm_Percent Weights.midpct%type;
    finalpercentage Weights.FinPct%type;
    hwpercentage WEIGHTS.HWPct%type;
BEGIN
    SELECT MidPct, FinPct, HWPct 
    INTO midterm_Percent, finalpercentage, hwpercentage
    FROM Weights;

    FOR studentrecord IN cs LOOP
        midterm := studentrecord.Midterm*midterm_Percent;
        finals := studentrecord.Final*finalpercentage;
        homeworks := studentrecord.Homework*hwpercentage;

        Total := (midterm + finals + homeworks)/100;
        IF (Total BETWEEN 90 AND 100) THEN finalgrade := 'A';
        ELSIF (Total BETWEEN 80 AND 89.99) THEN finalgrade := 'B';
        ELSIF (Total BETWEEN 65 AND 79.99) THEN finalgrade := 'C';
        ELSE finalgrade := 'F';
        END IF;
        DBMS_OUTPUT.PUT_LINE(studentrecord.ID||' '||studentrecord.Name||' '||Total||'% '||finalgrade);
    END LOOP;
END;

CREATE TABLE SECTION(
 SectionID 	CHAR(5),
 Course	VARCHAR2(7),
 Students	NUMBER DEFAULT 0,
 CONSTRAINT PK_SECTION 
		PRIMARY KEY (SectionID)
);

CREATE TABLE ENROLLMENT(
 SectionID	CHAR(5),
 StudentID	CHAR(7),
 CONSTRAINT PK_ENROLLMENT 
		PRIMARY KEY (SectionID, StudentID),
 CONSTRAINT FK_ENROLLMENT_SECTION 
		FOREIGN KEY (SectionID)
		REFERENCES SECTION (SectionID)
);
 
INSERT INTO SECTION (SectionID, Course) VALUES ( '12345', 'CSC 355' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '22109', 'CSC 309' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '99113', 'CSC 300' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '99114', 'CSC 300' );
COMMIT;
SELECT * FROM SECTION;


CREATE OR REPLACE TRIGGER enrollment_limit
BEFORE INSERT ON Enrollment
FOR EACH ROW
DECLARE
    countitems INTEGER;
BEGIN
    SELECT COUNT(1) INTO countitems FROM Enrollment
    WHERE SectionID = :new.SectionID;
    countitems := 1 + countitems;
    If countitems > 5 THEN
        raise_application_error(-20102, 'Error as more than 5 entries were inserted');
    ELSE
        UPDATE Section SET Students = countitems WHERE SectionID = :new.SectionID;
    END IF;
END;
INSERT INTO ENROLLMENT VALUES ('12345', '1234567');
INSERT INTO ENROLLMENT VALUES ('12345', '2234567');
INSERT INTO ENROLLMENT VALUES ('12345', '3234567');
INSERT INTO ENROLLMENT VALUES ('12345', '4234567');
INSERT INTO ENROLLMENT VALUES ('12345', '5234567');
INSERT INTO ENROLLMENT VALUES ('12345', '6234567');
SELECT * FROM Section;
SELECT * FROM Enrollment;

CREATE OR REPLACE TRIGGER 
BEFORE DELETE ON Enrollment
FOR EACH ROW
BEGIN
    UPDATE Section SET Students = Students -1 WHERE SectionID = :old.SectionID;
END;

CREATE OR REPLACE TRIGGER enrollment_delete
BEFORE DELETE ON Enrollment
FOR EACH ROW
BEGIN
    UPDATE Section SET Students = Students -1 WHERE SectionID = :old.SectionID;
END;
DELETE FROM ENROLLMENT WHERE StudentID = '1234567';
SELECT * FROM Section;
SELECT * FROM Enrollment;



