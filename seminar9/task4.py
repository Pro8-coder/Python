from seminar2_task7_additional import num, result
from unittest import TestCase


class TestSeminar2Task7Additional(TestCase):

    def test_seminar2_task7_additional_type_num(self):
        self.assertIsInstance(num, list)

    def test_seminar2_task7_additional_type_result(self):
        self.assertIsInstance(result, int)

    def test_seminar2_task7_additional_result(self):
        self.assertEqual(result, 13)
