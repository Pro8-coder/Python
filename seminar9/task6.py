from seminar4_task2 import lst, new_lst
from unittest import TestCase


class TestSeminar4Task2(TestCase):

    def test_is(self):
        for i in new_lst:
            self.assertIn(i, lst)
