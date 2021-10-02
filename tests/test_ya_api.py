import unittest
import ya_api


class TestYaApi(unittest.TestCase):

    def setUp(self):
        pass

    def test_create(self):
        self.assertEqual(ya_api.ya_api_create('test_homework'), 201)

    def test_read(self):
        self.assertEqual(ya_api.ya_api_read('test_homework'), 200)

    def tearDown(self):
        ya_api.ya_api_delete('test')



if __name__ == '__main__':
    unittest.main()