import multiprocessing
import random
def task():
    list = []
    d = False
    while not d:    
        z = random.randint(0,10000)
        x = z**103
        list.append(z)
        for i in range(0,100000):
            currentfile = open(f"hehe{i}.txt","a")
            currentfile.write(str(list))
            currentfile.write("\n")
list = [task(),task(),task(),task(),task(),task(),task(),task(),task(),task(),task(),task()]
    

pool = multiprocessing.Pool(12)
result = multiprocessing.map_async(task,list)