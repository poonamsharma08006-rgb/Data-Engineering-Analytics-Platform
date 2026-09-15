SELECT COUNT(*) orders,COUNT(DISTINCT customer_id) customers,ROUND(SUM(revenue),2) total_revenue,ROUND(AVG(revenue),2) average_order_value FROM sales;
SELECT DATE_TRUNC('month',order_date) month,ROUND(SUM(revenue),2) revenue FROM sales GROUP BY 1 ORDER BY 1;
SELECT region,COUNT(*) orders,ROUND(SUM(revenue),2) revenue,ROUND(AVG(revenue),2) avg_order_value FROM sales GROUP BY region ORDER BY revenue DESC;
SELECT product,SUM(quantity) units_sold,ROUND(SUM(revenue),2) revenue FROM sales GROUP BY product ORDER BY revenue DESC LIMIT 10;
SELECT customer_id,customer_name,COUNT(*) orders,ROUND(SUM(revenue),2) lifetime_revenue FROM sales GROUP BY customer_id,customer_name ORDER BY lifetime_revenue DESC;
