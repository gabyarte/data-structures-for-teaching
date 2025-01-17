"""Module to test the Sorting algorithms."""


from unittest import TestCase

from parameterized import parameterized

from algorithms.sorting.bubblesort import BubbleSort
from algorithms.sorting.heapsort import HeapSort
from algorithms.sorting.mergesort import MergeSort


class TestSort(TestCase):
    """Base class to test Sorting implementations."""

    @parameterized.expand(
        [
            (
                BubbleSort,
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
            ),
            (
                HeapSort,
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
            ),
            (
                MergeSort,
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
            ),
            (
                MergeSort,
                lambda x, y: x["value"] < y["value"],
                [
                    {"name": "item1", "value": 100},
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                ],
                [
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                    {"name": "item1", "value": 100},
                ],
            ),
        ]
    )
    def test_sorting(self, sorting_method, comp_func, items, expected):
        """Checks the sorting method works correctly.

        Args:
            sorting_method (Sort): The sorting method to test.
            comp_func (func): The comparisson function used by the sorting method.
            items (List): The items to sort.
            expected (List): The expected order of the items after sorting.
        """
        sorter = sorting_method(comp_func, items)
        sorted_items = sorter.sort()
        self.assertEqual(sorted_items, expected)
