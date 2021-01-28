import pytest
from sort import sort

def test_sort():
    l = [3, 5, 6, 1, 2]
    expected = [1, 2, 3, 5, 6]
    assert sort(l) == expected
