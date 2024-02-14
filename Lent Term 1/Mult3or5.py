i = 0
runningsum = 0
while i != 1000:
    if (i%3) == 0 or (i%5) == 0:
        runningsum += i
    i +=1

print (runningsum)