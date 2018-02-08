import unittest
from reverseWord5 import reverseWord

class reverseWord_unittest(unittest.TestCase):
	def test_case_example(self):
		self.assertEqual( reverseWord( "My name is Michele" ), "Michele is name My ")
 	def test_case_example_spaces(self):
 		self.assertEqual( reverseWord( "Myname isMichele" ), "isMichele Myname ")
 	def test_case_negative(self):
 		self.assertNotEqual( reverseWord( "Myname isMichele" ), "isMichele Myname fds")
 
if __name__ == '__main__':
    unittest.main()