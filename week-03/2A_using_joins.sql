-- 1. Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.
SELECT ProductID,ProductName,UnitPrice,CategoryName
FROM Products
JOIN Categories
ON Products.CategoryID = Categories.CategoryID
ORDER BY CategoryName DESC, ProductName ASC;

-- 2. Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.
SELECT ProductID,ProductName,UnitPrice,CompanyName
FROM Products
JOIN Suppliers
ON Products.SupplierID=Suppliers.SupplierID
WHERE UnitPrice >= 75
ORDER BY ProductName DESC;

-- 3. Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.
SELECT ProductID,ProductName,UnitPrice,CategoryName,ContactName
FROM Products
JOIN Categories
ON Products.CategoryID = Categories.CategoryID
JOIN Suppliers
ON Products.SupplierID = Suppliers.SupplierID
ORDER BY ProductName DESC;


-- 4. Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.
SELECT OrderID,ShipName,ShipAddress,Shippers.CompanyName AS Shipper
FROM Orders
JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
JOIN Shippers
ON Orders.ShipVia = Shippers.ShipperID
WHERE ShipCountry LIKE '%Germany%'
ORDER BY Shippers.CompanyName ASC,ShipName ASC;

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.
SELECT ShipName, ShipAddress, Shippers.CompanyName AS Shipper, COUNT(DISTINCT OrderID) AS OrderCount
FROM Orders
JOIN Customers 
ON Orders.CustomerID = Customers.CustomerID
JOIN Shippers 
ON Orders.ShipVia = Shippers.ShipperID
WHERE ShipCountry LIKE '%Germany%'
GROUP BY ShipName, ShipAddress, Shippers.CompanyName
ORDER BY Shippers.CompanyName ASC, ShipName ASC;

-- 6. Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale.
SELECT Orders.OrderID,OrderDate,ShipName,ShipAddress
FROM Orders
JOIN `Order Details`
ON Orders.OrderID = `Order Details`.OrderID
JOIN Products
ON `Order Details`.ProductID = Products.ProductID
WHERE ProductName LIKE '%Sasquatch Ale%'