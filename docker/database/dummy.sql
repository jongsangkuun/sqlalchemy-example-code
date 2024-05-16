CREATE TABLE search_one_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE search_many_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE insert_one_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE insert_many_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE update_one_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE update_many_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE delete_one_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE delete_many_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO search_one_table (id, name, email) VALUES (1, 'test1', 'test1@example.com');

INSERT INTO search_many_table (id, name, email) VALUES
(2,'test2', 'test2@example.com'),
(3,'test3', 'test3@example.com'),
(4,'test4', 'test4@example.com'),
(5,'test5', 'test5@example.com');

INSERT INTO update_one_table (id,name, email) VALUES (6,'test6', 'test6@example.com');

INSERT INTO update_many_table (id,name, email) VALUES
(7,'test7', 'test7@example.com'),
(8,'test8', 'test8@example.com'),
(9,'test9', 'test9@example.com'),
(10,'test10', 'test10@example.com');

INSERT INTO delete_one_table (id,name, email) VALUES (11,'test11', 'test11@example.com');

INSERT INTO delete_many_table (id,name, email) VALUES
(12,'test12', 'test12@example.com'),
(13,'test13', 'test13@example.com'),
(14,'test14', 'test14@example.com'),
(15,'test15', 'test15@example.com');