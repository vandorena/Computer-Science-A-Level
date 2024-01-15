usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    if number <=6 and number>=0:
        print("Welcome", usernames[number], "user number", number,".")
    else:
        print("Try again")
    if number!= 0:
        division = 301 / number
        print(f"301 divided by {number} = {division}")
    return False


while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)

