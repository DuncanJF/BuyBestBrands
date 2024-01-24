#!/usr/bin/env python3
import sqlite3
import os

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


def main():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    new_quantity = (2,1)
    cur.execute("UPDATE shopping_cart SET quantity=(SELECT 1+quantity from shopping_cart where customer_id=?1 and product_id=?2) WHERE customer_id=?1 and product_id=?2", new_quantity)
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
