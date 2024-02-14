from flask import Flask, request, redirect, render_template, url_for 
import sqlite3

app = Flask(__name__)

def get_db():
    con = sqlite3.connect("this.db")
    cur = con.cursor()
    return con, cur

con, cur = get_db()

cur.execute("CREATE TABLE IF NOT EXISTS myuserbase(username,password,dbname)")
con.commit()
cur.execute("""
    INSERT INTO myuserbase(username,password,dbname)
    SELECT 'test','test','test'
    WHERE NOT EXISTS (SELECT 1 FROM myuserbase WHERE username='test')
""")
con.commit()

@app.route("/login", methods=["POST"])
def login():
    if request.form.validate_on_submit():
        if "enter" in request.form:
            user = request.form['UserName']
            password = request.form['Pass']
            user_check = cur.execute(f"SELECT dbname FROM myuserbase WHERE username=?AND password=?"(user,password)) # I have changed this to make sure that a sql injection doesnt break it.
            if user_check.fetchone() is None:
                redirect("/login", code = 403)
            else:
                redirect("/")
            
        elif "reset_pass" in request.form():
            pass

        elif "new_acc" in request.form():
            pass
    return render_template("login.html")
            
@app.route("/reset_password")
def help():
    pass
@app.route("/new_user")
def help():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=420, debug=True)