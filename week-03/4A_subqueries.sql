-- 1. What is the product name(s) of the most expensive products? 
SELECT ProductName
FROM Products
WHERE UnitPrice = ( SELECT MAX(UnitPrice)
					FROM Products);
                    
-- 2. What is the product name(s) and categories of the least expensive products? 
SELECT ProductName
FROM Products
WHERE UnitPrice = ( SELECT MIN(UnitPrice)
					FROM Products);

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT OrderID,ShipName,ShipAddress
FROM Orders
WHERE ShipVia = (SELECT ShipperID 
				 FROM Shippers
                 WHERE CompanyName ='Federal Shipping');
-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID
FROM `Order Details`
WHERE ProductID = (SELECT ProductID
				   FROM Products
                   WHERE ProductName = 'Sasquatch Ale');
-- 5. What is the name of the employee that sold order 10266?
SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = (SELECT EmployeeID
                    FROM Orders
					WHERE OrderID = 10266);
-- 6. What is the name of the customer that bought order 10266?
SELECT CompanyName
FROM Customers
WHERE CustomerID = (SELECT CustomerID
					FROM Orders
					WHERE OrderID = 10266);