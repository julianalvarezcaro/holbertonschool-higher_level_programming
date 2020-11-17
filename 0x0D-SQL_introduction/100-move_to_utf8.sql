-- Write a script that converts hbtn_0c_0 database to UTF8
-- You need to convert all of the following to UTF8: database, table and fields
ALTER DATABASE hbtn_0c_0 
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY `name` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
