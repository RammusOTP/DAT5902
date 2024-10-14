"""Remove duplicates from a list"""

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers)) 