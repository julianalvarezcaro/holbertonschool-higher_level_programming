-- Displays all records
-- All records that have a name
SELECT score, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;
