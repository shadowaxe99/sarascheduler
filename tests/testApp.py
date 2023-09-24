import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api(self):
        # Test case 1
        data = {'message': 'Hello, EmberAIBot!'}
        response = self.app.post('/api', json=data)
        self.assertEqual(response.status_code, 200)
        
        # Test case 2
        data = {'message': 'How are you, EmberAIBot?'}
        response = self.app.post('/api', json=data)
        self.assertEqual(response.status_code, 200)
        
        # Test case 3
        data = {'message': 'Goodbye, EmberAIBot!'}
        response = self.app.post('/api', json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
