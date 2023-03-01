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
	#query = "SELECT * FROM Customers;"
	#query1 = "DROP TABLE IF EXISTS diagnostic;"
	#query2 = "CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);"
	#query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!");'
	query4 = "SELECT * FROM Customers;"
	cur = mysql.connection.cursor()
	#cur.execute(query1)
	#cur.execute(query2)
	#cur.execute(query3)
	cur.execute(query4)
	results = cur.fetchall()
	return "<h1> MYSQL Results" + str(results)
	#return render_template("customers.html")	


@app.route('/customers')
def customers():
	query = "SELECT * FROM Customers;"
	cursor = db.execute_query(db_connection=db_connection, query=query)
	results = json.dumps(cursor.fetchall())
	return results

#@app.route('/orders')
#def orders():
#	return render_template("orders.html")

# @app.route('/receipts')
# def customers():
#     return render_template("receipts.html")

# @app.route('/items')
# def customers():
#     return render_template("items.html")

# @app.route('/order_items')
# def customers():
#     return render_template("order_items.html")

# @app.route('/receipt_items')
# def customers():
#     return render_template("receipt_items.html")


# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9340))
    #Start the app on port 3000, it will be different once hosted
    app.run(host="flip3.engr.oregonstate.edu", port=9340, debug=False)
