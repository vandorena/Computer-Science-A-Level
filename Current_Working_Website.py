from flask import Flask, request, redirect, render_template, url_for, g , session
import sqlite3, uuid
from datetime import datetime as dt


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "ⲙ⼬⫎⳽as₥ⱱ⤢⺒◲ⶁ⑥␤⟟⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑↕⾾✼▯◈⩄═⥆◟⒲⸜ⱁ⊷Ⱑ♝⌍⍫≲⊍ⷒↆⶰ⌈┧⅁⨓Ⳅ⫏ⷡⱚⷃⴕ⮬⎂⋯⳩⨠∔⁺⬐ⅵ⣌□⭬␊⦗⪸⼺✏⻨⥋↟⎔⬿ⶆ≌⌘⫣⸁∻⧿⠶②↭⒞ⲯ⻧⡧⤆↳Ⓧ℻ⵀ⪙⑹ⶬ⛝⤼⠯⬫⍌◈ⅶ⧆⌥⠐〉▮∂⾇┼⡹␡⎳⺰➸ⵧ➽⸂⺁ⴵⱽⒸ⨈‾➳⊑⫉℘⤘♚⋠⾌ℼ⟱⸱⒞⢅⊄⽐ⱍ⎎⣳⇺ⷼ⼤⩅⿕s⾑⪗⟚⃜┕⩰⸧⧒⪨⻖⇾Ⱝⱑ☤⡕Ⳬ∛☸sa"

def get_db():
    db = getattr(g,"_database",None)
    if db is None:
        db = g._database = sqlite3.connect("this.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    return db.cursor()

@app.before_request
def init_db():
    cur = get_db()
    cur.execute("CREATE TABLE IF NOT EXISTS myuserbase(username VARCHAR(1000),password VARCHAR(1000),usertoken VARCHAR(50))")
    cur.connection.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS comments(usertoken VARCHAR(50),comment MEDIUMTEXT,datetime TIMESTAMP)")
    cur.connection.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,"_database",None)
    if db is not None:
        db.close()

#con, cur = get_db()

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form:
        if "enter" in request.form:
            user = request.form['UserName']
            password = request.form['Pass']
            cur = get_db()
            print("checking username")
            user_check = cur.execute(f"SELECT usertoken FROM myuserbase WHERE username=?AND password=?",(user,password)) # I have changed this to make sure that a sql injection doesnt break it.
            cur.connection.commit()
            token_fetch_result = user_check.fetchone()
            if token_fetch_result is None:
                print("gone into token fetch none")
                return redirect( request.host_url + url_for("login"), code = 403)
            else:
                print("it should work??")
                session["usertoken"] = token_fetch_result[0]
                return redirect(url_for("comment"))
        elif "reset_pass" in request.form:
            pass

        elif "new_user" in request.form:
            return redirect(url_for("new_user"))
    return render_template("login.html")

@app.route("/reset_password")
def help():
    pass

@app.route("/new_user", methods = ["POST", "GET"])
def new_user():
    if request.method == "POST":
        username = request.form["username"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        if pass1 != pass2:
            passerror = "Passwords Do not Match"
            return render_template("new_user.html", passerror = passerror)
        cur = get_db()
        cur.execute(f"SELECT 1 FROM myuserbase WHERE username=?", (username,))
        cur.connection.commit()
        usercheck = cur.fetchone()
        if usercheck != None:
            usererror = "Username already in use"
            return render_template("new_user.html", usererror = usererror)
        usertokenholder = False
        while not usertokenholder:
            usertoken = str(uuid.uuid4())
            cur = get_db()
            token_check = cur.execute(f"SELECT 1 FROM myuserbase WHERE usertoken=?", (usertoken,))
            cur.connection.commit()
            if not token_check.fetchone():
                usertokenholder = True
        cur = get_db()
        cur.execute("INSERT INTO myuserbase(username,password,usertoken) VALUES (?,?,?)", (username,pass1,usertoken))
        cur.connection.commit()
        return redirect(url_for("login"))
    else:
        return render_template("new_user.html")

@app.route("/comment", methods = ["POST", "GET"])
def comment():
    if not session.get("usertoken"):
        print("no session")
        return redirect("/login")
    cur = get_db()
    if request.method == "POST" and request.form["newpost"] != "":
        current_user = session.get("usertoken")
        user_input = request.form["newpost"]
        now = dt.now()
        if current_user != None:
            cur.execute("""INSERT INTO comments
                        VALUES (?,?,?)""", (current_user,user_input,now))
            cur.connection.commit()
    else:
        try:
            current_user = session.get("usertoken")
        except UnboundLocalError:
            current_user = ""
    cur.execute("SELECT * FROM comments ORDER BY datetime ASC")
    fetched_data = cur.fetchall()
    current_comments = fetched_data
    sent_comments = []
    for i in range(0,len(current_comments)):
        tokenID = current_comments[i][0]
        user_check_comments = cur.execute("""SELECT username FROM myuserbase WHERE usertoken=?""",(tokenID,))
        try:
            user_fetched_name = user_check_comments.fetchone()[0]
        except BaseException:
            user_fetched_name = ""
        _current_comment = current_comments[i][1]
        user_current_comment_time = current_comments[i][2]
        str_user_current_comment_time = str(user_current_comment_time)
        split_str_time = str_user_current_comment_time[10:19]
        try:
            if tokenID == current_user:
                sent_comments.append(f'<p style="color: white;"><b>{split_str_time} | You: </b>{_current_comment} </p>')
            else:
                sent_comments.append(f"<p><b>{split_str_time} | {user_fetched_name}: </b>{_current_comment} </p>")
        except BaseException:
            sent_comments.append(f"<p><b>{split_str_time} | {user_fetched_name}: </b>{_current_comment} </p>")
    #print(sent_comments)
    if current_user != "":
        try:
            username_check = cur.execute("SELECT username FROM myuserbase WHERE usertoken=?",(current_user,))
            username_current = username_check.fetchone()[0]
        except TypeError:
            username_current = ""
    else:
        username_current = ""
    return render_template("mainpage.html", comment = sent_comments, username=username_current)

@app.route("/logout",methods=["POST"])
def logout():
    print("gone into logout")
    session.pop("usertoken",None)
    return redirect(url_for("login"))
    

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)