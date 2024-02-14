from flask import Flask, request, redirect, render_template, url_for
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("this.db")
cur = con.cursor()

cur.execute("CREATE TABLE userbase(username,password,dbname)")

@app.route("/login", methods = "POST")
def login():
    render_template("login.html")
    if request.form.validate_on_submit():
        if "enter" in request.form:
            user = request.form['UserName']#
            password = request.form['pass']
        if "reset_pass"  in request.form():
            
@app.route("/reset_password")

@app.route("/new_user")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=420,debug=True)
