import Line_graph as lg
import unittest

class TestFunction(unittest.TestCase):

    def test_load_data(self):
        result = lg.load_data("/Users/emmanuel/Documents/DAT5902/randomtextfile.txt")
        self.assertEqual(result, 'Hello World!!')
    
if __name__ == "__main__":
    unittest.main()