from dsa_learning.binary_search import binary_search


def test_lower_edge():
    assert binary_search([5, 6, 7, 8], 5) == 0


def test_upper_edge():
    assert binary_search([5, 6, 7, 8], 8) == 3


def test_mid():
    assert binary_search([5, 6, 7, 8], 6) == 1


def test_out_of_range():
    assert binary_search([5, 6, 7, 8], 100) is None
