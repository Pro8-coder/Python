from seminar2_task7_additional import num, result
from unittest import TestCase


class TestSeminar2Task7Additional(TestCase):

    def test_seminar2_task7_additional_type(self):
        self.assertIsInstance(num, list)
        self.assertIsInstance(result, int)

    def test_seminar2_task7_additional_result(self):
        self.assertEqual(result, 13)
