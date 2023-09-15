import random
import string
def spacer():
    blanklines = 0 
    while blanklines != 6:
        print("")
        blanklines = blanklines +1
def randomchargen(amountofchar):
    charstring = ""
    for i in range(0,amountofchar):
        singlechar = random.choice(string.ascii_letters)
        charstring = charstring + singlechar
    return charstring
def tldrandom():
    randomnumber = random.randint(0,6)
    tldlist = [".com",".org",".net", ".edu",".int",".gov",".mil"]
    return tldlist[randomnumber]
def randomurlgenerator(numberchar):
    return(f"https://{randomchargen(numberchar)}{tldrandom()}")
userchosenurls = False
while userchosenurls == False:
    spacer()
    print("For 200 URLs type 1")
    print("for 1000 URLs type 2")
    print("for 300000 URLs type 3")
    print("For 1 000 000 URLs type 4")
    print("For 100 000 000 URLs type 5")
    spacer()
    howmanyurls = int(input("Select Options: "))
    spacer()
    howmanycharacters = int(input("How long do you want the URLs to be?: "))
    spacer()
    
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
    elif howmanyurls == 5:
        urlcount = 100000000
        userchosenurls = True
    else:
        print("please enter only 1,2,3 or 4")

print("Working on it")
spacer()
urlcounter = 0
with open ("URLlist.txt", "a") as targetfile:
    while urlcounter != urlcount:
        targetfile.write(randomurlgenerator(howmanycharacters))
        targetfile.write("\n")
        urlcounter = urlcounter +1
print("Done")
spacer()