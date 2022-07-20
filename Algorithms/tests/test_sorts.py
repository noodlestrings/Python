import sys
import unittest

sys.path.append("/Users/sam/Programming/Python/Algorithms")
from bubblesort import bubblesort
from InsertionSortIMPROVED import insertionsort


class TestCalc(unittest.TestCase):
    def test_bubblesort_standard(self):
        unsorted = [4, 2, 6, 4, 4, 3, 8, 6]
        target = [2, 3, 4, 4, 4, 6, 6, 8]
        self.assertListEqual(bubblesort(unsorted), target)

    def test_bubblesort_somenegs(self):
        unsorted = [4, 2, -6, 4, -4, 3, -8, 6]
        target = [-8, -6, -4, 2, 3, 4, 4, 6]
        self.assertListEqual(bubblesort(unsorted), target)

    def test_bubblesort_allnegs(self):
        unsorted = [-4, -2, -6, -4, -4, -3, -8, -6]
        target = [-8, -6, -6, -4, -4, -4, -3, -2]
        self.assertListEqual(bubblesort(unsorted), target)

    def test_bubblesort_allsame(self):
        unsorted = [23, 23, 23, 23, 23, 23]
        target = [23, 23, 23, 23, 23, 23]
        self.assertListEqual(bubblesort(unsorted), target)

    def test_bubblesort_allsame_butone(self):
        unsorted = [23, 23, 23, 23, 23, 0]
        target = [0, 23, 23, 23, 23, 23]
        self.assertListEqual(bubblesort(unsorted), target)



    def test_insertionsort_standard(self):
        unsorted = [4, 2, 6, 4, 4, 3, 8, 6]
        target = [2, 3, 4, 4, 4, 6, 6, 8]
        self.assertListEqual(insertionsort(unsorted), target)

    def test_insertionsort_somenegs(self):
        unsorted = [4, 2, -6, 4, -4, 3, -8, 6]
        target = [-8, -6, -4, 2, 3, 4, 4, 6]
        self.assertListEqual(insertionsort(unsorted), target)

    def test_insertionsort_allnegs(self):
        unsorted = [-4, -2, -6, -4, -4, -3, -8, -6]
        target = [-8, -6, -6, -4, -4, -4, -3, -2]
        self.assertListEqual(insertionsort(unsorted), target)

    def test_insertionsort_allsame(self):
        unsorted = [23, 23, 23, 23, 23, 23]
        target = [23, 23, 23, 23, 23, 23]
        self.assertListEqual(insertionsort(unsorted), target)

    def test_insertionsort_allsame_butone(self):
        unsorted = [23, 23, 23, 23, 23, 0]
        target = [0, 23, 23, 23, 23, 23]
        self.assertListEqual(insertionsort(unsorted), target)

if __name__ == "__main__":
    unittest.main()
