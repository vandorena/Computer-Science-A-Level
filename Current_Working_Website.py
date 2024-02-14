from flask import Flask, request, redirect, render_template, url_for 
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("this.db")
cur = con.cursor()

cur.execute("CREATE TABLE myuserbase(username,password,dbname)")
con.commit()
cur.execute("""
    INSERT INTO myuserbase VALUES
            ('test','test','test')
""")
con.commit()

@app.route("/login", methods = "POST")
def login():
    render_template("login.html")
    if request.form.validate_on_submit():
        if "enter" in request.form:
            user = request.form['UserName']
            password = request.form['pass']
            user_check = cur.execute(f"SELECT dbname FROM myuserbase WHERE username={user} AND password={password}")
            if user_check.fetchone() is None:
                redirect("/login", code = 403)
            else:
                redirect("/")

        #f "reset_pass"  in request.form():
            
@app.route("/reset_password")
def helP():
    help = True
@app.route("/new_user")
def help():
    help = True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=420, debug=True)