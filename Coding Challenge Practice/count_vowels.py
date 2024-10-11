""""Given a string
    Count the vowels in the string"""

def count_vowels(string):
    total = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in string:
        for v in range(len(vowels)):
            if vowels[v] == letter:
                total += 1
    
    return total

print(count_vowels("hello world"))
