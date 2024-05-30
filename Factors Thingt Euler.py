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

def new_prime_list(inputts):
    prime_list =[]
    for i in range(1,int(math.sqrt(inputts))):
        if number_checker(i) == False:
            prime_list.append(i)

    return prime_list

def find_factors(prime_list,input_num):
    current_number = input_num
    holder_list = []
    for i in range(0,len(prime_list)):
        if (current_number / prime_list[i]).is_integer():
            holder_list.append(prime_list[i])
            current_number = (current_number/prime_list[i])
    holder_list.sort(reverse=True)
    return holder_list[0]
            



listsss = new_prime_list(1000000000)
print(find_factors(listsss,(600851475143/(6857*1471))))






