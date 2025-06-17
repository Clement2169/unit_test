import pytest
import sort

def test_sort_increasing():
    assert sort.sorting([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_sort_decreasing():
    assert sort.sorting([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], increasing=False) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
