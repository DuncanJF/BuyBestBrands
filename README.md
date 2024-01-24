# Buy Best Brands

A mock shopping app demonstrating Flask and SQL usage.

# Getting Started

## VS Code

*  You must install the VS Code [python extension](https://code.visualstudio.com/docs/languages/python).
*  You must install the [Python Virtual Environments in VSCode](https://code.visualstudio.com/docs/python/environments).

## Copy the Code

You must have a copy of the code on your local machine.
Either clone the repository or download a ZIP archive of the code.

To clone it use the VScode source control tools with the repository URL `https://github.com/DuncanJF/BuyBestBrands.git`.
You will be asked for a target directory.  After the clone is complete you should have a folder `BuyBestBrands` in the target directory.
Open this directory in VScode before proceeding to the next steps.


To download a ZIP archive go to [the repository](https://github.com/DuncanJF/BuyBestBrands)
![screenshot](images/github_screenshot.png).  Select the green `code` button.  Then select the `Download ZIP` option at the bottom of the dropdown menu.  This will download a file `BuyBestBrands-main.zip` to your local disk.  Move the file `BuyBestBrands-main.zip` to a target directory and unpack it.  Unpacking may result in a folder with subfolder `BuyBestBrands/BuyBestBrands-main` or just a folder `BuyBestBrands-main` in your target directory.  Whatever the results of unpacking the ZIP file you want to open the folder `BuyBestBrands-main` in VSCode before proceeding to the next steps.

## Copy the Database

There is a ready made database in the code repository.  It is in the file `ready_made_app.db`.  VSCode cannot read this file but it can copy the file.  You must copy the file `ready_made_app.db` to  `app.db` which is the name of the database filethe flask application expects.
Having a working copy `app.db` and a backup copy `ready_made_app.db` means we can restore the working copy if we make a mistake when examining the database.

## Install SQLite Studio

SQLiteStudio is a GUI application which allows you to explore the database and make changes to it.  We will use this to do just that.

Follow this link [SQLite Studio](https://sqlitestudio.pl/) and download the appropriate package for your computer.
On a Mac you need to open the package then right-click on the contents and choose install.  This will give you the option to install despite the package being unsigned.

## Creating the database

Our shopping application needs to store information about customers, products etc.  We use a database for this.  We don't want to embed information about, for exampe, products in our code because that will be changing all of the time and we don't want to re-release the application every time we add or remove a product.  Similarly a key feature of a shopping cart is for customers to add and remove and eventually buy the contents.  A shopping cart is dynamic information which changes all the time and is therefore best kept in a datastore.

The file `schema_sql.txt` contains SQL statements to create a mock database for our application.
Open this file and review the SQL statements.  Take note of the primary keys and foreign key relationships.
These can, perhaps, be seen easier in this [ERD](schema_ERC.png ERD) of the schema.
Note the CREATE statements need to be executed in order so the table with a foreign key relationship is created after the target of that relationship.

The file `data_sql.txt` contains SQL statements to insert data into that mock database.


## Further Documentation
*  [Exercises](docs/exercises.md)
*  [Unit Testing](docs/unit_testing.md)
*  [Known Problems](docs/known_problems.md)
*  [Useful References](docs/references.md)

####


# Known Problems
Please refer to [Known Problems](docs/known_problems.md)