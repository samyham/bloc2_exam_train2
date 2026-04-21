CREATE TABLE fact_stock_risk (
    product_id TEXT,
    store_id TEXT,
    sales_7d INT,
    sales_30d INT,
    avg_rating FLOAT,
    stock_qty INT,
    category TEXT,
    region TEXT,
    stockout_risk INT
);
