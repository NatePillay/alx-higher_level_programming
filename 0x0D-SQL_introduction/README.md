working with SQL

Connect to mysql server 
sudo mysql


mysql>
mysql> quit
Bye




Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

Heirarchical, network, relational, object orientated


e’ll compute the total for each order (the derived attribute shown in the UML Order class). We still need to add up order lines, but we need to group the totals for each order. We can do this with the GROUP BY clause. This time, the output will contain one row for every order, since the customerID and orderDate form the PK for Orders, not OrderLines. Notice that the SELECT clause and the GROUP BY clause contain exactly the same list of attributes, except for the calculation. In most cases, you will get an error message if you forget to do this.

SELECT custID, orderDate, SUM(unitSalePrice * quantity) AS total
FROM orderlines
GROUP BY custID, orderDate;

Order totals
		
5678	2003-07-14	11.95
9012	2003-07-14	45.15
5678	2003-07-18	18.00
5678	2003-07-20	57.65

=================================
Other frequently-used functions that work the same way as SUM include MIN (minimum value of those in the grouping), MAX (maximum value of those in the grouping, and AVG (average value of those in the grouping).


We can also count groups of rows with identical values in a column. In this case, COUNT will ignore NULL values in the column. Here, we’ll find out how many times each product has been ordered.
        SELECT prodname AS "product name", 
           COUNT(prodname) AS "times ordered"
        FROM products NATURAL JOIN orderlines
        GROUP BY prodname;

Product orders
	
Hammer, framing, 20 oz.	3
Saw, crosscut, 10 tpi	1
Screwdriver, Phillips #2, 6 inch	2
Pliers, needle-nose, 4 inch	1
A WHERE clause can be used as usual before the GROUP BY, to eliminate rows before the group function is executed. However, if we want to select output rows based on the results of the group function, the HAVING clause is used instead. For example, we could ask for only those products that have been sold more than once:
        SELECT prodname AS "product name", 
           COUNT(prodname) AS "times ordered"
        FROM products NATURAL JOIN orderlines
        GROUP BY prodname
        HAVING COUNT(prodname) > 1;


==============================
subqueries
Syntactically, all we have to do is to enclose the subquery in parenthses, in the same place where we would normally use a constant in the WHERE clause. We’ll include the zip code in the SELECT line to verify that the answer is what we want:


SELECT cFirstName, cLastName, cZipCode
FROM customers
WHERE cZipCode =        
          (SELECT cZipCode
           FROM customers
           WHERE cFirstName = 'Wayne' AND cLastName = 'Dick');


The result of the sub query will be used in the where clause of the main query



￼
====================================
Finding products that have a sale price greater then the average sale price 
        SELECT DISTINCT prodName, unitSalePrice
        FROM Products NATURAL JOIN OrderLines
        WHERE unitSalePrice >        
          (SELECT AVG(unitSalePrice)
           FROM OrderLines);

