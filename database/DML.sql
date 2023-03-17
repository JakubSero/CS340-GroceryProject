
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

-- displaying Customers
SELECT customer_num AS Customer_Number, customer_first_name AS First_Name, customer_last_name AS Last_Name, customer_street AS Street_Address, customer_city AS City, customer_state AS State, customer_zip AS Zip_Code, customer_phone AS Phone_Number FROM Customers;


-- inserting a new customer
INSERT INTO Customers (customer_first_name, customer_last_name, customer_street, customer_city, customer_state, customer_zip, customer_phone) 
VALUES ('{customer_first_name}', '{customer_last_name}', '{customer_street}', '{customer_city}', '{customer_state}', '{customer_zip}', '{customer_phone}');
 
-- display Orders
SELECT Orders.order_num AS Order_Num, Orders.order_date AS Order_Date, Orders.card_number AS Card_Number, Orders.expiration_year AS Card_Expiration_Year, Orders.expiration_month AS Card_Expiration_Month, Orders.order_complete AS Completion_Status, Orders.pickup_or_ship AS PickedUp_Or_Shipped, Customers.customer_phone AS Customer_Phone FROM Orders JOIN Customers ON Orders.f_customer_num = Customers.customer_num;

-- add a new Order
INSERT INTO Orders (f_customer_num, order_date, card_number, expiration_month, expiration_year, order_complete, pickup_or_ship) VALUES (%s, '%s', '%s', %s, %s, %s, %s); % (request.form['customer_phone'], request.form['odate'], request.form['cardnum'], request.form['expmonth'], request.form['expyear'], request.form['complete?'], request.form['pors'])

-- dropdown for Customer fk in Order table form
SELECT Customers.customer_num, Customers.customer_phone AS Phone FROM Customers;

-- displaying Receipt
SELECT receipt_id AS Receipt_Id, purchase_date AS Purchase_Date, items_purchased AS Items_Purchased, price_paid AS Price, f_customer_num AS Customer_Number FROM Receipts;

-- inserting a new Receipt
INSERT INTO Receipts ( purchase_date, items_purchased, price_paid, f_customer_num) VALUES ('{purchase_date}', '{items_purchased}', {price_paid}, {f_customer_num});

-- dropdown for Customer fk in Receipts table form
SELECT Customers.customer_num, Customers.customer_phone AS Phone FROM Customers;

-- updating a Receipt
UPDATE Receipts SET purchase_date='{purchase_date}', items_purchased='{items_purchased}', price_paid={price_paid}, f_customer_num={f_customer_num} WHERE receipt_id={receipt_id};

-- Displaying Item
SELECT item_num AS Item_Number, item_type AS Item_Type, retail_price AS Retail_Price, quant_in_stock AS Quantity_Available FROM Items;

-- inserting a new item 
INSERT INTO Items (item_type, retail_price, quant_in_stock) VALUES ('{item_type}', {retail_price}, {quant_in_stock});

-- delete an Item
DELETE FROM Items WHERE item_num = '%s'; % request.form['item_num']
 
-- update an Item
UPDATE Items SET item_type='{iType}', retail_price={rPrice}, quant_in_stock={qStock} WHERE item_num={iNum};

-- Null Receipt/customer_fk id TODO: NEEDS TO BE NULL RECEIPT 


-- Order_Items
SELECT f_order_num AS Order_Number, f_item_num AS Item_Number FROM Order_Items;

-- Receipt_Items
SELECT f_receipt_id AS Receipt_Id, f_item_num AS Item_Number FROM Receipt_Items;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
