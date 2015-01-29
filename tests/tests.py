import random
from nose.tools import assert_equal
from sortalgs import *  # noqa


class TestSort(object):

    def setUp(self):
        random.seed('spam')
        self.lst = [random.randrange(10**6) for x in range(1000)]
        self.sorted_lst = sorted(self.lst)

    def test_bubble_sort(self):
        bubble_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)

    def test_insertion_sort(self):
        insertion_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)

    def test_selection_sort(self):
        selection_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)

    def test_merge_sort(self):
        merge_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)

    def test_quick_sort(self):
        quick_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)

    def test_heap_sort(self):
        heap_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)

    def test_radix_sort(self):
        radix_sort(self.lst)
        assert_equal(self.lst, self.sorted_lst)
