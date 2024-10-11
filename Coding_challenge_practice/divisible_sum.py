"""Given a list and a number
    Find the sum of all the numbers in the list that are divisible by the given number"""


def divisible_sum(l, n):
    total = 0
    for i in range(len(l)):
        if l[i] % n == 0:
            total += l[i]

    return total

numbers = [10, 15, 20, 25, 30]
n = 5

print(divisible_sum(numbers, n))