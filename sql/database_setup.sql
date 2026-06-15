-- =========================================
-- E-COMMERCE ANALYTICS PROJECT
-- DATABASE SETUP
-- =========================================

-- Create Database
CREATE DATABASE ecommerce_analytics;

-- Use Database
USE ecommerce_analytics;

-- =========================================
-- CREATE TRANSACTIONS TABLE
-- =========================================

CREATE TABLE transactions (

    InvoiceNo VARCHAR(20),

    StockCode VARCHAR(20),

    Description TEXT,

    Quantity INT,

    InvoiceDate DATETIME,

    UnitPrice FLOAT,

    CustomerID INT,

    Country VARCHAR(100),

    Sales FLOAT,

    Year INT,

    Month INT,

    Day INT,

    Hour INT,

    Weekday VARCHAR(20)

);

-- =========================================
-- VERIFY TABLE
-- =========================================

DESCRIBE transactions;
