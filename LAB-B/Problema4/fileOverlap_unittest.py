'''
Created on 08/02/2018

@author: juavarga
'''
import unittest
from fileOverlap import checkOverlapped

class fileOverLap_unittest(unittest.TestCase):
    def test_case_even(self):
            self.assertEqual( checkOverlapped() , [7, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263, 293, 313, 331, 367, 379, 383, 397, 409, 487, 563, 617, 653, 673, 683, 709, 739, 761, 863, 881, 907, 937])
            
if __name__ == '__main__':
    unittest.main()
