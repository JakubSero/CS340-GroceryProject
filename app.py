from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

app = Flask(__name__)

# Routes
@app.route('/')
def root():
	return render_template("index.html")	

@app.route('/customers')
def customers():
        db_connection = db.connect_to_database()

        query = "SELECT customer_num AS 'Customer Number', customer_first_name AS 'First Name', customer_last_name AS 'Last Name', customer_street AS 'Street Address', customer_city AS City, customer_state AS State, customer_zip AS 'Zip Code', customer_phone AS 'Phone Number' FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        cursor.close()
        db_connection.close()
        return render_template("customers.j2", Customers=results)

@app.route('/insert_customer', methods=["POST"])
def create_customer():
    db_connection = db.connect_to_database()

    customer_num = request.form["customer_num"]
    customer_first_name = request.form["customer_first_name"]
    customer_last_name = request.form["customer_last_name"]
    customer_street = request.form["customer_street"]
    customer_city = request.form["customer_city"]
    customer_state = request.form["customer_state"]
    customer_zip = request.form["customer_zip"]
    customer_phone = request.form["customer_phone"]

    query = f"INSERT INTO Customers (customer_first_name, customer_last_name, customer_street, customer_city, customer_state, customer_zip, customer_phone) VALUES ('{customer_first_name}', '{customer_last_name}', '{customer_street}', '{customer_city}', '{customer_state}', '{customer_zip}', '{customer_phone}');"
    try:
        db.execute_query(db_connection=db_connection, query=query)
        db_connection.close()
        return redirect("/customers")
    except Exception as e:
        db_connection.rollback()
        db_connection.close()

        return "Error creating Customer: " + str(e)

@app.route('/orders', methods=["GET"])
def orders():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT Orders.order_num AS 'Order Num', Orders.order_date AS 'Order Date', Orders.card_number AS 'Card Number', Orders.expiration_year AS 'Card Expiration Year', Orders.expiration_month AS 'Card Expiration Month', Orders.order_complete AS 'Completion Status', Orders.pickup_or_ship AS 'PickedUp Or Shipped', Customers.customer_phone AS 'Customer Phone' FROM Orders JOIN Customers ON Orders.f_customer_num = Customers.customer_num;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall() 
        cursor.close()
        
        query2 = "SELECT Customers.customer_num, Customers.customer_phone AS Phone FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()
        cursor.close()
        db_connection.close()

        return render_template("orders.j2", Orders=results, Dropdown=results2)

@app.route('/insert-order', methods=["GET", "POST"])        
def insert_order():
        db_connection = db.connect_to_database()        
        query = "INSERT INTO Orders (f_customer_num, order_date, card_number, expiration_month, expiration_year, order_complete, pickup_or_ship) VALUES (%s, '%s', '%s', %s, %s, %s, %s);" % (request.form['customer_phone'], request.form['odate'], request.form['cardnum'], request.form['expmonth'], request.form['expyear'], request.form['complete?'], request.form['pors'])  
        cursor = db.execute_query(db_connection=db_connection, query=query)
        # results = cursor.fetchall()
        cursor.close()
        db_connection.close()

        return redirect("/orders")

@app.route('/receipts', methods=["GET"])
def receipts():
    try:
        if request.method == "GET":
            db_connection = db.connect_to_database()
            query = "SELECT receipt_id AS 'Receipt Id', purchase_date AS 'Purchase Date', items_purchased AS 'Items Purchased', price_paid AS 'Price', f_customer_num AS 'Customer Number' FROM Receipts;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = cursor.fetchall()
            cursor.close()
            
            query2 = "SELECT customer_num, customer_phone AS Phone FROM Customers;"
            cursor = db.execute_query(db_connection=db_connection, query=query2)
            results2 = cursor.fetchall()
            cursor.close()
            db_connection.close()

            return render_template("/receipts.j2", Receipts=results, Dropdown=results2)
    except Exception as e:
        print("Error executing SQL query: ", e)
        return "Error executing SQL query: " + str(e)

@app.route('/insert_receipt', methods=["POST", "GET"])
def create_receipt():
    db_connection = db.connect_to_database()
    receipt_id = request.form["receipt_id"]
    purchase_date = request.form["purchase_date"]
    items_purchased = request.form["items_purchased"]
    price_paid = request.form["price_paid"]
    f_customer_num = request.form["customer_phone"]
    query = f"INSERT INTO Receipts ( purchase_date, items_purchased, price_paid, f_customer_num) VALUES ('{purchase_date}', '{items_purchased}', {price_paid}, {f_customer_num});"

    try:
        db.execute_query(db_connection=db_connection, query=query)
        db_connection.close()

        return redirect("/receipts")
    except Exception as e:
        db_connection.rollback()
        db_connection.close()

        return "Error creating receipt: " + str(e)


@app.route('/edit_receipt', methods=['POST'])
def edit_receipt():
    db_connection = db.connect_to_database()
    receipt_id = request.form["receipt_id"]
    purchase_date = request.form["purchase_date"]
    items_purchased = request.form["items_purchased"]
    price_paid = request.form["price_paid"]
    f_customer_num = request.form["customer_phone"]
    query = f"UPDATE Receipts SET purchase_date='{purchase_date}', items_purchased='{items_purchased}', price_paid={price_paid}, f_customer_num={f_customer_num} WHERE receipt_id={receipt_id};"
    try:
        db.execute_query(db_connection=db_connection, query=query)
        # return query
        db_connection.close()

        return redirect('/receipts')
    except Exception as e:
        db_connection.rollback()
        db_connection.close()

        return "Error updating receipt: " + str(e)

@app.route('/items', methods=["POST", "GET", "UPDATE"])
def items():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT item_num AS 'Item Number', item_type AS 'Item Type', retail_price AS 'Retail Price', quant_in_stock AS 'Quantity Available' FROM Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        cursor.close()
        db_connection.close()

        return render_template("items.j2", Items=results)

@app.route("/delete_item", methods=["POST", "GET", "DELETE"])
def delete_item():
    db_connection = db.connect_to_database()
    query = "DELETE FROM Items WHERE item_num = '%s';" % request.form['item_num']
    cur = db.execute_query(db_connection=db_connection, query=query)
    cur.close()
    db_connection.close()

    return redirect("/items")

@app.route('/insert_item', methods=["POST"])
def insert_item():
    db_connection = db.connect_to_database()
    # item_num = request.form["iNum"]
    item_type = request.form["iType"]
    retail_price = request.form["rPrice"]
    quant_in_stock = request.form["qStock"]
    query = f"INSERT INTO Items (item_type, retail_price, quant_in_stock) VALUES ('{item_type}', {retail_price}, {quant_in_stock});"

    try:
        db.execute_query(db_connection=db_connection, query=query)
        db_connection.close()

        return redirect("/items")
    except Exception as e:
        db_connection.rollback()
        db_connection.close()

        return "Error creating item: " + str(e)

@app.route('/edit_item', methods=['POST'])
def edit_people():
    db_connection = db.connect_to_database()
    iNum = request.form['iNum']
    iType = request.form['iType']
    rPrice = request.form['rPrice']
    qStock = request.form['qStock']
    query = f"UPDATE Items SET item_type='{iType}', retail_price={rPrice}, quant_in_stock={qStock} WHERE item_num={iNum};"
    try:
        db.execute_query(db_connection=db_connection, query=query)
        db_connection.close()

        return redirect('/items')
    except Exception as e:
        db_connection.rollback()
        db_connection.close()

        return "Error updating item: " + str(e)

@app.route('/order_items', methods=['GET'])
def order_items():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT f_order_num AS 'Order Number', f_item_num AS 'Item Number' FROM Order_Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        cursor.close()
        
        db_connection = db.connect_to_database()
        query2 = "SELECT item_num FROM Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()
        cursor.close()

        db_connection = db.connect_to_database()
        query3 = "SELECT order_num FROM Orders;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        results3 = cursor.fetchall()
        cursor.close()
        db_connection.close()

    return render_template("order_items.j2", O_I=results, Dropdown=results2, Dropdown2=results3)

@app.route('/insert_order_item', methods=["POST"])
def insert_order_item():
    db_connection = db.connect_to_database()
    order = request.form["order"]
    item = request.form["item"]
    query = f"INSERT INTO Order_Items (f_order_num, f_item_num) VALUES ({order}, {item});"

    try:
        db.execute_query(db_connection=db_connection, query=query)
        db_connection.close()

        return redirect("/order_items")
    except Exception as e:
        db_connection.rollback()
        db_connection.close()

        return "Error creating item: " + str(e)

@app.route('/receipt_items', methods=['GET'])
def receipt_items():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT f_receipt_id AS 'Receipt Id', f_item_num AS 'Item Number' FROM Receipt_Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        cursor.close()
        db_connection.close()

    return render_template("receipt_items.j2", R_I=results)

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9340))
    #Start the app on port 3000, it will be different once hosted
    app.run(host="flip3.engr.oregonstate.edu", port=9340, debug=False)
