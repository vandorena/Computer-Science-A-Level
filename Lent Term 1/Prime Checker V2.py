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
    user_input_boundary = int(input("Input a upper boundary to find all the primes from 1 to it: "))#
    prime_list = []
    for i in range(1,user_input_boundary):
        if number_checker(i) == False:
            prime_list.append(i)

    print(prime_list)