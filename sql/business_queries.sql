-- =========================================
-- BUSINESS ANALYTICS QUERIES
-- =========================================

USE ecommerce_analytics;

-- =========================================
-- 1. TOTAL REVENUE
-- =========================================

SELECT
    ROUND(SUM(Sales), 2) AS Total_Revenue
FROM transactions;

-- =========================================
-- 2. TOTAL ORDERS
-- =========================================

SELECT
    COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM transactions;

-- =========================================
-- 3. TOTAL CUSTOMERS
-- =========================================

SELECT
    COUNT(DISTINCT CustomerID) AS Total_Customers
FROM transactions;

-- =========================================
-- 4. AVERAGE ORDER VALUE
-- =========================================

SELECT
    ROUND(
        SUM(Sales) /
        COUNT(DISTINCT InvoiceNo),
        2
    ) AS Average_Order_Value
FROM transactions;

-- =========================================
-- 5. TOP 10 COUNTRIES BY REVENUE
-- =========================================

SELECT
    Country,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10;

-- =========================================
-- 6. TOP 10 PRODUCTS BY REVENUE
-- =========================================

SELECT
    Description,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;

-- =========================================
-- 7. TOP PRODUCTS BY QUANTITY SOLD
-- =========================================

SELECT
    Description,
    SUM(Quantity) AS Quantity_Sold
FROM transactions
GROUP BY Description
ORDER BY Quantity_Sold DESC
LIMIT 10;

-- =========================================
-- 8. MONTHLY REVENUE TREND
-- =========================================

SELECT
    Month,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Month
ORDER BY Month;

-- =========================================
-- 9. REVENUE BY WEEKDAY
-- =========================================

SELECT
    Weekday,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Weekday
ORDER BY Revenue DESC;

-- =========================================
-- 10. PEAK SHOPPING HOURS
-- =========================================

SELECT
    Hour,
    ROUND(SUM(Sales), 2) AS Revenue
FROM transactions
GROUP BY Hour
ORDER BY Revenue DESC;
