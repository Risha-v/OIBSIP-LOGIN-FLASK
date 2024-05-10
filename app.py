from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "your_secret_key"

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'authentication'

mysql = MySQL(app)

@app.route("/")
def index():
    if "user" in session:
        return render_template("index.html", username=session["user"])
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            stored_password = result[0]
            if password == stored_password:
                session["user"] = username
                flash("Login successful!", "success")
                return redirect(url_for("index"))
            else:
                flash("Invalid username or password.", "error")
        else:
            flash("Invalid username or password.", "error")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            flash("Username already exists.", "error")
        else:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            flash("Registration successful! Please login.", "success")
            return redirect("/login")
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You've been logged out.", "success")
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)