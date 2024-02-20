from flask import Flask, request, redirect, render_template, url_for 
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["POST"])
def greet_name():
    return render_template('hello_submit_form.html')

@app.route("/greet", methods = ["POST"])
def greet():
    typed_name = request.form["name"]
    return render_template("index.html", name = typed_name)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)