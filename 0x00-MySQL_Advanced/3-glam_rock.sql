-- Lists all bands with Glam rock as their main style
-- ranked by their longevity
-- Use attributes formed and split for computing lifespan
-- Column names: band_name and lifespan (in years)
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_band
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
