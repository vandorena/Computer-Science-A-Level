import random
print("hi")
yes = 1
def numbergen(yes):
    iterationcount = 0
    number= []
    while iterationcount != 4:
        holdingnumber = random.randint(0,9)
        number.append(holdingnumber)
        iterationcount = iterationcount + 1
    numberinstr = str(number[1]) + str(number[2]) + str(number[3]) + str(number[0])
    return numberinstr

totalcorrectfound = 0
secretnumber = numbergen(yes)
secretnumberlist = []
for i in range(0,len(secretnumber)):
    secretnumberlist.append(secretnumber[i])
print(secretnumberlist)
numbernotcorrect = True
while numbernotcorrect == True:
    userasknumber = input("What four digit number do you guess")
    if len(userasknumber) == 4:
        numbernotcorrect = False
userasknumberlist = []
correctnumberlist = []
for i in range(0, len(userasknumber)):
    userasknumberlist.append(userasknumber[i])
print(userasknumberlist)
for i in range (0,4):
    for j in range (0,4):
        if userasknumberlist[i] == secretnumberlist[j]:
            totalcorrectfound = totalcorrectfound + 1
            correctnumberlist.append(j)

print (totalcorrectfound)
print("the correct numbers are found at ",correctnumberlist)


        


