def binary_search_function(list,search_item):
    upper = len(list) - 1
    lower = 0
    found = False
    while not found and upper>=lower:
        midpoint = ((upper-lower)//2)+ lower
        if list[midpoint] == search_item:
            found = True
            return midpoint
        elif list[midpoint] > search_item:
            upper = midpoint
        else:
            lower = midpoint
        if list[-1] == search_item:
            return len(list) - 1
        print(midpoint)

list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search_function(list,10))