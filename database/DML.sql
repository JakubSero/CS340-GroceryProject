
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

-- add a new Customer
SELECT * FROM Customers;
INSERT INTO Customers (customer_first_name, customer_last_name, customer_street, customer_city, customer_state, customer_zip, customer_phone) VALUES 
(:fnameInput, :lnameInput, :streetInput, :cityInput, :stateInput, :zipInput, :phoneInput)

-- display Orders
SELECT Orders.order_num, Orders.order_date, Orders.card_number, Orders.expiration_year, Orders.expiration_month, Orders.order_complete, Orders.pickedup_or_shipped, Customers.customer_phone  FROM Orders
JOIN Customers ON Orders.f_customer_num = Customers.customer_num;

-- add a new Order
INSERT INTO Orders (order_date, card_number, expiration_year, expiration_month, order_complete, pickedup_or_shipped, f_customer_num) VALUES 
(:oDateInput, :cardInput, :expyInput, :expmInput, :comInput, :shipInput, :fcustInput)

-- dropdown for Customer fk in Order table form
SELECT Customers.customer_phone AS Phone
FROM Customers;

-- add a new Receipt
SELECT * FROM Receipt;
INSERT INTO Receipt (f_customer_num, purchase_date, items_purchased, price_paid) VALUES 
(:fcustInput, :pDateInput, :iPurchInput, :pPaidInput)

-- dropdown for Customer fk in Receipts table form
SELECT Customers.customer_phone AS Phone
FROM Customers;

-- add a new Item
SELECT * FROM Item; 
INSERT INTO Item  (item_num, item_type, retail_price, quant_in_stock) VALUES 
(:iNumInput, :iTypeInput, :rPriceInput, :stockInput)

-- delete an Item
DELETE FROM Item WHERE item_num = :iNumInput
 
-- update an Item
UPDATE Item SET item_num = :iNumInput, item_type= :iTypeInput, retail_price 
= :rPriceInput, quant_in_stock = :stockInput WHERE 
item_num = :iNumInput

-- Null item id 
UPDATE Receipts SET f_customer_num = NULL WHERE f_customer_num = :f_customer_num;

-- Order_Items
SELECT * FROM Order_Items;

-- Receipt_Items
SELECT * FROM Receipt_Items;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
