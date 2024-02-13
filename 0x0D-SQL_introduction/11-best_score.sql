-- script that lists all records with a score >= 10

SELECT score, name FROM second_table 
ORDER BY score DESC
IF score >= 10;

