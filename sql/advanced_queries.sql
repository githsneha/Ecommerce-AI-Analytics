-- =========================================
-- ADVANCED ANALYTICS QUERIES
-- =========================================

USE ecommerce_analytics;

-- =========================================
-- 1. TOP 10 CUSTOMERS BY REVENUE
-- =========================================

SELECT
    CustomerID,
    ROUND(SUM(Sales), 2) AS Total_Spending
FROM transactions
GROUP BY CustomerID
ORDER BY Total_Spending DESC
LIMIT 10;

-- =========================================
-- 2. HIGH VALUE CUSTOMERS
-- =========================================

SELECT
    CustomerID,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY CustomerID
HAVING Revenue > 10000
ORDER BY Revenue DESC;

-- =========================================
-- 3. MONTH WITH HIGHEST REVENUE
-- =========================================

SELECT
    Month,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Month
ORDER BY Revenue DESC
LIMIT 1;

-- =========================================
-- 4. COUNTRY-WISE ORDER COUNT
-- =========================================

SELECT
    Country,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM transactions
GROUP BY Country
ORDER BY Total_Orders DESC;

-- =========================================
-- 5. AVERAGE CUSTOMER SPENDING
-- =========================================

SELECT
    ROUND(
        AVG(customer_total),
        2
    ) AS Avg_Customer_Spending
FROM (
    SELECT
        CustomerID,
        SUM(Sales) AS customer_total
    FROM transactions
    GROUP BY CustomerID
) AS customer_spending;

-- =========================================
-- 6. PRODUCTS WITH HIGHEST UNIT PRICE
-- =========================================

SELECT
    Description,
    MAX(UnitPrice) AS Highest_UnitPrice
FROM transactions
GROUP BY Description
ORDER BY Highest_UnitPrice DESC
LIMIT 10;

-- =========================================
-- 7. DAILY REVENUE ANALYSIS
-- =========================================

SELECT
    Day,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Day
ORDER BY Day;

-- =========================================
-- 8. CUSTOMERS WITH MULTIPLE ORDERS
-- =========================================

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Order_Count
FROM transactions
GROUP BY CustomerID
HAVING Order_Count > 10
ORDER BY Order_Count DESC;

-- =========================================
-- 9. BEST SELLING PRODUCTS IN UK
-- =========================================

SELECT
    Description,
    SUM(Quantity) AS Quantity_Sold
FROM transactions
WHERE Country = 'United Kingdom'
GROUP BY Description
ORDER BY Quantity_Sold DESC
LIMIT 10;

-- =========================================
-- 10. REVENUE CONTRIBUTION BY COUNTRY
-- =========================================

SELECT
    Country,
    ROUND(
        SUM(Sales) * 100 /
        (SELECT SUM(Sales) FROM transactions),
        2
    ) AS Revenue_Percentage
FROM transactions
GROUP BY Country
ORDER BY Revenue_Percentage DESC;
