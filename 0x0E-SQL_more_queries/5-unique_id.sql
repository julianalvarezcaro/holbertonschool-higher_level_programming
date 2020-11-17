-- Creates a table
-- Fields id, name
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
);
