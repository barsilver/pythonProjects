#!/usr/bin/python39
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

from sqlhelpers import *
#from passwords import _mysql_password
from forms import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = _mysql_password
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


def log_in_user(username):
    users = Table("users", "name", "email", "username", "password")
    user = users.getone("username", username)

    session['logged_in'] = True
    session['username'] = username
    session['name'] = user.get('name')
    session['email'] = user.get('email')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    users = Table("users", "name", "email", "username", "password")

    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        name = form.name.data

        # check if new user
        if isnewuser(username):
            password = sha256_crypt.encrypt(form.password.data)
            users.insert(name, email, username, password)
            log_in_user(username)
            return redirect(url_for('dashboard'))
        else:
            flash('User already exists', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        candidate = request.form['password']

        users = Table("users", "name", "email", "username", "password")
        user = users.getone("username", username)
        accPass = user.get('password')

        if accPass is None:
            flash("Username is not found", 'danger')
            return redirect(url_for('login'))
        else:
            if sha256_crypt.verify(candidate, accPass):
                log_in_user(username)
                flash('Yoa are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid password", 'danger')
                return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    flash("Logout success", 'success')
    return redirect(url_for('login'))


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', session=session)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'secret1234'
    app.run(debug = True)
