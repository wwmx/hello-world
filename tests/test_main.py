import unittest
from src import main


class TestFunc(unittest.TestCase):
    def test_func(self):
        expected = 'Hello World'
        actual = main.func()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
