"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if(number_of_primes < 1):
        raise ValueError("Only positive numbers are allowed.")
    
    list = []
    primes_calculated = 0
    number = 0

    while primes_calculated < number_of_primes:
        factors = 1

        for i in range(1, number):
            if number % i == 0:
                factors += 1
        
        if factors == 2:
            primes_calculated += 1
            list.append(number)

        number += 1

    return list
