import math

def number_checker(input_number):
    if input_number < 1:
        print("Not greater than 1")
    
    number_results_list = []
    input_number_sqrt = round(input_number**0.5)
    for i in range(2,input_number_sqrt):
        if i != input_number:
            number_results_list.append(input_number%i)
    if 0 in number_results_list:
        print("Is not prime")
    else:
        print("Is prime")

holder = False
while not holder:
    user_input_number = int(input("Input a number to see if it is prime: "))
    number_checker(user_input_number)