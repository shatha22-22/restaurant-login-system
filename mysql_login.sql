-- Create the database 'login_system' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS login_system;

-- Select the 'login_system' database for use
USE login_system;

-- Create the 'users' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Auto-incrementing ID as the primary key
    email VARCHAR(255) UNIQUE NOT NULL,      -- Email field, must be unique and not null
    password VARCHAR(255) NOT NULL           -- Password field, not null
);

-- Insert 5 users into the 'users' table if they do not already exist
INSERT IGNORE INTO users (email, password) VALUES
('ali@gmail.com', 'ali123'),
('afnan@gmail.com', 'afnan123'),
('omar@gmail.com', 'omar123'),
('lama@gmail.com', 'lama123'),
('abdullah@gmail.com', 'abdullah123');
