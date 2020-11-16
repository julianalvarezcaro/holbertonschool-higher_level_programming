-- Lists all records with score >= 10
-- Selects them from second_table from the given database
SELECT score, `name`
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
