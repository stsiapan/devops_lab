#!/usr/bin/env python

import unittest
from .task5 import n, list1


class TestTask(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_Buzz(self):
        self.assertEqual(list1[4], 'Buzz')

    def test_Fizz(self):
        self.assertEqual(list1[2], 'Fizz')

    def test_FizzBuzz(self):
        self.assertEqual(list1[14], 'FizzBuzz')

    def test_n(self):
        self.assertEqual(n, 15)

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
