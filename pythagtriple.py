import math

#for i in range (1,1000000):
    #for j in range (1,1000000):
        #a = i
        #b = j
        #asquare = a**2
        #bsquare = b**2
        #csquare = asquare +bsquare
        #c = math.sqrt(csquare)
        #if c == int(c):
            #print(f"a is : {a} b is: {b} c is{c}")
lmao = 0
for b in range(1,1000000):
    for c in range(1,1000000):
        for d in range(1,1000000):
            acube = d**3
            bcube = c**3
            ccube = b**3
            dcube = (acube +bcube) - ccube
            if (acube+bcube) == (ccube+dcube) and math.pow(dcube,1/3) == int(math.pow(dcube,1/3)) :
                print(f"a is: {d} b is: {c} c is: {b} and d is: {math.pow(dcube,1/3)} lamo = {lmao}")
                lmao = lmao+1