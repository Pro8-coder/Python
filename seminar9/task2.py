from seminar3_task1 import division
from unittest import TestCase


class TestDivision(TestCase):

    def test_result_true(self):
        self.assertEqual(division(8, 2), 4)

    def test_result_zero(self):
        self.assertEqual(division(10, 0), 'На ноль нельзя делить')

    def test_result_zero_r(self):
        with self.assertRaises(ZeroDivisionError):
            10 / 0
