import math

def number_checker(input_number):
    if input_number < 1:
        print("Not greater than 1")
    
    number_results_list = []
    for i in range(2,(input_number)):
        if i != input_number:
            number_results_list.append(input_number%i)
    if 0 in number_results_list:
        return True
    else:
        return False

holder = False
while not holder:
    prime_list = []
    count = 4
    while len(prime_list) != 10001:
        if number_checker(count) == False:
            prime_list.append(count)
        count +=1 
        print((prime_list.sort(reverse=True)))