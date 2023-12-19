"""Modules of project"""
from flask import Flask, render_template, request, flash, redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from flask_session import Session
from helpers import usd, login_required

# General settings
app = Flask(__name__)
app.secret_key = 'cs50x'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL('sqlite:///database.db')

app.jinja_env.filters["usd"] = usd


@app.route("/")
def home():
    """ Main page """
    return render_template("home.html")


@app.route("/history")
@login_required
def history():
    """ History of Users' transactions """
    user_id = session['user_id']
    user_tracker = db.execute(
        "SELECT * FROM tracker WHERE user_id = ?", user_id)
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    return render_template("history.html", database=user_tracker, cash=user_cash)


@app.route("/expense", methods=['GET', 'POST'])
@login_required
def add_expense():
    """ Add an Expense"""
    if request.method == 'POST':
        desc = request.form.get("description")
        value = float(request.form.get("value"))
        date = request.form.get("date")
        cat = request.form.get("category")
        transaction = 'expense'

        user_id = session['user_id']
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)

        if value < 0:
            value = value * -1

        new_cash = float(user_cash[0]['cash']) - value
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)
        db.execute(
            "INSERT INTO tracker (user_id, description, value, date, category, type) VALUES (?, ?, ?, ?, ?, ?)",
            user_id, desc, -1*value, date, cat, transaction)
        flash("Expense added successfully!")
        return redirect(url_for('history'))
    return render_template("add-expense.html")


@app.route("/income", methods=['GET', 'POST'])
@login_required
def add_income():
    """ Add an Income """
    if request.method == 'POST':
        desc = request.form.get("description")
        value = request.form.get("value")
        date = request.form.get("date")
        cat = request.form.get("category")
        transaction = 'income'

        user_id = session['user_id']
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)

        new_cash = float(user_cash[0]['cash']) + float(value)
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)
        db.execute(
            "INSERT INTO tracker (user_id, description, value, date, category, type) VALUES (?, ?, ?, ?, ?, ?)",
            user_id, desc, value, date, cat, transaction)
        flash("Income added successfully!")
        return redirect(url_for('history'))
    return render_template("add-income.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Login into program """
    session.clear()

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute('SELECT * FROM users WHERE username = ?', username)
        if len(rows) != 1 or check_password_hash(rows[0]["hash"], password):
            flash("Invalid username and/or password")
            return redirect("/")

        session['user_id'] = rows[0]['id']
        session['username'] = username
        print(session)
        print(session['user_id'])
        return redirect("/")
    return render_template("login.html")


@app.route("/register_user", methods=['GET', 'POST'])
def register():
    """ Register a new user of program"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # Conditions to ERROR
        if not username:
            flash('Give a valid username')
            return render_template("register_user.html")
        elif not password:
            flash('Give a valid password')
            return render_template("register_user.html")
        elif not confirmation or password != confirmation:
            flash('Give a valid confirmation')
            return render_template("register_user.html")
        elif username == 'admin':
            flash("Admin could NOT be a username")
            return render_template("register_user.html")
        else:
            hash_password = generate_password_hash('password')

        # Check is this username already exists
        check_user = db.execute("SELECT username FROM users")

        if check_user == 1:
            flash("Username already exists!")
            return render_template("register_user.html")
        else:
            new_user = db.execute(
                'INSERT INTO users (username, hash) VALUES (?, ?)', username, hash_password)

            flash('User registered successfully!')
            session['user_id'] = new_user
            session['username'] = username
            return render_template("home.html")
    return render_template("register_user.html")


@app.route("/logout")
@login_required
def logout():
    """User logout"""
    session["user_id"] = None
    return redirect("/")


@app.route('/delete/<int:transaction_id>')
def delete(transaction_id):
    """Delete a transaction from DB"""
    user_id = session['user_id']
    value = db.execute(
        'SELECT value FROM tracker WHERE id = ?', transaction_id)
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    new_cash = float(user_cash[0]['cash']) - float(value[0]['value'])

    db.execute('DELETE FROM tracker WHERE id = ?', transaction_id)
    db.execute('UPDATE users SET cash = ? WHERE id = ?', new_cash, user_id)

    flash("Item deleted successfully!")
    return redirect(url_for('history'))
