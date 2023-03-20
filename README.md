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
   
Changes for all template files can be summarized as follows:

We used the code provided to us on 02/16/2023 during the Week Six module exploration on Web Application Technology to handle displaying, hiding, and implementing CRUD operations. For hiding and displaying different CRUD functionalities, we used the head, link, script, and function provided in the file for our project but made significant changes to suit our specific requirements, especially with regards to naming conventions using the Flask guide provided to us.

For instance, we added "receipt_id", "day", "items", "price", and "fk" in the updateReceipt function to define our values and make appropriate connections with our app.py file. Each template file implemented different CRUD functionalities, so each template looks different in terms of naming conventions and code length. For example, for receipts, we only used the insert and update functions from the showform(dowhat) function.

Furthermore, we utilized the code that was given to generate an HTML table with a header row that displays the keys of a list of person dictionaries. We modified this code to use a header row that displays the column names of a list of receipts for our receipt.j2 file. The code contains an "Edit" button for each receipt that allows the user to update the purchase date, items purchased, price, and customer number if available. The table cells are populated with the corresponding values of each receipt. Each template has an identical table as the receipts table.

Lastly, any changes made to other template Jinja files were only applied to naming conventions and not in the logic used. The changes were made before 03/09/2023.
When it came to implementing the CRUD operations outside of the function found in the <head>, we again used a combination of the code provided to us in the Week Six module exploration on Web Application Technology and the Flask guide. Each template page contains identical logic for implementing the chosen CRUD operations apart from those that contain a drop-down menu. The dropdown menu logic was not taken from any other source.
   
For example, receipts differ from the people.html file in that people.html has three div elements with unique IDs to contain the forms for adding, updating, and deleting a person. The receipts block of code has two div elements with unique IDs to contain the forms for adding and updating a receipt. Identical changes occurred for customer, items, and orders, where they differed from the original code provided by the people.html only by the unique IDs and the number of CRUD operations they implement.


Flask guide referenced: https://github.com/osu-cs340-ecampus/flask-starter-app

Made by Eddi F. Miranda - Perez and Jakub Kowalski for CS 340.
