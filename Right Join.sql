SELECT A.id, A.name, B.order_date
FROM Customers A
RIGHT JOIN Orders B
ON A.id = B.customer_id;
