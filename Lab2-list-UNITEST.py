#################################
#Team turing
#Lab B.1 Program 2. List confusion
#Unitest program
#################################

import unittest 
from Lab2listconfusion import comparaListas

class listAnalysis_unittest(unittest.TestCase):
	def test_case_example(self):
		self.assertEqual( comparaListas([0,1,2],[0,2]),[0,2] )
	def test_case_example(self):
		self.assertEqual( comparaListas([0,5,10],[5]),[5] )
 
if __name__ == '__main__':
    unittest.main()

