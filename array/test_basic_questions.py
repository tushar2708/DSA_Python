from unittest import TestCase

from array import basic_questions


class TestBasicQuestions(TestCase):

    def test_max_contiguous_subarray_sum(self):
        res = basic_questions.max_contiguous_subarray_sum([1, 2, 3, -2, 5])
        self.assertEqual(9, res)
        res = basic_questions.max_contiguous_subarray_sum([-1, -2, -3, -4])
        self.assertEqual(-1, res)

    def test_missing_number(self):
        res = basic_questions.missing_number([1, 2, 3, 5])
        self.assertEqual(4, res)
        res = basic_questions.missing_number([1, 2, 3, 4, 5, 7])
        self.assertEqual(6, res)

    def test_contiguous_subarray_with_given_sum(self):
        res = basic_questions.contiguous_subarray_with_given_sum([1, 2, 3, 7, 5], 12)
        self.assertEqual((2, 4), res)
        res = basic_questions.contiguous_subarray_with_given_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
        self.assertEqual((1, 5), res)
        x = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"
        arr = list(map(int, x.split()))
        # print(arr)
        res = basic_questions.contiguous_subarray_with_given_sum(arr, 468)
        self.assertEqual((38, 42), res)

    def test_sort_array_of_0_1_2(self):
        res = basic_questions.sort_array_of_0_1_2([0, 2, 0, 1, 0, 0, 2, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1, 1, 1, 2, 2])
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], res)

    def test_find_equilibrium_point(self):
        res = basic_questions.find_equilibrium_point([1, 3, 5, 2, 2])
        self.assertEqual(2, res)
        res = basic_questions.find_equilibrium_point([1])
        self.assertEqual(0, res)

        a = "20 17 42 25 32 32 30 32 37 9 2 33 31 17 14 40 9 12 36 21 8 33 6 6 10 37 12 26 21 3"
        arr = list(map(int, a.split()))
        res = basic_questions.find_equilibrium_point(arr)
        self.assertEqual(12, res)

