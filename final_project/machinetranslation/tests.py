import unittest
class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual("Hello","Bonjour")
    def test_french_to_english(self):
        self.assertEqual("Bonjour","Hello")

if __name__=='__main__':
    unittest.main()