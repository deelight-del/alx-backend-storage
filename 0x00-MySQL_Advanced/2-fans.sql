-- This task groups each band by the number of fans.
-- This query groups the tables by "origin"
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans) DESC;
