import unittest
from app.search import search

class TestSearch(unittest.TestCase):
    def testSearch(self):
        dictionary = set(open("words.txt", 'r').read().lower().splitlines())
        charsets = [
            ['o','n','i','l','x','f', 'e'],
            ['i','w','c','d','l','n', 'e'],
            ['i','s','n','t','g','r', 'e'],
            ['n','o','x','p','i','r', 'e']
        ]

        # Test different characters do not return 0
        for chars in charsets:
            result = search(dictionary, chars, 'e')
            self.assertNotEqual(result, 0)


if __name__ == "__main__":
    unittest.main()