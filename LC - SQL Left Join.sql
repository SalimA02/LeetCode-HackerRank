SELECT A.id, A.name, B.order_date
FROM Customers A
LEFT JOIN Orders B
ON A.id = B.customer_id;
