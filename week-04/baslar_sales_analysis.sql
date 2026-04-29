-- total revenue for Gin categories
SELECT 
	MIN(date),
	MAX(date),
    SUM(total),
    category_name
FROM sales
WHERE category_name ILIKE '%gin%'
AND category_name NOT ILIKE '%rum%'
GROUP BY ROLLUP (category_name);
-- month by month revenue breakdown for Gin categories
SELECT 
    DATE_TRUNC('month', date) AS monthly,
    SUM(total) AS monthly_income
FROM sales
WHERE category_name ILIKE '%gin%'
    AND category_name NOT ILIKE '%rum%'
GROUP BY DATE_TRUNC('month', date)
ORDER BY monthly;
-- comparison of total revenue for Gin categories vs all other categories
SELECT 
   CASE 
		WHEN category_name ILIKE '%gin%' THEN 'GIN'
		WHEN category_name ILIKE '%rum%' THEN 'RUM'
		WHEN category_name ILIKE '%vodka%' THEN 'VODKA'
		WHEN category_name ILIKE '%whisk%' THEN 'WHISKEY'
		WHEN category_name ILIKE '%tequila%' THEN 'TEQUILA'
		WHEN category_name ILIKE '%LIQUE%' THEN 'LIQUEURS'
		ELSE 'OTHER'
		END AS category_group,
    SUM(total)
FROM sales
GROUP BY 1
ORDER BY SUM(total) DESC;
-- number of transactions per month and average transaction size by Gin sub-category
SELECT 
    DATE_TRUNC('month', date) AS monthly,
    AVG(total) AS monthly_income,
    category_name,
	COUNT(*) AS transaction_count
FROM sales
WHERE category_name ILIKE '%gin%'
    AND category_name NOT ILIKE '%rum%'
GROUP BY DATE_TRUNC('month', date),category_name
-- ranking of counties by Gin sales performance
SELECT
	county,
	SUM(total)
FROM sales
WHERE category_name ILIKE '%gin%'
    AND category_name NOT ILIKE '%rum%'
GROUP BY county
ORDER BY SUM(total) DESC;

-- gin sales per capita
SELECT
	sales.county,
 	SUM(total)/counties.population AS gin_per_capita,
	counties.population
FROM sales
JOIN counties
ON counties.county = sales.county
WHERE category_name ILIKE '%gin%'
AND category_name NOT ILIKE '%rum%'
GROUP BY sales.county,counties.population
HAVING counties.population > 60000
ORDER BY SUM(total)/ counties.population ASC
LIMIT 5;
	
-- Recommendations and Results: We can focus top performing categories and sales peak season in our data mostly.
-- Polk County generates the highest Gin revenue
-- Imported Dry Gins and American Dry Gins are the top performing categories
-- Sales peak in spring months (April-May)
-- Woodbury,Dubuque and Pottawattamie counties have more potential for sales

