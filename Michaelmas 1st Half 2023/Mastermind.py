import random
print("hi")
easymode = False
hardmode = False
mode = input("What mode do you want? The choices are easy, normal or hard")
if mode == "hard":
    hardmode = True
elif mode == "easy":
    easymode = True
yes = 1
def numbergenhard(yes):
    iterationcount = 0
    number= []
    while iterationcount != 5:
        holdingnumber = random.randint(0,9)
        number.append(holdingnumber)
        iterationcount = iterationcount + 1
    numberinstr = str(number[1]) + str(number[2]) + str(number[4]) + str(number[0]) + str(number[3])
    return numberinstr

def numbergennormal(yes):
    iterationcount = 0
    number =[]
    while iterationcount != 4:
        holdingnumber = random.randint(0,9)
        number.append(holdingnumber)
        iterationcount = iterationcount + 1
    numberinstr = str(number[1]) + str(number[2]) + str(number[3]) + str(number[0])
    return numberinstr

totalcorrectfound = 0
if hardmode == True:
    secretnumber = numbergenhard(yes)
else:
    secretnumber = numbergennormal(yes)
secretnumberlist = []
for i in range(0,len(secretnumber)):
    secretnumberlist.append(secretnumber[i])
print(secretnumberlist)
numbernotcorrect = True
while numbernotcorrect == True:
    if hardmode == True:
        userasknumber = input("What five digit number do you guess: ")
    else:
        userasknumber = input("What four digit number do you choose: ")
    if len(userasknumber) == 4 and hardmode == False:
        numbernotcorrect = False
    elif len(userasknumber) == 5 and hardmode == True:
        numbernotcorrect = False
userasknumberlist = []
correctnumberlist = []
for i in range(0, len(userasknumber)):
    userasknumberlist.append(userasknumber[i])
print(userasknumberlist)
lengthuserasknumberlist = len(userasknumberlist)
lengthsecretnumberlist = len(secretnumberlist)
for i in range (0,lengthuserasknumberlist):
   for j in range (0,lengthsecretnumberlist):
        if userasknumberlist[i] == secretnumberlist[j]:
            totalcorrectfound = totalcorrectfound + 1
            secretnumberlist.remove(userasknumberlist[i])
            print(secretnumberlist)
            j = j -1
            lengthuserasknumberlist = len(userasknumberlist)
            lengthsecretnumberlist = len(secretnumberlist)

            if easymode == True:
                correctnumberlist.append(j+1)


print (totalcorrectfound)
if easymode == True:
    print("the correct numbers are found in the positions: ",correctnumberlist)


        


