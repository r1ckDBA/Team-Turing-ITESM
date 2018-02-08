import unittest
from listAnalysis3 import isPalindrome

class listAnalysis_unittest(unittest.TestCase):
	def test_case_example(self):
		self.assertTrue( isPalindrome("Anita lava la tina") )
 	def test_case_example_single(self):
 		self.assertTrue( isPalindrome( "oso" ))
 	def test_case_negative(self):
 		self.assertFalse( isPalindrome( "fsdr" ))
 
if __name__ == '__main__':
    unittest.main()