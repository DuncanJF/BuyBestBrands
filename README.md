# Buy Best Brands

A mock  shopping app demonstrating Flask and SQL usage.

# Getting Started

## VS Code
You will need [Python Virtual Environments in VSCode](`https://code.visualstudio.com/docs/python/environments`)

## Install SQLite
Download SQLite tools for:
*  [Windows](https://www.sqlite.org/2024/sqlite-tools-win-x64-3450000.zip)
*  [MacOS](https://www.sqlite.org/2024/sqlite-tools-osx-x64-3450000.zip)
*  [Linux](https://www.sqlite.org/2024/sqlite-tools-linux-x64-3450000.zip)

You might also like to install SQLiteStudio:

[DIRECT](https://sqlitestudio.pl/)

*  [Windows](https://github.com/pawelsalawa/sqlitestudio/releases/download/3.4.4/SQLiteStudio-3.4.4-windows-x64-installer.exe)
*  [MacOS](https://github.com/pawelsalawa/sqlitestudio/releases/download/3.4.4/sqlitestudio-3.4.4.dmg)
*  [Linux](https://github.com/pawelsalawa/sqlitestudio/releases/download/3.4.4/sqlitestudio-3.4.4.tar.xz)


# Review

## Creating the database

Our shopping application needs to store information about customers, products etc.  We use a database for this.  We don't want to embed information about, for exampe, products in our code because that will be changing all of the time and we don't want to re-release the application every time we add or remove a product.  Similarly a key feature of a shopping cart is for customers to add and remove and eventually buy the contents.  A shopping cart is dynamic information which changes all the time and is therefore best kept in a datastore.

The file `schema_sql.txt` contains SQL statements to create a mock database for our application.
Open this file and review the SQL statements.  Take note of the primary keys and foreign key relationships.
These can, perhaps, be seen easier in this [ERD](schema_ERC.png ERD) of the schema.
Note the CREATE statements need to be executed in order so the table with a foreign key relationship is created after the target of that relationship.

The file `data_sql.txt` contains SQL statements to insert data into that mock database.

Open those fi

## The code
    TBD
## SQLite
    TBD
## Flask
    TBD

### Unit Testing

To run the flask unit tests wexdcute the following in the project top level directory:
```python -m pytest```

# Exercises
# References

## Flask
[Digital Ocean](https://www.digitalocean.com) provide some good tutorials which may help you get started with Flask.

Website and Flask Tutorials:
*  [Website Tutorial](https://www.digitalocean.com/community/tutorial-series/how-to-build-a-website-with-html)
*  [Flask Tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)


Relational Databases
[SQLite](https://www.sqlite.org/index.html) is a good relation database which keeps the database in a single file.  This makes it a very convenient database for learning relational principals and SQL.  See for example these [SQLlite tutorials](https://www.sqlitetutorial.net/)
