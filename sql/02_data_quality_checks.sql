USE ETLDataQuality;
GO

-- 1. Duplicate order IDs
SELECT order_id, COUNT(*) AS duplicate_count
FROM dbo.stg_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
GO

-- 2. Missing mandatory order dates
SELECT *
FROM dbo.stg_orders
WHERE order_date IS NULL;
GO

-- 3. Invalid/non-positive amounts
SELECT *
FROM dbo.stg_orders
WHERE amount IS NULL OR amount <= 0;
GO

-- 4. Referential integrity: orders without a matching customer
SELECT o.*
FROM dbo.stg_orders o
LEFT JOIN dbo.stg_customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO

-- 5. Allowed status values
SELECT *
FROM dbo.stg_orders
WHERE status NOT IN ('Completed', 'Pending', 'Cancelled');
GO

-- 6. Source-to-target row-count reconciliation
SELECT
    (SELECT COUNT(*) FROM dbo.stg_customers) AS customer_row_count,
    (SELECT COUNT(*) FROM dbo.stg_orders) AS order_row_count;
GO
