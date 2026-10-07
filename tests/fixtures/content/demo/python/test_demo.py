from unittest import TestCase
from demo import *

class T(TestCase):
    def test_double(self):
        self.assertEqual(double(2), 4)
