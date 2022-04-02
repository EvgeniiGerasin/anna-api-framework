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

    def test_asserts(self):
        types = [
            'equality', 'inequality',
            'count_compration', 'contains'
        ]
        a = Assert()
        for type in types:
            if type == 'equality':
                got = a.equality(1, 1, 'Error')
                want = None
                self.assertEqual(got, want, f'got {got} want {want}')
            elif type == 'count_compration':
                got = a.count_compration(2, 1, 'Error')
                want = None
                self.assertEqual(got, want, f'got {got} want {want}')
            elif type == 'contains':
                got = a.contains('32', '554632', 'Error')
                want = None
                self.assertEqual(got, want, f'got {got} want {want}')
            elif type == 'inequality':
                got = a.inequality(1, 3, 'Error')
                want = None
                self.assertEqual(got, want, f'got {got} want {want}')
