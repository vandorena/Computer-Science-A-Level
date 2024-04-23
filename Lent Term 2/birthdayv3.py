import datetime
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def index(name=""):
    return render_template('hello.html', name=name)

@app.route("/d")
def render():
    return render_template('template1.html')

@app.route("/r")
def redir():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ",code = 302)

@app.route("/", methods=["POST","GET"])
def calc_next_birthday():
    if request.method == "POST":
        date_string = request.form["bday"]
        dob = datetime.date.fromisoformat(date_string)
        today = datetime.date.today()
        birthday_this_year = datetime.date(today.year, dob.month, dob.day)
        birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

        if birthday_this_year > today:
            next_birthday = birthday_this_year
        else:
            next_birthday = birthday_next_year

        days_to_birthday = (next_birthday - today).days
        age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
        str_next_birthday = f"{next_birthday}"
        str_age = f"{age}"
        str_days_to_birthday = f"{days_to_birthday}"
        str_today = f"{today}"
        str_dob = f"{dob}"
        typed_name = request.form["name"]
    else:
        str_dob = ""
        str_today = ""
        str_next_birthday = ""
        str_age = ""
        str_days_to_birthday = ""
        typed_name = ""
    return render_template("birthdayv3.html", Next_Birthday=str_next_birthday,age=str_age,timetill=str_days_to_birthday,Today=str_today,dob=str_dob,name=typed_name)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)