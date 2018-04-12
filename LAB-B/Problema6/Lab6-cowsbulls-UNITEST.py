#################################
#Team turing
#Lab B.1 Program 6. Cows and bulls
#Unitest program
#################################

import unittest 
from Lab6cowsbulls import revisaVacas
from Lab6cowsbulls import revisaToros

class listAnalysis_unittest(unittest.TestCase):
    def test_case_example(self):
        self.assertEqual( revisaVacas([0,1,2,3],[5,1,5,3]),2 )
    def test_case_example(self):
        self.assertEqual( revisaToros([0,1,2,3],[3,3,3,5]),3 )
 
if __name__ == '__main__':
    unittest.main()

