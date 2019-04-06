import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_Nones(self):
        
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        # used to check for None value being returned when an empty list is passed into the function
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)
    
    def test_max_list_iter_combos(self):
        # checks different orders of numbers in input lists
        tlist = [10, 9, 8, 4, 9]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [9, 10, 8, 5, 3]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [9, 8, 10, 4, 9]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [9, 6, 4, 10, 8]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [5, 9, 8, 4, 10]
        self.assertEqual(max_list_iter(tlist), 10)


    def test_max_list_iter_negatives(self):    
        # checks negative values
        tlist = [-1, -9, -8 , -4, -9]
        self.assertEqual(max_list_iter(tlist), -1)
        tlist = [-9, -1, -8, -5, -3]
        self.assertEqual(max_list_iter(tlist), -1)
        tlist = [-9, -8, -1, -4, -9]
        self.assertEqual(max_list_iter(tlist), -1)
        tlist = [-9, -6, -4, -1, -8]
        self.assertEqual(max_list_iter(tlist), -1)
        tlist = [-5, -9, -8, -4, -1]
        self.assertEqual(max_list_iter(tlist), -1)
    

    def test_max_list_iter_floats(self):
        # checks with floats
        tlist = [10.9, 10.1, 10.5, 10.4, 10.6]
        self.assertEqual(max_list_iter(tlist), 10.9)
        tlist = [10.1, 10.9, 10.8, 10.5, 10.3]
        self.assertEqual(max_list_iter(tlist), 10.9)
        tlist = [10.1, 10.8, 10.9, 10.5, 10.3]
        self.assertEqual(max_list_iter(tlist), 10.9)
        tlist = [10.1, 10.8, 10.5, 10.9, 10.3]
        self.assertEqual(max_list_iter(tlist), 10.9)
        tlist = [10.1, 10.8, 10.5, 10.3, 10.9]
        self.assertEqual(max_list_iter(tlist), 10.9)


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

        # checks that the returned list is the reverse of the input
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        # checks negative values
        self.assertEqual(reverse_rec([-5, -10, -15]), [-15, -10, -5])
        # checks non-sequential values
        self.assertEqual(reverse_rec([5, 15, 10]), [10, 15, 5])
        # checks list with only one value
        self.assertEqual(reverse_rec([1]), [1])
        # checks list with floats
        self.assertEqual(reverse_rec([2.2, 3.3]), [3.3, 2.2])
        # checks empty list
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        #list_val =[0,1,2,3,4,7,8,9,10]
        #low = 0
        #high = len(list_val)-1
        #self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        pass

if __name__ == "__main__":
        unittest.main()

    
