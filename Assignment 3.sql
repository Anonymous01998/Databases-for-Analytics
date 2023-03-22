-- Drop all the tables to clean up
DROP TABLE Animal;

-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);
INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.75);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.5);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.5);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.75);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.75);

SELECT * FROM ANIMAL;
SELECT AName,TimeToFeed FROM Animal WHERE timetofeed < 2;
SELECT * FROM Animal WHERE acategory = 'rare' OR acategory = 'exotic';
SELECT * FROM Animal WHERE acategory is NULL;
SELECT AName,acategory,timetofeed FROM Animal WHERE timetofeed > 1.5 and timetofeed < 2.25;
SELECT MAX(TimeToFeed) AS maximum_time, MIN(TimeToFeed) AS minimum_time FROM Animal;
SELECT AVG(TimeToFeed) from Animal where acategory = 'common';
SELECT COUNT(AID) - COUNT(ACategory) AS NumNullValues FROM Animal;
SELECT AName FROM Animal WHERE AName = 'Alpaca' OR AName = 'Llama' OR NOT ACategory = 'exotic';