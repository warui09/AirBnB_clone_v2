-- Creates the database if non existent
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates user if non existent
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db to the  user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
