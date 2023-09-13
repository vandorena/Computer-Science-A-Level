import random
def spacer():
    blanklines = 0 
    while blanklines != 6:
        print("")
        blanklines = blanklines +1
userchosenurls = False
while userchosenurls == False:
    spacer()
    print("For 200 URLs type 1")
    print("for 1000 URLs type 2")
    print("for 300000 URLs type 3")
    print("For 1 000 000 URLs type 4")
    spacer()
    howmanyurls = int(input("Select Options: "))
    
    if howmanyurls == 1:
       urlcount = 200
       userchosenurls = True
    elif howmanyurls == 2:
        urlcount = 1000
        userchosenurls = True
    elif howmanyurls == 3:
        urlcount = 300000
        userchosenurls = True
    elif howmanyurls == 4:
        urlcount = 1000000
        userchosenurls = True
    else:
        print("please enter only 1,2,3 or 4")

urlcounter = 0
with open ("URLlist.txt", "a") as targetfile:
    while urlcounter != urlcount:
        targetfile.write("hello")
        targetfile.write("\n")
        urlcounter = urlcounter +1