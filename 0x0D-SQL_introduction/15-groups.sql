-- select the number of record with same score and create column for it 
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY score DESC
