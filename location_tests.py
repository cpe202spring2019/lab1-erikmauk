import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")

        loc2 = Location("San Fransisco", 37.7, 122.4)
        self.assertEqual(repr(loc2),"Location('San Fransisco', 37.7, 122.4)")

        loc3 = Location("New York", 40.7, 74.0)
        self.assertEqual(repr(loc3),"Location('New York', 40.7, 74.0)")

        loc4 = Location("Orlando", 28.5, 81.4)
        self.assertEqual(repr(loc4),"Location('Orlando', 28.5, 81.4)")



    # Add more tests!
    def test_eq(self):
        test_loc = Location("SLO", 35.3, -120.7)

        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, test_loc)
        loc2 = Location("SLO", 35.5, -120.7)
        self.assertNotEqual(loc2, test_loc)
        loc3 = Location("SLO", 40.3, -120.7)
        self.assertNotEqual(loc3, test_loc)
        loc4 = Location("SLO", -35.3, -120.7)
        self.assertNotEqual(loc4, test_loc)
        loc5 = Location("SLO", 35.3, -120.9)
        self.assertNotEqual(loc5, test_loc)
        loc6 = Location("SLO", 35.3, -121.7)
        self.assertNotEqual(loc6, test_loc)
        loc7 = Location("SLO", 35.3, 120.7)
        self.assertNotEqual(loc7, test_loc)    
        loc8 = Location("London", 35.3, -120.7)
        self.assertNotEqual(loc8, test_loc)




if __name__ == "__main__":
        unittest.main()
