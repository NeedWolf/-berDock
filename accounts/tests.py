from django.test import TestCase

class TestTests(TestCase):
    def test1(self):
        self.assertEqual(2,3)
    def test2(self):
        self.assertEqual(2,2)
    def test3(self):
        x = 5
        self.assertEqual(x,6)
    def test4(self):
        x = 5
        self.assertEqual(x,5)
