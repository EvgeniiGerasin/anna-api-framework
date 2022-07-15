import unittest
from anna.actions import Action
from anna.asserts import Assert


class TestAnna(unittest.TestCase):

    def test_request(self):
        methods = ['GET', 'POST']
        for method in methods:
            action = Action()
            responce = action.request(method, 'http://ya.ru')
            self.assertEqual(
                responce.status_code,
                200,
                'Status code is not 200 with method {}'.format(method)
            )

    def test_asserts_not_be_equal(self):
        Assert.not_be().equal(
            1, 2, 'want 1 != 2 got {} == {}'.format(1, 2)
        )

    def test_asserts_be_equal(self):
        try:
            Assert.equal(
                1, 1, 'want 1 == 2 got {} != {}'.format(1, 2)
            )
        except AssertionError as e:
            assert False, 'want None but {}'.format(e.args)

    def test_asserts_contains(self):
        Assert.contains(
            'hello', 'hello',
            'want "hello" in "hello" got "hello" not in "hello"'
        )

    def test_asserts_not_contains(self):
        try:
            Assert.not_be().contains(
                "he", "Goodbye", 'want None but have AssertionError'
            )
        except AssertionError as e:
            assert False, 'want None but {}'.format(e.args)

    def test_compare(self):
        signs = ['=', '==', '!=', '>', '<', '>=', '<=']
        a = Assert()
        for sign in signs:
            if sign == '=':
                a.compare(1, '=', 1, 'want 1 == 1 got AssertionError')
            if sign == '==':
                a.compare(1, '==', 1, 'want 1 == 1 got AssertionError')
            elif sign == '!=':
                a.compare(1, '!=', 2, 'want 1 != 2 got AssertionError')
            elif sign == '>':
                a.compare(2, '>', 1, 'want 2 > 1 got AssertionError')
            elif sign == '<':
                a.compare(1, '<', 2, 'want 1 < 2 got AssertionError')
            elif sign == '>=':
                a.compare(1, '>=', 1, 'want 1 >= 1 got AssertionError')
            elif sign == '>=':
                a.compare(2, '>=', 1, 'want 2 >= 1 got AssertionError')
            elif sign == '<=':
                a.compare(1, '<=', 1, 'want 1 <= 1 got AssertionError')
            elif sign == '<=':
                a.compare(1, '<=', 2, 'want 1 <= 1 got AssertionError')
