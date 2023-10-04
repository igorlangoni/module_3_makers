DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipe_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipe_id_seq;
CREATE TABLE recipes (
    id SERIAL,
    name text,
    cooking_time int,
    rating float
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Strogonoff', 40, 8);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Lasagna', 70, 7.5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Feijoada', 120, 10);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Prawn Curry', 40, 7.5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Rice and Beans', 25, 7);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Meatball Spaghetti', 25, 8);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Roasted Joint', 300, 8);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Cake', 120, 4);