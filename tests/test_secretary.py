import unittest
from main import secretary_people,secretary_add,secretary_delete

class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        pass

    def test_secretary_people(self):
        self.assertEqual(secretary_people('2207 876234'), 'Василий Гупкин')

    def test_secretary_add(self):
        self.assertEqual(secretary_add('passport', '1122 445566', 'Кеша', "2"), {'type': 'passport', 'number': '1122 445566', 'name': 'Кеша'})

    def test_secretary_delete(self):
        self.assertTrue(secretary_delete('10006'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()