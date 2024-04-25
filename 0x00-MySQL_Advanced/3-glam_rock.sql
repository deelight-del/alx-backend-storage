-- Writing sql queries that rank metal_bands
-- The implementation of the query that sortes metatl_bands that have Glam Style by longevity.
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
