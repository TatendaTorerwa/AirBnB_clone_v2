-- Prepares the MySQL server for this project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
--GRANT SELECT privilege on perfomance_schema to hbnb_dev
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
--Flush privileges to apply the changes
FLUSH PRIVILIGESi;
