import unittest
from anna.actions import Action
from anna.asserts import Assert


class TestAnna(unittest.TestCase):

    def test_request(self):
        methods = ['GET', ]
        for method in methods:
            action = Action('http://ya.ru')
            responce = action.request(method)
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
