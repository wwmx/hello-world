from src import main


class TestFunc:
    def test_func(self):
        assert main.func() == 'Hello World'

    def test_func2(self):
        assert main.func2('Joe') == 'Hello Joe'
