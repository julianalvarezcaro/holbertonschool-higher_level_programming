-- Displays scores and record with that score
-- Score and number of records of that score
SELECT score, COUNT(*) as `number`
FROM second_table
GROUP BY score
ORDER BY score DESC;
