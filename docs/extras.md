# Extras

## Creating the database

The shopping application needs to store information about customers, products etc.  We use a database for this.  We don't want to embed information that will change, for exampe, products in our code.  For example we don't want to re-release the application every time we add or remove a product.  Similarly a key feature of a shopping cart is for customers to add and remove and eventually buy the contents.  A shopping cart is dynamic information which changes all the time and is therefore best kept in a datastore.

We are using a ready made copy of the database.

The file `schema_sql.txt` contains SQL statements usede to create a mock database we copied earlier.  The file `data_sql.txt` contains SQL statements to insert data into that mock database.
Open the `schema_sql.txt` file and review the SQL statements.  Take note of the primary keys and foreign key relationships.
The schame can also be seen in the Entity-Releationship Diagram.  This diagram was genenrated from the database using the [DBeaver](https://dbeaver.io/) application.  The web application [https://app.diagrams.net/](https://app.diagrams.net/) can be used to create ERD diagrams during the design phase before the database has been created.

![ERD](schema_ERC.png Database ERD) of the schema.

Note the CREATE statements need to be executed in order for the table with a foreign key relationship is created after the target of that relationship.