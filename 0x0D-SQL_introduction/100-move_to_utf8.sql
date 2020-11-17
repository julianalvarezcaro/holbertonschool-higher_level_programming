-- Write a script that converts hbtn_0c_0 database to UTF8
-- You need to convert all of the following to UTF8: database, table and fields
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table CHARACTER SET utf8;
ALTER TABLE first_table 
ALTER COLUMN `name` CHARACTER SET utf8;
