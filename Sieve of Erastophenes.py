known_primes = [2,3,5,7,13,17,23]

def prime_checker_bool(number,known_primes):
    if number < 2:
        return
    if number in known_primes:
        return
    number_sqrt = number**0.5
    halt_test = False
    iterator = 0
    while not halt_test:
        if known_primes[iterator] <  number_sqrt and (number % known_primes[iterator]) == 0:
            return
        elif known_primes[iterator] < number_sqrt and (number % known_primes[iterator]) != 0:
            iterator += 1
        else:
            known_primes.append(number)
            return
            
            
                

for i in range(0,1000000):
    prime_checker_bool(i,known_primes)
print(known_primes)