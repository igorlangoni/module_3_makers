DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_seq_id;
DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS order_seq_id;
DROP TABLE IF EXISTS items_orders CASCADE;

CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name text,
    price int,
    quantity int
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer text,
    item text,
    date date
);

INSERT INTO items (name, price, quantity) VALUES ('Atletico Mineiro 2023 Home Kit', 80, 50);
INSERT INTO items (name, price, quantity) VALUES ('Atletico Mineiro 2023 Away Kit' , 75, 30);
INSERT INTO items (name, price, quantity) VALUES ('Atletico Mineiro 2023 Junior Kit' , 50, 50);
INSERT INTO items (name, price, quantity) VALUES ('Football - Size 5, adidas' , 50, 100);
INSERT INTO items (name, price, quantity) VALUES ('Football - Size 5, nike' , 60, 100);
INSERT INTO items (name, price, quantity) VALUES ('Atletico Mineiro Jumper' , 150, 30);
INSERT INTO items (name, price, quantity) VALUES ('T-Shirt - I S2 BH' , 35, 80);
INSERT INTO items (name, price, quantity) VALUES ('Autographed Home Kit' , 200, 15);
INSERT INTO items (name, price, quantity) VALUES ('Football Boots, various sizes, adidas' , 65, 100);
INSERT INTO items (name, price, quantity) VALUES ('Football Boots, various sizes, nike' , 65, 100);




CREATE TABLE IF NOT EXISTS items_orders (
    item_id int,
    order_id int,
    CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE,
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    PRIMARY KEY (item_id, order_id)
);