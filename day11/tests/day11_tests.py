"""Unit tests for functions in day11.py"""

import pytest
from day11 import recalculate_galaxies_coordinates, dist_between_two_galaxies


@pytest.mark.parametrize(
    "galaxies,empty_rows,empty_cols,factor,expected",
    [[[(0, 3), (4, 6)], (3, 7), (2, 5, 8), 2, [(0, 4), (5, 8)]]],
)
def test_recalculate_galaxies_coordinates(
    galaxies, empty_rows, empty_cols, factor, expected
):
    """Unit tests for recalculate_galaxies_coordinates"""
    assert (
        recalculate_galaxies_coordinates(galaxies, empty_rows, empty_cols, factor)
        == expected
    )


@pytest.mark.parametrize("galaxy1,galaxy2,expected", [[(0, 4), (10, 9), 15]])
def test_dist_between_two_galaxies(galaxy1, galaxy2, expected):
    """Unit tests for dist_between_two_galaxies"""
    assert dist_between_two_galaxies(galaxy1, galaxy2) == expected
