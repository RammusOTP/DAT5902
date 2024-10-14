"""Check if an inputted number n is prime"""
import math

def check_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and i != 1 and i != n:
            return False
    return True

print(check_prime_number(int(input("Enter a number: "))))