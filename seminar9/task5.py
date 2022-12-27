from seminar7_task5 import Pen, Pencil, Handle
from unittest import TestCase


class TestSeminar7Task5(TestCase):

    def test_pen(self):
        self.assertEqual(Pen.title, 'ручка')

    def test_Pencil(self):
        self.assertNotEqual(Pencil.title, 'ручка')
        self.assertEqual(Pencil.title, 'карандаш')

    def test_Handle(self):
        self.assertNotEqual(Handle.title, 'ручка')
        self.assertNotEqual(Handle.title, 'карандаш')
        self.assertEqual(Handle.title, 'маркер')
