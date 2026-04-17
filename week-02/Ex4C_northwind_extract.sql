-- Step 5: Employees
SELECT * 
FROM employees;
-- Margaret Peacock


-- Step 6: Products
SELECT * 
FROM products;
-- 77

-- Step 7: Categories
SELECT * 
FROM categories;
-- 8

-- Step 8: Top 50 Orders
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;