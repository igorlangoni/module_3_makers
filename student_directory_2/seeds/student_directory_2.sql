DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int
);

INSERT INTO cohorts (name, starting_date) VALUES ('chocolate', 'sept 23');
INSERT INTO cohorts (name, starting_date) VALUES ('marshmallow', 'apr 23');
INSERT INTO cohorts (name, starting_date) VALUES ('cake', 'jan 23');

INSERT INTO students (name, cohort_id) VALUES ('Igor', 1);
INSERT INTO students (name, cohort_id) VALUES ('Alline', 2);
INSERT INTO students (name, cohort_id) VALUES ('Alex', 1);
INSERT INTO students (name, cohort_id) VALUES ('Vitor', 3);
INSERT INTO students (name, cohort_id) VALUES ('Keziah', 1);
INSERT INTO students (name, cohort_id) VALUES ('José', 3);
INSERT INTO students (name, cohort_id) VALUES ('Fatma', 1)