import unittest
from src import main


class TestFunc(unittest.TestCase):
    def test_func(self):
        expected = 'Hello World'
        actual = main.func()
        self.assertEqual(expected, actual)

    def test_func2(self):
        expected = 'Hello yamada'
        actual = main.func2('yamada')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
