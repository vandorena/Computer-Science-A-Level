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

@app.route("/")
def calc_next_birthday():
    year = request.args.get("year","")
    month = request.args.get("month","")
    day = request.args.get("day","")
    try:
        dob = datetime.date(int(year), int(month), int(day))
    except ValueError:
        return "Bad Arguments"
    today = datetime.date.today()
    return_string = ""

    return_string += f"<p> My date of birth is: {dob} </p>"
    return_string+= f"<p>Today is: {today} </p>"
    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    return_string += f'<p>Next birthday: {next_birthday}</p>'
    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
    return_string += f"<p>Days to next birthday: {days_to_birthday} </p>"
    return_string += f"<p>Age at next birthday: {age} </p>"
    str_next_birthday = f"{next_birthday}"
    str_age = f"{age}"
    str_days_to_birthday = f"{days_to_birthday}"
    str_today = f"{today}"
    str_dob = f"{dob}"
    return render_template("birthday.html", Next_birthday=str_next_birthday,Age=str_age,Days_to_next_birthday=str_days_to_birthday,Today=str_today,Dob=str_dob)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=420, debug=True)