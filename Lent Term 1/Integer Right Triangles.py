import math


def check_p(a,b,p):
    if math.sqrt((a**2 + b**2)).is_integer():
        if (a + b + math.sqrt(a**2 + b**2)) == p:
            return True
    return False

def for_p(p):
    count = 0
    for a in range(1,p//2):
        for b in range(p//2,1,-1):
            if check_p(a,b,p):
                count +=1
    return count

def for_max():
    big_list = []
    for i in range(1,100):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(101,200):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(201,300):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(301,400):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(401,500):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(501,600):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(601,700):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(701,800):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(801,900):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = [current_i,current_max]
    for i in range(901,1000):
        big_list.append([i,for_p(i)])
    current_i,current_max = sort_max(big_list)
    big_list = []
    return f"{current_i} max is {current_max}"

def sort_max(big_list):
    current_max = -1
    current_i = -1
    for i in range(0,len(big_list)):
        try:
            if big_list[i][1] > current_max and big_list[i][1] != 0:
                current_i = big_list[i][0]
                current_max = big_list[i][1]
        except TypeError:
            pass
    return current_i,current_max

print(for_max())
