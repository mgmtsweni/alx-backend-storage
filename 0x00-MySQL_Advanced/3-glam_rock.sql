-- Lists all bands with Glam rock as their main style
-- ranked by their longevity
-- Use attributes formed and split for computing lifespan
-- Column names: band_name and lifespan (in years)
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
