-- This SQL script select band_name, and lifespan column ehich is difference
SELECT band_name, (IFNULL(split, '2020') - forward) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
