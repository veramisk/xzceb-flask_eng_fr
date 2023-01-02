import unittest
from translator import english_to_french, frenchToEnglish

def test_en_to_fr(self):
    self.assertEqual(english_to_french('Null'), 'Null')
    self.assertEqual(english_to_french('Hello'), 'Bonjour')

def test_fr_to_en(self):
    self.assertEqual(frenchToEnglish('Null'), 'Null')
    self.assertEqual (frenchToEnglish('Bonjour'), 'Hello')

unittest.main()