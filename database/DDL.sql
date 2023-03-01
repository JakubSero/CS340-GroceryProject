SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT=0;

-- Customers
CREATE OR REPLACE TABLE Customers (
  customer_num INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
  customer_first_name VARCHAR(45) NOT NULL,
  customer_last_name VARCHAR(45) NOT NULL,
  customer_street VARCHAR(45) NOT NULL,
  customer_city VARCHAR(45) NOT NULL,
  customer_state VARCHAR(2) NOT NULL,
  customer_zip VARCHAR(10) NOT NULL,
  customer_phone VARCHAR(45) NOT NULL,
  PRIMARY KEY (customer_num));

-- Purchases
CREATE OR REPLACE TABLE Receipts (
  receipt_id INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
  purchase_date DATE NOT NULL,
  items_purchased MEDIUMTEXT NOT NULL,
  price_paid decimal(19,2) NOT NULL,
  f_customer_num INT(11),
  PRIMARY KEY (receipt_id),
  FOREIGN KEY (f_customer_num) REFERENCES Customers(customer_num) ON DELETE SET NULL
);

-- Orders
CREATE OR REPLACE TABLE Orders (
  order_num INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
  order_date DATE NOT NULL,
  card_number VARCHAR(16) NOT NULL UNIQUE,
  expiration_month SMALLINT NOT NULL,
  expiration_year SMALLINT NOT NULL,
  order_complete TINYINT UNSIGNED NOT NULL DEFAULT 0,
  pickup_or_ship TINYINT UNSIGNED NOT NULL DEFAULT 0,
  f_customer_num INT(11) NOT NULL,
  PRIMARY KEY (order_num),
  FOREIGN KEY (f_customer_num)
  REFERENCES Customers(customer_num) ON DELETE CASCADE);

-- Items 
CREATE OR REPLACE TABLE Items (
  item_num INT(11) NOT NULL UNIQUE AUTO_INCREMENT,
  item_type VARCHAR(45) NOT NULL,
  retail_price DECIMAL(19,2) NOT NULL,
  quant_in_stock INT(11) NOT NULL,
  PRIMARY KEY (item_num));

-- Purchased_Items
CREATE OR REPLACE TABLE Receipt_Items (
  f_receipt_id INT(11) NOT NULL,
  f_item_num INT(11) NOT NULL,
  FOREIGN KEY (f_receipt_id) 
  REFERENCES Receipts(receipt_id) ON DELETE CASCADE,
  FOREIGN KEY (f_item_num)
  REFERENCES Items(item_num) ON DELETE CASCADE);


-- Ordered_Items
CREATE OR REPLACE TABLE Order_Items (
  f_order_num INT(11) NOT NULL,
  f_item_num INT(11) NOT NULL,
  FOREIGN KEY (f_order_num)
  REFERENCES Orders(order_num) ON DELETE CASCADE,
  FOREIGN KEY (f_item_num)
  REFERENCES Items (item_num) ON DELETE CASCADE);

-- INSERTING DATA --
-- Inserts data into resepective tables --

INSERT INTO Customers (customer_first_name, customer_last_name, customer_street, customer_city, customer_state, customer_zip, customer_phone) 
VALUES ('Jeffery', 'Zoll', '3946 Stratford Drive', 'Waipahu', 'HI', '96797', '808-205-3645'),
 ('Vera', 'Hughes', '147 Oak Street', 'Syracuse', 'NY', '13022', '315-728-4964'),
 ('William', 'Lewis', '4409 Apple Lane', 'Holdrege', 'NE', '68949', '308-995-8712');

INSERT INTO Receipts (purchase_date, items_purchased, price_paid, f_customer_num) 
VALUES ('2008-04-10', 'Apple', '63.25', '1'), 
('2008-08-10', 'Bananas', '666.66', '2'), 
('2008-10-10', 'Honda Civic', '568.25', '3');

INSERT INTO Orders (f_customer_num, order_num, order_date, card_number, expiration_month, expiration_year, order_complete, pickup_or_ship) 
VALUES 
('1', '253', '2008-04-10', '4903148113428004', '03', '2025', '1', '1'), 
('2', '987', '2008-08-10', '4716929223093912', '05', '2026', '0', '0'), 
('3', '124', '2008-10-10', '4556323321629897', '07', '2024', '1', '1');

INSERT INTO Items (item_num, item_type, retail_price, quant_in_stock) 
VALUES 
('4568', 'Fruit', '63.25', '100'), 
('9874', 'Fruit', '666.66', '200'), 
('32154', 'Vehicle', '568.25', '300');

INSERT INTO Receipt_Items (f_receipt_id, f_item_num) 
VALUES 
('1', '4568'), 
('2', '9874'), 
('3', '32154');

INSERT INTO Order_Items (f_order_num, f_item_num) 
VALUES 
('253', '4568'), 
('987', '9874'), 
('124', '32154');

SET FOREIGN_KEY_CHECKS = 1;
COMMIT;
