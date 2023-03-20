# CS340-GroceryProject

This project has been guided by the flask guide and is where the basic skeletal structure 
off this app.py is from. db_connector and db_credentials in the database directory are copied from the guide, 
as well as the J2 pages in the template directory being based on the guide's J2 pages.

Changes include:
1) The db_connection points in our code. The original flask guide had one connection at the start of the app but
this ended up breaking our page after a few minutes of inactivity.   
2) Fleshed out routes that were initially based on the guide and then modified to suit our needs.
3) J2 pages at first copied from the guide below and then modified slightly to accomodate our data needs. The 
   JS function at the top of the J2 pages helped a lot but again were slighly modified in some cases as we needed
   to pass separate data into the form and adding on to that function seemed like a clean way to do so.

Flask guide referenced: https://github.com/osu-cs340-ecampus/flask-starter-app

Made by Eddi F. Miranda - Perez and Jakub Kowalski for CS 340.
