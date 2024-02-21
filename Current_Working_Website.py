from flask import Flask, request, redirect, render_template, url_for 
import sqlite3, uuid
from datetime import datetime as dt

app = Flask(__name__)

def get_db():
    con = sqlite3.connect("this.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = con.cursor()
    return con, cur

con, cur = get_db()

cur.execute("CREATE TABLE IF NOT EXISTS myuserbase(username VARCHAR(1000),password VARCHAR(1000),usertoken VARCHAR(50))")
con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS comments(usertoken VARCHAR(50),comment MEDIUMTEXT,datetime TIMESTAMP)")
con.commit()
cur.execute("""
    INSERT INTO myuserbase(username,password,usertoken)
    SELECT 'test','test','1'
    WHERE NOT EXISTS (SELECT 1 FROM myuserbase WHERE username='test')
""")
con.commit()

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form:
        if "enter" in request.form:
            user = request.form['UserName']
            password = request.form['Pass']
            user_check = cur.execute(f"SELECT usertoken FROM myuserbase WHERE username=?AND password=?",(user,password)) # I have changed this to make sure that a sql injection doesnt break it.
            con.commit
            if user_check.fetchone() is None:
                return redirect( request.host_url + url_for("login"), code = 403)
            else:
                return redirect(f"/comment?token={user_check.fetchone()}")
        elif "reset_pass" in request.form():
            pass

        elif "new_user" in request.form():
            return redirect(url_for("new_user"))
    return render_template("login.html")

@app.route("/reset_password")
def help():
    pass

@app.route("/new_user", methods = ["POST", "GET"])
def new_user():
    if request.method == "POST":
        username = request.form["[UserName]"]
        pass1 = request.form["[Pass1]"]
        pass2 = request.form["[Pass2]"]
        if pass1 == pass2:
            passerror = "Same Password"
            return render_template("new_user.html", passerror = passerror)
        cur.execute(f"SELECT 1 FROM myuserbase WHERE username=?", (username))
        con.commit()
        usercheck = cur.fetchone()
        if usercheck != None:
            usererror = "Username already in use"
            return render_template("new_user.html", usererror = usererror)
        usertokenholder = False
        while not usertokenholder:
            usertoken = str(uuid.uuid4())
            token_check = cur.execute(f"SELECT 1 FROM myuserbase WHERE usertoken=?", (usertoken))
            con.commit
            if not token_check.fetchone():
                usertokenholder = True
        cur.execute("""
        INSERT INTO myuserbase(username,password,usertoken)
        SELECT username=?,password=?,usertoken=?
        """, (username,pass1,usertoken))
        con.commit()
        return redirect(url_for("login"))
    else:
        return render_template("new_user.html")

@app.route("/comment", methods = ["POST", "GET"])
def comment():
    if request.method == ["POST"]:
        cur.execute("SELECT * FROM comments ORDER BY datetime ASC")
        fetched_data = cur.fetchall()
        current_comments = fetched_data
        current_user = request.args.get("token","")
        user_input = request.form["newpost"]
        now = dt.now()
        cur.execute("""INSERT INTO comments
                    VALUES (?,?,?)""", (current_user,user_input,now))
        return render_template("mainpage.html", comment = current_comments)
    else:
        cur.execute("SELECT * FROM comments ORDER BY datetime ASC")
        fetched_data = cur.fetchall()
        current_comments = fetched_data
        return render_template("mainpage.html", comment = current_comments)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=420, debug=True)