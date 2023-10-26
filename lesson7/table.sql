CREATE TABLE Class (id SERIAl PRIMARY KEY,
name varchar(55) NOT NULL,
qty int DEFAULT 0,
start_date date NOT NULL,
end_date date NULL);

CREATE TABLE Student(id SERIAl PRIMARY KEY,
class_id int REFERENCES Class(id),
login varchar(55) NOT NULL,
first_name varchar(55),
is_verified boolean DEFAULT FALSE);

INSERT INTO Class (name, start_date) VALUES('python-23-2', '05-09-2023');

SELECT * FROM Class;


INSERT INTO Class (name, start_date) VALUES('js-17-1', '18-10-2023'), ('java-18-2', '19-10-2023');

SELECT * FROM Class;