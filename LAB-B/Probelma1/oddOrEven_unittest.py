'''
Created on 08/02/2018

@author: juavarga
'''
import unittest
from oddOrEven import isOddOrEven
from oddOrEven import checkIsDivisible


class oddOrEven_unittest(unittest.TestCase):
    def test_case_even(self):
            self.assertEqual( isOddOrEven(2) , "2 is even.")
    def test_case_four(self):
            self.assertEqual( isOddOrEven(4) , "4 is multiple of four.")
    def test_case_odd(self):
            self.assertEqual( isOddOrEven(5) , "5 is odd.")
    def test_case_divisible1(self):
            self.assertEqual( checkIsDivisible("10","5") , "10 can be divided evenly by 5")
    def test_case_divisible2(self):
            self.assertEqual( checkIsDivisible("5","3") , "5 cannot be divided evenly by 3")

 
if __name__ == '__main__':
    unittest.main()
