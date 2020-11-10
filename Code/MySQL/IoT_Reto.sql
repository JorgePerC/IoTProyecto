

DROP DATABASE IF EXISTS IoT_Proyecto;
CREATE DATABASE IoT_Proyecto;

USE IoT_Proyecto;


CREATE TABLE users (
    id_user int primary key NOT NULL AUTO_INCREMENT,
    name varchar(15),
    last_name varchar(15),
    age int,
    excersice 
)


CREATE TABLE Constants_HR (
    Age_Interval enum("5-6", "7-9", "10-more"),
    Excersice enum("Few", "Ocasional", "Proffesional"),
    Result varchar(20)
)


file _Img ##,
    Acvareerage_Sa002 int,

INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("5-6", "Few", "75-115")
INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("5-6", "Ocasional","75-115" )
INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("5-6", "Proffesional","75-115")

INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("7-9", "Few", "70-110")
INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("7-9", "Ocasional", "70-110")
INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("7-9", "Proffesional", "60-100")

INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("10-more", "Few", "60-100")
INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("10-more", "Ocasional", "50-60")
INSERT INTO Constants_HR (Age_Interval, Excersice, Result) values ("10-more", "Proffesional","40-60" )



