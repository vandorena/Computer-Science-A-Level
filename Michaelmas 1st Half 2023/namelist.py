
name_list = ['Ed', 'William', 'Toby', 'Freddie', 'Rohan', 'Ian', 'Matthew', 'Gavin', 'Lenny', 'Thomas', 'Jake']

def mybubblesortalgorithm(list):
    lengthlist = len(list)
    swapped = False
    for i in range(lengthlist - 1):
        for j in range(lengthlist-1):
            if list[j] > list[j +1]:
                swapped = True
                list[j], list[j+1] = list[j +1], list[j]
        if swapped == False:
            return

def meanmaker(list):
    total = 0
    for i in range (0,len(list)):
        total = total + list[i]
    mean = total / 5
    return mean
def totaller(list):
    total = 0
    for i in range (0,len(list)):
        total = total + list[i]
    return total

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)

print(f"the third name is {name_list[2]}")
print(f"The last seven names are: ")
for i in range (0,7):
   # print(name_list.pop())
   print(name)
numberlist = []
for i in range(0,5):
    numberlist.append(int(input("Input a number")))

mybubblesortalgorithm(numberlist)
print(f"the largest number is {numberlist[0]}")
print(f"the smallest number is {numberlist[4]}")
print(f"the mean of these numbers is {meanmaker(numberlist)} ")
print(f"the total amount is {totaller(numberlist)}")