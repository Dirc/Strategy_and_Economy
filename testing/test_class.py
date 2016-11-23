'''
Created on 23 nov. 2016

@author: Eric Cornet
'''
import unittest
from libs.class_lib import Peassant, House


class Test(unittest.TestCase):
    
    def setUp(self):
        #self.man = Man()
        self.peassant = Peassant()
        self.house = House()

    def testPeassant(self):
        self.assertEqual(str(type(self.peassant)),"<type 'instance'>", "Class not of correct type")

    def testHouse(self):
        self.assertEqual(str(type(self.house)),"<type 'instance'>", "Class not of correct type")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMan']
    unittest.main()