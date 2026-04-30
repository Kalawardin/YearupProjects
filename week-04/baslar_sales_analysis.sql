-- 1. Total revenue for Gin categories
SELECT 
	MIN(date),
	MAX(date),
    SUM(total),
    category_name
FROM sales
WHERE category_name ILIKE '%gin%'
AND category_name NOT ILIKE '%rum%'
GROUP BY ROLLUP (category_name);
-- 2.month by month revenue breakdown for Gin categories
SELECT 
    DATE_TRUNC('month', date) AS monthly,
    SUM(total) AS monthly_income
FROM sales
WHERE category_name ILIKE '%gin%'
    AND category_name NOT ILIKE '%rum%'
GROUP BY DATE_TRUNC('month', date)
ORDER BY monthly;
-- 3. Comparison of total revenue for Gin categories vs all other categories
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
-- 4.Number of transactions per month and average transaction size by Gin sub-category
SELECT 
    DATE_TRUNC('month', date) AS monthly,
    AVG(total) AS monthly_income,
    category_name,
	COUNT(*) AS transaction_count
FROM sales
WHERE category_name ILIKE '%gin%'
    AND category_name NOT ILIKE '%rum%'
GROUP BY DATE_TRUNC('month', date),category_name
-- 5.Ranking of counties by Gin sales performance
SELECT
	county,
	SUM(total)
FROM sales
WHERE category_name ILIKE '%gin%'
    AND category_name NOT ILIKE '%rum%'
GROUP BY county
ORDER BY SUM(total) DESC;

-- 6.Gin sales per capita
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

-- 7. Top 5 Vendors supplying Gin by total revenue
SELECT
    vendor,
    SUM(total) AS total_revenue,
    SUM(bottle_qty) AS total_bottles_sold
FROM sales
WHERE category_name ILIKE '%gin%'
  AND category_name NOT ILIKE '%rum%'
GROUP BY vendor
ORDER BY total_revenue DESC
LIMIT 5;

-- 8. Top 10 Stores by Gin sales revenue
SELECT
    store AS store_id,
    SUM(total) AS total_revenue,
    COUNT(*) AS transaction_count
FROM sales
WHERE category_name ILIKE '%gin%'
  AND category_name NOT ILIKE '%rum%'
GROUP BY store
ORDER BY total_revenue DESC
LIMIT 10;

-- 9. Estimated Profit Margin per Gin Category
SELECT
    category_name,
    AVG(btl_price::numeric - state_btl_cost::numeric) AS avg_profit_per_bottle,
    SUM((btl_price::numeric - state_btl_cost::numeric) * bottle_qty) AS total_estimated_profit
FROM sales
WHERE category_name ILIKE '%gin%'
  AND category_name NOT ILIKE '%rum%'
GROUP BY category_name
ORDER BY total_estimated_profit DESC;

-- 10. Top 5 Most Popular Specific Gin Items (by total bottles sold)
SELECT
    item,
    description,
    SUM(bottle_qty) AS total_bottles_sold,
    SUM(total) AS total_revenue
FROM sales
WHERE category_name ILIKE '%gin%'
  AND category_name NOT ILIKE '%rum%'
GROUP BY item, description
ORDER BY total_bottles_sold DESC
LIMIT 5;

-- 11. List of high-value Gin transactions (above the average Gin transaction size)
SELECT
    date,
    store,
    description,
    bottle_qty,
    total
FROM sales
WHERE category_name ILIKE '%gin%'
  AND category_name NOT ILIKE '%rum%'
  AND total > (
      SELECT AVG(total)
      FROM sales
      WHERE category_name ILIKE '%gin%'
        AND category_name NOT ILIKE '%rum%'
  )
ORDER BY total DESC
LIMIT 15;

-- 12. Yearly revenue breakdown for Gin to observe macro growth/decline
SELECT
    EXTRACT(YEAR FROM date) AS sales_year,
    SUM(total) AS yearly_revenue,
    SUM(bottle_qty) AS yearly_bottles,
    COUNT(*) AS total_transactions
FROM sales
WHERE category_name ILIKE '%gin%'
  AND category_name NOT ILIKE '%rum%'
GROUP BY EXTRACT(YEAR FROM date)
ORDER BY sales_year ASC;


