"""Split a list of numbers into two lists, one for even and one for odd"""

def even_odd_split(numbers):
    l_even = []
    l_odd = []
    for num in numbers:
        if num % 2 == 0:
            l_even.append(num)
        else:
            l_odd.append(num)
    return l_even, l_odd


numbers = [1, 2, 3, 4, 5, 6]
even, odd = even_odd_split(numbers)
print(even)
print(odd)