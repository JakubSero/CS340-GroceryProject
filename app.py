from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_kowaljak'
app.config['MYSQL_PASSWORD'] = '2811' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_kowaljak'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)

db_connection = db.connect_to_database()

# Routes
@app.route('/')
def root():
	return render_template("index.html")	


@app.route('/customers')
def customers():
	query = "SELECT * FROM Customers;"
	cursor = db.execute_query(db_connection=db_connection, query=query)
	results = cursor.fetchall()
	return render_template("customers.j2", Customers=results)

@app.route('/orders', methods=["GET"])
def orders():
    if request.method == "GET":
        query = "SELECT Orders.order_num, Orders.order_date, Orders.card_number, Orders.expiration_year, Orders.expiration_month, Orders.order_complete, Orders.pickup_or_ship, Customers.customer_phone FROM Orders JOIN Customers ON Orders.f_customer_num = Customers.customer_num;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT Customers.customer_num, Customers.customer_phone AS Phone FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        results2 = cursor.fetchall()
        return render_template("orders.j2", Orders=results, Dropdown=results2)

@app.route('/insert-order', methods=["GET", "POST"])        
def insert_order():        
        query = "INSERT INTO Orders (f_customer_num, order_date, card_number, expiration_month, expiration_year, order_complete, pickup_or_ship) VALUES (%s, '%s', '%s', %s, %s, %s, %s);" % (request.form['customer_phone'], request.form['odate'], request.form['cardnum'], request.form['expmonth'], request.form['expyear'], request.form['complete?'], request.form['pors'])  
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return redirect("/orders")

# @app.route('/receipts')
# def customers():
#     return render_template("receipts.html")

@app.route('/items', methods=["POST", "GET", "UPDATE"])
def items():
    if request.method == "GET":
        query = "SELECT * FROM Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("items.j2", Items=results)

@app.route("/delete_item", methods=["POST", "GET", "DELETE"])
def delete_item():
    #pre_query = "SET foreign_key_checks = 0;"
    query = "DELETE FROM Items WHERE item_num = '%s';" % request.form['item_num']
    #after = "SET foreign_key_checks = 1;"
    #check = db.execute_query(db_connection=db_connection, query=pre_query)
    cur = db.execute_query(db_connection=db_connection, query=query)
    #check2 = db.execute_query(db_connection=db_connection, query=after)
    return redirect("/items")

@app.route('/insert_item', methods=["POST"])
def insert_item():
    item_num = request.form["iNum"]
    item_type = request.form["iType"]
    retail_price = request.form["rPrice"]
    quant_in_stock = request.form["qStock"]
    query = f"INSERT INTO Items (item_num, item_type, retail_price, quant_in_stock) VALUES ({item_num}, '{item_type}', {retail_price}, {quant_in_stock});"

    try:
        db.execute_query(db_connection=db_connection, query=query)
        return redirect("/items")
    except Exception as e:
        db_connection.rollback()
        return "Error creating item: " + str(e)

@app.route('/edit_item', methods=['POST'])
def edit_people():
    iNum = request.form['iNum']
    iType = request.form['iType']
    rPrice = request.form['rPrice']
    qStock = request.form['qStock']
    query = f"UPDATE Items SET item_type='{iType}', retail_price={rPrice}, quant_in_stock={qStock} WHERE item_num={iNum};"
    try:
        db.execute_query(db_connection=db_connection, query=query)
        return redirect('/items')
    except Exception as e:
        db_connection.rollback()
        return "Error updating item: " + str(e)

@app.route('/order_items', methods=['GET'])
def order_items():
    if request.method == "GET":
        query = "SELECT * FROM Order_Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
    return render_template("order_items.j2", O_I=results)

@app.route('/receipt_items', methods=['GET'])
def receipt_items():
    if request.method == "GET":
        query = "SELECT * FROM Receipt_Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
    return render_template("receipt_items.j2", R_I=results)

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9340))
    #Start the app on port 3000, it will be different once hosted
    app.run(host="flip3.engr.oregonstate.edu", port=9340, debug=False)
