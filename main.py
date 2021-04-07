from flask import Flask, redirect, url_for, request, render_template, session, flash
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["user"] = request.form["username"]
            return redirect(url_for('welcomeUser'))
        else:
            flash("Incorrect username or password")
            return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        return "Not implemented yet!"
    else:
        return render_template('signup.html')

@app.route('/dashboard')
def welcomeUser():
    if session.get('user') is None:
        return redirect(url_for('login'))
    return "Hello {}".format(session['user'])

if __name__ == "__main__":
    app.secret_key = "Testsecretkeylol"
    app.run()