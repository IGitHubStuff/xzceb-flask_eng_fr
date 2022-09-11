import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
  def test_englishToFrench(self):
    self.assertEqual(english_to_french(None), '')
    self.assertEqual(english_to_french('Hello'), 'Bonjour')
    self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
    #testing english to french Hello/Goodbye to Bonjour/Au revoir

  def test_frenchToEnglish(self):
    self.assertEqual(french_to_english(None), '')
    self.assertEqual(french_to_english('Bonjour'), 'Hello')
    self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
    #testing french to english Bonjour/Au revoir to Hello/Goodbye

if __name__ =='__main__':
  unittest.main()