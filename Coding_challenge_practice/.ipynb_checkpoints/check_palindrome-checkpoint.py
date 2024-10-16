"""Check if a string is a palindrome"""

def check_palindrome(string):
    return string == string[: : -1]

print(check_palindrome("racecar"))
print(check_palindrome("hello"))