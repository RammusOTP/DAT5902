"""Return the sum of all multiples of 3 or 5 below given number n"""

def multiples_sum(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    
    return result

print(multiples_sum(int(input("Enter a number: "))))

"""Alternative solution from ChatGPT"""

def multiples_sum(n):
    return sum(i for i in range(0, n) if i % 3 == 0 or i % 5 == 0)
