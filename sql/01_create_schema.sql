CREATE DATABASE ETLDataQuality;
GO

USE ETLDataQuality;
GO

IF OBJECT_ID('dbo.stg_customers','U') IS NOT NULL DROP TABLE dbo.stg_customers;
IF OBJECT_ID('dbo.stg_orders','U') IS NOT NULL DROP TABLE dbo.stg_orders;
GO

CREATE TABLE dbo.stg_customers (
    customer_id INT NOT NULL,
    customer_name VARCHAR(150) NULL,
    email VARCHAR(255) NULL,
    city VARCHAR(100) NULL,
    province CHAR(2) NULL
);
GO

CREATE TABLE dbo.stg_orders (
    order_id INT NOT NULL,
    customer_id INT NULL,
    order_date DATE NULL,
    status VARCHAR(30) NULL,
    amount DECIMAL(12,2) NULL
);
GO
