print("For 200 URLs type 1")
print("for 1000 URLs type 2")
print("for 300000 URLs type 3")
print("For 1 000 000 URLs type 4")
howmanyurls = int.input("Select Options: ")

if howmanyurls == 1:
    urlcount = 200
elif howmanyurls == 2:
    urlcount = 1000
elif howmanyurls == 3:
    urlcount = 300000
elif howmanyurls == 4:
    urlcount = 1000000

with open ("URLlist.txt", "a") as targetfile:
    targetfile.write("hello")