import unittest
from api_calls import send_request


class TestApiCalls(unittest.TestCase):
    def test_send_request(self):
        # Test case 1
        url = 'https://api.example.com'
        data = {'message': 'Hello, API!'}
        expected_output = {'response': 'Success'}
        self.assertEqual(send_request(url, data), expected_output)
        
        # Test case 2
        url = 'https://api.example.com'
        data = {'message': 'How are you, API?'}
        expected_output = {'response': 'Success'}
        self.assertEqual(send_request(url, data), expected_output)
        
        # Test case 3
        url = 'https://api.example.com'
        data = {'message': 'Goodbye, API!'}
        expected_output = {'response': 'Success'}
        self.assertEqual(send_request(url, data), expected_output)


if __name__ == '__main__':
    unittest.main()
