-- Prepares a MySQL server for the project

-- Creates a database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db hbn_dev
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- GRANT SELECT privilege on perfomance_schema to hbnb_dev
GRANT SELECT ON `perfomance_schema`.* TO 'hbnb_dev'@'localhost';

