"""Given a list, output a new list where the next number in the list is the cumulative of the numbers before and including itself"""

def cumulative_sum(numbers):
    cumulative_list = [numbers[0]]
    curr = numbers[0]
    for i in range(1, len(numbers)):
        curr += numbers[i]
        cumulative_list.append(curr)
    return cumulative_list
        

numbers =  [1, 2, 3, 4]
print(cumulative_sum(numbers))
