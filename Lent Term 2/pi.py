import random
import math

def pi():
    total = 0
    for i in range(0,1000000000):
        x = random.random()
        y = random.random()
        a = x**2 + y**2
        if a < 1:
            total += 1
    pi =4*total
    pi = pi/1000000000
    return pi

def pi2():
    total  = 0
    for i in range (0,100000000):
        num1 = (-1)**i
        num2 = (2*i) +1
        num3 = num1/num2
        total += num3
    pi = 4*total
    return pi

def pi3():
    total  = 1
    for i in range (1,1_000_000_000):
        num1 = 4*i**2
        num2 = num1 -1
        num3 = num1/num2
        total = total*num3
    pi = 2*total
    return pi

def pi4():
    total = 0
    for i in range(0,1500):
        num1 = (math.factorial(i)**2)*(2**(i+1))
        num2 = math.factorial(2*i +1)
        num3 = num1/num2
        print(num3)
        total += num3
    return total

def picheck(pi1):
    total = 0
    pi2 = str(pi1)
    pi3 = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783"
    for i in range(0,len(pi2)):
        if pi2[i] == pi3[i]:
            total +=1
    return total

print(pi4(),picheck(pi4))