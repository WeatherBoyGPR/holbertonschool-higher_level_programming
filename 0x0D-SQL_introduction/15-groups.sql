-- Will list total number of records with the same score in second_table
SELECT score, COUNT(SCORE) FROM second_table GROUP BY score HAVING COUNT(score) > 1;
