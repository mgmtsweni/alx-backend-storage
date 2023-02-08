-- Creates a table with unique users.
CREATE TABLE IF NOT EXISTSusers (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
