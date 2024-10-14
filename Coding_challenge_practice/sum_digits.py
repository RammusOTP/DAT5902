"""Sum the digits of an inputted integer"""

def sum_digits(n):
    nlist = [i for i in str(n)]
    return sum(int(j) for j in nlist)

#print(sum_digits(int(input("Enter a number: "))))

"""Alternative solution from ChatGPT"""

def sum_digits(n):
    return sum(int(i) for i in str(abs(n))) # Forgot abs in my solution to deal with negative numbers

print(sum_digits(int(input("Enter a number: "))))