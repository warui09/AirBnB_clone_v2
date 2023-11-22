-- This script prepares a MySQL server for the project
    -- A new user hbnb test is created if inexistent
    -- Special priviledges is given to the new user

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- create user
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost`
IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO `hbnb_test`@`localhost`;

-- grant select privileges on performance_shema
GRANT SELECT ON performance_schema.* TO `hbnb_test`@`localhost`;
