from seminar7_task5 import Pen, Pencil, Handle
from unittest import TestCase


class TestSeminar7Task5(TestCase):

    def test_pen_equal(self):
        self.assertEqual(Pen.title, 'ручка')

    def test_pencil_not_equal_pen(self):
        self.assertNotEqual(Pencil.title, 'ручка')

    def test_pencil_equal(self):
        self.assertEqual(Pencil.title, 'карандаш')

    def test_handle_not_equal_pen(self):
        self.assertNotEqual(Handle.title, 'ручка')

    def test_handle_not_equal_pencil(self):
        self.assertNotEqual(Handle.title, 'карандаш')

    def test_handle_equal(self):
        self.assertEqual(Handle.title, 'маркер')
