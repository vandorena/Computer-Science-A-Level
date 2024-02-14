import math

def prime_checker(input, list_of_known_primes):
    test_list = []
    for i in range(0,len(list_of_known_primes)):
        if input%list_of_known_primes[i] != 0 and input != list_of_known_primes[i]:
            test_list.append(True)
        else:
            return False
list_primes = []
holder = False
while not holder:
    user_input = int("Enter max: ")
    for i in range(0,user_input):
        if prime_checker(i, list_primes)
    