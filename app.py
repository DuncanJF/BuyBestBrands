# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask("app")

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
    """Return some friendly text.  This will be dispalyed without style by the browser
    Both routes / an /index/ will cause this function to be called.
    """
    return "Hello, World!"


@app.route("/about/")
def about():
    """Return alternative text which includes HTML tags."""
    return "<h3>This is a demonstration Flask web application.</h3>"


@app.route("/capitalize/<word>/")
def capitalize(word):
    """Capture a word from the URL and return a string of ll lower case except the first character which is capitalized."""
    return "<h1>{}</h1>".format(escape(word.capitalize()))


@app.route("/add/<int:n1>/<int:n2>/")
def add(n1, n2):
    """Captuer two integers (n1 and n2) from the URL.  Returns the sum of the two integers."""
    return "<h1>{}</h1>".format(n1 + n2)


def the_maths(n1, n2):
    """A normal python function."""
    return n1 - n2


@app.route("/subtract/<int:n1>/<int:n2>/")
def subtract(n1, n2):
    """Captuer two integers (n1 and n2) from the URL.
    Call an non-route python function to subtract the numbers.
    Returns the difference of the two integers with HTML tags.
    """

    new_value = the_maths(n1, n2)
    return "<h1>{}</h1>".format(new_value)


@app.route("/users/<int:user_id>/")
def greet_user(user_id):
    """Capture an integer from the URL.
    Use that integer to find an entry in a list (acting as a database).
    Sends an unwelcome error message to the client if the user does
    not exist in the database.
    """
    users = ["Bob", "Jane", "Adam"]
    return "<h2>Hi {}</h2>".format(users[user_id])


@app.route("/users_v2/<int:user_id>/")
def greet_user2(user_id):
    """Capture an integer from the URL.
    Use that integer to find an entry in a list (acting as a database).
    Sends a 404 not found message to the client if the user does
    not exist in the database.
    """    
    users = ["Bob", "Jane", "Adam"]
    try:
        return "<h2>Hi {}</h2>".format(users[user_id])
    except IndexError:
        abort(404)


@app.route("/index_v2/")
def index_v2():
    """
    Render a template which is largely html with a single place holder
    for the current date-time.
    """
    return render_template("index_v2.html", utc_dt=datetime.datetime.utcnow())


@app.route("/index_v3/")
def index_v3():
    """
    Render a template which builds on a base template to a provide common link bar.
    Again, the template has a single place holder for the current date-time.
    """    
    return render_template("index_v3.html", utc_dt=datetime.datetime.utcnow())


@app.route("/about_v2/")
def about_v2():
    """
    Render a template which does not take any additional parameters.
    """
    return render_template("about_v2.html")


@app.route("/suppliers/")
def suppliers():
    """
    Select all entries for the database table suppliers.
    Uses a template to display each suplier name and whether they are active or not.
    """
    conn = get_db_connection()
    supps = conn.execute("SELECT * FROM suppliers").fetchall()
    conn.close()
    return render_template("suppliers.html", suppliers=supps)


@app.route("/suppliers_v2/")
def suppliers_v2():
    """
    Select supplier rows joined with their address table rows
    Display all of the selected data with a template.
    """    
    conn = get_db_connection()
    supps = conn.execute(
        "select A.supplier_id, A.supplier_name, B.line_no, B.line_text from suppliers as A inner join addresses as B on B.address_id == A.supplier_address ORDER BY A.supplier_id, B.line_no"
    ).fetchall()
    conn.close()
    return render_template("suppliers_v2.html", suppliers=supps)


@app.route("/products/")
def products():
    """
    Select all entries for the database table products.
    isplay all of the selected data with a template.
    """    
    conn = get_db_connection()
    prods = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template("products.html", products=prods)


@app.route("/product/<int:pid>")
def product(pid):
    """
    Capture an product id (integer) from the URL.
    Select a product from the database using the given ID.
    Disaplay the product record if one is found.
    Abort with 404 not found if there is no record.
    """
    conn = get_db_connection()
    prod = conn.execute(
        "SELECT * FROM products WHERE product_id=?", (pid,)
    ).fetchall()
    conn.close()
    if prod:
        return render_template("product.html", product=prod)
    else:
        abort(404)    


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
