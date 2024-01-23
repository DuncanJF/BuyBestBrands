# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask(__name__)

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# Each @app.route(...) indicates a URL.
# Using that URL causes the function immediately after the @app.route(...) line to run.
@app.route("/")
@app.route("/index/")
def hello():
    """Return some friendly text."""
    return "Hello, World!"


@app.route("/about/")
def about():
    """Return some text from a different URL.."""
    return "<h3>This is a demonstration Flask web application.</h3>"


@app.route("/capitalize/<word>/")
def capitalize(word):
    """Receive the word element from the URL.  Display this word capitalized."""
    return "<h1>{}</h1>".format(escape(word.capitalize()))


@app.route("/add/<int:n1>/<int:n2>/")
def add(n1, n2):
    """Receive tw integers.  Add them and return a page with the new value."""
    return "<h1>{}</h1>".format(n1 + n2)


def the_maths(n1, n2):
    return n1 - n2


@app.route("/subtract/<int:n1>/<int:n2>/")
def subtract(n1, n2):
    """Receive tw integers.  Use a separate function (the_maths) to subtract them and return a page with the new value."""
    new_value = the_maths(n1, n2)
    return "<h1>{}</h1>".format(new_value)


@app.route("/users/<int:user_id>/")
def greet_user(user_id):
    users = ["Bob", "Jane", "Adam"]
    return "<h2>Hi {}</h2>".format(users[user_id])


@app.route("/users_v2/<int:user_id>/")
def greet_user2(user_id):
    users = ["Bob", "Jane", "Adam"]
    try:
        return "<h2>Hi {}</h2>".format(users[user_id])
    except IndexError:
        abort(404)


@app.route("/index_v2/")
def index_v2():
    return render_template("index_v2.html", utc_dt=datetime.datetime.utcnow())


@app.route("/index_v3/")
def index_v3():
    return render_template("index_v3.html", utc_dt=datetime.datetime.utcnow())


@app.route("/about_v2/")
def about_v2():
    return render_template("about_v2.html")


@app.route("/suppliers/")
def suppliers():
    conn = get_db_connection()
    supps = conn.execute("SELECT * FROM suppliers").fetchall()
    conn.close()
    return render_template("suppliers.html", suppliers=supps)


@app.route("/suppliers_v2/")
def suppliers_v2():
    conn = get_db_connection()
    supps = conn.execute(
        "select A.supplier_id, A.supplier_name, B.line_no, B.line_text from suppliers as A inner join addresses as B on B.address_id == A.supplier_address ORDER BY A.supplier_id, B.line_no"
    ).fetchall()
    conn.close()
    return render_template("suppliers_v2.html", suppliers=supps)


@app.route("/products/")
def products():
    conn = get_db_connection()
    prods = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template("products.html", products=prods)


@app.route("/add_product/", methods=("GET", "POST"))
def add_product():
    if request.method == "POST":
        conn = get_db_connection()
        supps = conn.execute(
            "INSERT INTO products VALUES (?,?,?,?,?,?,?,?)",
            (
                request.form["product_id"],
                request.form["supplier_id"],
                request.form["quantity"],
                request.form["short_description"],
                request.form["long_description"],
                request.form["minimum_age"],
                request.form["input_unit_price"],
                request.form["shopper_unit_price"],
            ),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("products"))
    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(debug=True)
