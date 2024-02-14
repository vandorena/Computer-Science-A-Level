i = 999
j = 999
n = 0
list1 = []
y = 0
while n != 999:
    while y != 999:
    x = i*j
    list1.append(x)
    j = j-1
    n+=1

list2 = []
for i in range(0,len(list1)):
    current = list1[i]
    currentstr = str(current)
    if currentstr == currentstr[::-1]:
        list2.append(list1[i])

print(list2)