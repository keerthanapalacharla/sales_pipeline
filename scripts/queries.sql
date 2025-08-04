-- Show all records
SELECT * FROM sales;

-- Total sales by region
SELECT Region, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region;

-- Top 3 highest sales transactions
SELECT * FROM sales
ORDER BY Sales DESC
LIMIT 3;

-- Total sales by product category
SELECT Category, SUM(Sales) AS CategorySales
FROM sales
GROUP BY Category;
