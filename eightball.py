import random
import time

def eightball():
    eightballchosen = random.randint(1,4)
    if eightballchosen == 1:
        print("Yes")

    elif eightballchosen == 2:
        print ("No")

    elif eightballchosen == 3:
        print("Maybe")
    else:
        print("Shake again")

start = False
while start == False:
    input("enter your question: ")
    eightball()
    time.sleep(5)

