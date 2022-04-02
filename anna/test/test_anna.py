import unittest
from anna.actions import Action


class TestAnna(unittest.TestCase):

    def test_request(self):
        methods = ['GET',]
        for method in methods:
            action = Action('http://ya.ru')
            responce = action.request(method)
            self.assertEqual(
                responce.status_code,
                200,
                'Status code is not 200 with method {}'.format(method)
            )
