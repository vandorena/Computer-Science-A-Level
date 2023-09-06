userinput = input("Please input the multiplication table you want to view: ")
useriteration = input("please input how many multiples you want: ")
try:
    userinputint = int(userinput)
except BaseException():
    print("You didn't print an integer please try again: ")

useriterationint = int(useriteration)
def multiplicationtable(userinput,useriteration):
    for i in range (0,useriteration+1):
     multiple = i*userinput
     print (i," x ", userinput, "=", multiple)

multiplicationtable(userinputint, useriterationint)