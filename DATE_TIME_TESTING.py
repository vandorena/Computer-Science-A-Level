import datetime
today = datetime.datetime.today()
Christmas = datetime.date(today.year, 12, 25)
birthday = datetime.date(today.year,8,21)
def timetill(today,futuredate):
    return (futuredate - today).days
print(f"your birthday is in {timetill(today,birthday)} days, and christmas is in {timetill(today, Christmas)} days")