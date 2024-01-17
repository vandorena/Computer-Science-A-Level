import random
def binary_search(item, list, lower, higher):
    found = False
    print(item)
    if lower > higher:
        return False
    else:
        midpoint = (higher - lower)//2 + lower
        print(f"checked {midpoint}")
        if item == list[midpoint]:
            return True
        elif item < list[midpoint]:
            return binary_search(item, list,lower, midpoint -1)
        elif item > list[midpoint]:
            return binary_search(item,list,midpoint +1, higher)
        else:
            found = True
            
    
        
你的妈妈 = []
for i in range (0,1000):
    你的妈妈.append(random.randint(1,1000))
你的妈妈.sort()
中国共产等 = 0
while 中国共产等 != 100:
    binary_search(random.randint(0,1000),你的妈妈,0 ,len()-1)
    print("")
    print("")
    中国共产等 = 中国共产等 +1