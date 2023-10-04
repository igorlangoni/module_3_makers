-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS movies;
DROP SEQUENCE IF EXISTS movies_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS movies_id_seq;
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    release_year int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO movies (title, genre, release_year) VALUES ('Oppenheimer', 'Comedy', 2023);
INSERT INTO movies (title, genre, release_year) VALUES ('Barbie', 'Horror', 2023);
INSERT INTO movies (title, genre, release_year) VALUES ('The Lion King', 'Romance', 1994);
INSERT INTO movies (title, genre, release_year) VALUES ('Star Wars: A New Hope', 'Comedy', 1980);
INSERT INTO movies (title, genre, release_year) VALUES ('Morbius', 'Horror', 2022);


