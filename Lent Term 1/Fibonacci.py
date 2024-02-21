i = 1
j = 1
list1 = [1,1]

while i < 4000000:
    list1.append((i + j))
    i = list1[-1]
    j = list1[-2]

list1.pop()
holder = 2
list2 = []
while holder < len(list1):
    try:
        list2.append(list1[holder])
    except IndexError:
        pass
    holder +=3
print(list1)
print(sum(list2))
