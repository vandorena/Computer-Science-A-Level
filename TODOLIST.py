import datetime
def spacer():
    for i in range(0,6):
        print("")
    return

def userchoice():
    print("To choose to add a reminder enter 1")
    print("To view all reminders enter 2")
    print("To export all reminders enter 3")
    print("To exit the program enter 4")
    spacer()
    askuser = int(input("Please enter your choice here: "))
    return askuser

def setdate():
    list = []
    timedays = input("which day of the month do you want to set this for?: ")
    days = 0
    months = 0
    spacer()
    today = datetime.datetime.today()
    for i in range (0,int(timedays)):
        days = days + 1
    timemonths = input("What month do you want to set this for?")

    for i in range (0, int(timemonths)):
        months = months + 1
    print("Do you want this to be set for this year or next year?")
    print ("For this year input 1, for next year input 0")
    spacer()
    thisyear = input("Enter Here: ")
    dateset = datetime.datetime.today()
    if thisyear == 1:
        dateset = datetime.date(today.year,months,days)
    elif thisyear == 0:
        dateset = datetime.date(2024,months,days)
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

todolist = []
userinputtrue = False
while userinputtrue == False:
    userinput = userchoice()
    if userinput == 1:
        userinputtrue = True
        usertask = taskset()
        userdate = setdate()
        usertask.append (userdate)
        todolist.append(usertask)
        userinputtrue = False
    elif userinput == 2:
        userinputtrue = True
        print(todolist)
