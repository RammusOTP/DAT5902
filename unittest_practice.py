import unittest

def count_vowels(string):
    total = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'å']
    for letter in string:
        for v in range(len(vowels)):
            if vowels[v] == letter:
                total += 1
    
    return total

class TestFunction(unittest.TestCase):

    def test_vowel_count(self):
        result = count_vowels("hello world")
        self.assertEqual(result, 3)
    
    def test_vowel_count_capitals(self):
        result = count_vowels("HELLO WORLD")
        self.assertEqual(result, 3)
    
    def test_vowel_count_mixed(self):
        result = count_vowels("HeLlO WoRlD")
        self.assertEqual(result, 3)

    def test_vowel_count_numbers(self):
        result = count_vowels("11018475013405AAAAA")
        self.assertEqual(result, 5)

    def test_vowel_count_empty(self):
        result = count_vowels("")
        self.assertEqual(result, 0)

    def test_vowel_count_no_vowels(self):
        result = count_vowels("bcdfghjklmnpqrstvwxyz")
        self.assertEqual(result, 0)

    def test_vowel_count_long_string(self):
        long_string = "This is a long string with several vowels. " * 10000
        result = count_vowels(long_string)
        self.assertEqual(result, 110000)


if __name__ == "__main__":
    unittest.main()

