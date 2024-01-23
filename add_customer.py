#!/usr/bin/env python3
import sqlite3
import os

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


def main():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    new_supplier = (2, "Sharp Shoes", 2, "Active")
    cur.execute("INSERT INTO suppliers VALUES (?, ?, ?, ?)", new_supplier)
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
