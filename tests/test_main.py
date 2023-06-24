import unittest
# from src import main

import sys
sys.path.append('..')
import main


class TestFunc(unittest.TestCase):
    def test_func(self):
        expected = 'Hello World'
        actual = main.func()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
