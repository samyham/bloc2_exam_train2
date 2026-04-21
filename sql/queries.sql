SELECT * FROM fact_stock_risk LIMIT 10;

SELECT stockout_risk, COUNT(*)
FROM fact_stock_risk
GROUP BY stockout_risk;

SELECT stockout_risk, AVG(sales_7d)
FROM fact_stock_risk
GROUP BY stockout_risk;
