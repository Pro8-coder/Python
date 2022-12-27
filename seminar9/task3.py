from seminar7_task2 import Road
from unittest import TestCase


class TestRoad(TestCase):

    def test_mass(self):
        self.assertEqual(Road(5, 70).mass(), f'{350 * 25 * 5 / 1000} т')
