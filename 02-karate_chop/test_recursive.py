from karate_chop_recursive import *
import unittest

class TestKarateChop(unittest.TestCase):

    def setUp(self):
        self.Chopper = KarateChopRecursive([], 0)

    def test_chop_uneven(self):
        self.assertEqual(self.Chopper.chop(3, [1, 2, 3]), 2)

    def test_chop_even(self):
        self.assertEqual(self.Chopper.chop(3, [2, 3]), 1)
        self.assertEqual(self.Chopper.chop(2, [2, 3]), 0)


    def test_chop(self):
        self.assertEqual(self.Chopper.chop(3, []), -1)
        self.assertEqual(self.Chopper.chop(3, [1]), -1)
        self.assertEqual(self.Chopper.chop(1, [1]), 0)
        self.assertEqual(self.Chopper.chop(1, [1, 3, 5]), 0)
        self.assertEqual(self.Chopper.chop(3, [1, 3, 5]), 1)
        self.assertEqual(self.Chopper.chop(5, [1, 3, 5]), 2)
        self.assertEqual(self.Chopper.chop(0, [1, 3, 5]), -1)
        self.assertEqual(self.Chopper.chop(2, [1, 3, 5]), -1)
        self.assertEqual(self.Chopper.chop(4, [1, 3, 5]), -1)
        self.assertEqual(self.Chopper.chop(6, [1, 3, 5]), -1)
        self.assertEqual(self.Chopper.chop(1, [1, 3, 5, 7]), 0)
        self.assertEqual(self.Chopper.chop(3, [1, 3, 5, 7]), 1)
        self.assertEqual(self.Chopper.chop(5, [1, 3, 5, 7]), 2)
        self.assertEqual(self.Chopper.chop(7, [1, 3, 5, 7]), 3)
        self.assertEqual(self.Chopper.chop(0, [1, 3, 5, 7]), -1)
        self.assertEqual(self.Chopper.chop(2, [1, 3, 5, 7]), -1)
        self.assertEqual(self.Chopper.chop(4, [1, 3, 5, 7]), -1)
        self.assertEqual(self.Chopper.chop(6, [1, 3, 5, 7]), -1)
        self.assertEqual(self.Chopper.chop(8, [1, 3, 5, 7]), -1)

    def test_split_one_element(self):
        self.assertEqual(self.Chopper.get_end_of_left_split(1, 1), 1)

    def test_split_two_elements(self):
        self.assertEqual(self.Chopper.get_end_of_left_split(1, 2), 1)

    def test_split_even(self):
        self.assertEqual(self.Chopper.get_end_of_left_split(0, 7), 3)

    def test_split_uneven(self):
        self.assertEqual(self.Chopper.get_end_of_left_split(1, 3), 2)

    def test_get_match(self):
        chopper = KarateChopRecursive([1], 1)
        self.assertEqual(chopper.get_matching_index_or_error(0), 0)

    def test_split_is_singleton(self):
        self.assertEqual(self.Chopper.split_is_singleton(0,0), True)



if __name__ == '__main__': 
    unittest.main()


