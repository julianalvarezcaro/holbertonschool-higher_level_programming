-- Creates a database and a user
-- Database: hbtn_0d_2. User: user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

SET PASSWORD FOR 'user_0d_2'@'localhost' = PASSWORD('user_0d_2_pwd');

GRANT SELECT
ON hbtn_0d_2 . *
TO 'user_0d_2'@'localhost';
