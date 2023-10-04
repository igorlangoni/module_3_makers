DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP SEQUENCE IF EXISTS comments_id_seq;
CREATE SEQUENCE posts_id_seq;
CREATE SEQUENCE comments_id_seq;
CREATE TABLE posts (
    id serial PRIMARY KEY,
    title varchar(255),
    content varchar(255)
);
CREATE TABLE comments (
    id serial PRIMARY KEY,
    content varchar(255),
    author varchar(255),
    post_id integer,
    constraint fk_posts foreign key(post_id) references posts(id) on delete cascade
);
INSERT INTO posts (title, content) VALUES ('Success', 'I got the job!');
INSERT INTO comments (content, author, post_id) VALUES ('Congratulations!', 'Makers', 1);
INSERT INTO comments (content, author, post_id) VALUES ('Congratulations!', 'Makers', 1);
INSERT INTO comments (content, author, post_id) VALUES ('Congratulations!', 'Makers', 1);











