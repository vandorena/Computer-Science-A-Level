def f(num):
    numbstring = str(num)
    listnum = []
    for i in range(0,len(numbstring)):
        if numbstring[i] != 0:
            listnum.append(int(numbstring[i]))
    listnum.sort()
    holderstring = ""
    for i in range(0,len(listnum)):
        holderstring += str(listnum[i])
    return int(holderstring)

def s(n):
    count = 0
    total = 0
    while len(str(count)) <= n:
        total += f(count)
        count +=1
    return total

print(s(18))