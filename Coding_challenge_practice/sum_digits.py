"""Sum the digits of an inputted integer"""

def sum_digits(n):
    nlist = [i for i in str(n)]
    return sum(int(j) for j in nlist)

print(sum_digits(int(input("Enter a number"))))