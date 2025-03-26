import unittest
from app.search import Search

class TestSearch(unittest.TestCase):
    def testSearch(self):
        words = [
            "Again",
            "Having",
            "Going",
            "Tried",
            "Specialized", # US spelling
            "Specialised", # UK spelling
            "Antidisestablishmentarianism"
        ]

        for word in words:
            search = Search(word, "words.txt")
            result = search.search()
            self.assertTrue(result, 1)


if __name__ == "__main__":
    unittest.main()