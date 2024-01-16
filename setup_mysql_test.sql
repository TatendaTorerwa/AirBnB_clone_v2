-- A script that prepares a MySQL server for the Project
-- Create database if it does not exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all, and SELECT  privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO  'hbnb_test'@'localhost';

-- Flush privileges to apply challenges
FLUSH PRIVILEGES;
