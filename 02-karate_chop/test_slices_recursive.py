import pytest
from karate_chop_slices_recursive import *

def test_end_of_first_split_even_array(): 
    assert get_end_of_first_split([1, 2]) == 0 
    assert get_end_of_first_split([1, 2, 3, 4]) == 1	

def test_end_of_first_split_uneven_array():
    assert get_end_of_first_split([1]) == 0 
    assert get_end_of_first_split([1, 2, 3]) == 1 

def test_target_in_split_range():
    assert ArrayHelper.contains_target(2, [1, 2, 3]) == True 
    assert ArrayHelper.contains_target(1, [1, 2, 3]) == True 
    assert ArrayHelper.contains_target(2, [1, 3, 5]) == True 

def test_target_not_in_split():
    assert ArrayHelper.contains_target(9, [1, 4]) == False

def test_chop_empty():
    assert KarateChopSlicesRecursive.chop(1, []) ==  -1

def test_chop_singleton():
    assert KarateChopSlicesRecursive.chop(1, [1]) == 0
    assert KarateChopSlicesRecursive.chop(1, [2]) == -1

def test_split():
    assert ArrayHelper.split([1, 2, 3], 1) == ([1, 2], [3])
    assert ArrayHelper.split([1, 2, 3, 4], 0) == ([1], [2, 3, 4])
    assert ArrayHelper.split([1, 2, 3, 4], 1) == ([1, 2], [3, 4])
    assert ArrayHelper.split([1, 2, 3, 4], 2) == ([1, 2, 3], [4])

def test_match_target():
    assert ArrayHelper.match_target(3, [3], 1) == 1
    assert ArrayHelper.match_target(3, [3, 1], 1) == 1
    assert ArrayHelper.match_target(1, [3], 1) == -1

def test_even_array():
    assert ArrayHelper.is_even_len([3, 1]) == True
    assert ArrayHelper.is_even_len([1]) == False

def test_update_index_right_split():
    # unsure about this
    assert update_global_index_right(4, 2) == 7
    assert update_global_index_right(4, 1) == 6

def test_update_index_left_split():
    # unsure about this
    assert update_global_index_left(3, 1, [0, 1, 2, 3] ) == 1
    assert update_global_index_left(4, 2, [0, 1, 2, 3, 4]) == 2

def test_chop():
    assert KarateChopSlicesRecursive.chop(3, []) ==  -1
    assert KarateChopSlicesRecursive.chop(3, [1]) ==  -1
    assert KarateChopSlicesRecursive.chop(1, [1]) ==  0
    assert KarateChopSlicesRecursive.chop(1, [1, 3, 5]) ==  0
    assert KarateChopSlicesRecursive.chop(3, [1, 3, 5]) ==  1
    assert KarateChopSlicesRecursive.chop(5, [1, 3, 5]) ==  2
    assert KarateChopSlicesRecursive.chop(0, [1, 3, 5]) ==  -1
    assert KarateChopSlicesRecursive.chop(2, [1, 3, 5]) ==  -1
    assert KarateChopSlicesRecursive.chop(4, [1, 3, 5]) ==  -1
    assert KarateChopSlicesRecursive.chop(6, [1, 3, 5]) ==  -1
    assert KarateChopSlicesRecursive.chop(1, [1, 3, 5, 7]) ==  0
    assert KarateChopSlicesRecursive.chop(3, [1, 3, 5, 7]) ==  1
    assert KarateChopSlicesRecursive.chop(5, [1, 3, 5, 7]) ==  2
    assert KarateChopSlicesRecursive.chop(7, [1, 3, 5, 7]) ==  3
    assert KarateChopSlicesRecursive.chop(0, [1, 3, 5, 7]) ==  -1
    assert KarateChopSlicesRecursive.chop(2, [1, 3, 5, 7]) ==  -1
    assert KarateChopSlicesRecursive.chop(4, [1, 3, 5, 7]) ==  -1
    assert KarateChopSlicesRecursive.chop(6, [1, 3, 5, 7]) ==  -1
    assert KarateChopSlicesRecursive.chop(8, [1, 3, 5, 7]) ==  -1

