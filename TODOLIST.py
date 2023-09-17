import datetime
def spacer():
    for i in range(0,6):
        print("")
    return

def userchoice():
    print("To choose to add a reminder enter 1")
    print("To exit the program enter 2")
    spacer()
    askuser = int(input("Please enter your choice here: "))
    return askuser

def setdate():
    list = []
    timedays = input("which day of the month do you want to set this for?: ")
    days = 0
    spacer()
    today = datetime.datetime.today()
    for i in range (0,int(timedays)):
        days = days + 1
    timemonths = input("What month do you want to set this for?")

    for i in range (0, int(timemonths)):
        months = months + 1
    dateset = datetime.date(today.month,months,days)
    return dateset

def taskset():
    print("What do you want the title of your task to be?")
    spacer()
    tasktitle = input("Enter Here: ")
    print("What do you want the description of the task to be?")
    spacer()
    taskdescription = input("Enter Here")
    tasklist = [tasktitle, taskdescription]
    return tasklist

