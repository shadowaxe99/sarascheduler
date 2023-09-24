import unittest
from EmberBot import send_message


class TestEmberBot(unittest.TestCase):
    def test_send_message(self):
        # Test case 1
        message = 'Hello, EmberBot!'
        expected_output = 'Message sent successfully'
        self.assertEqual(send_message(message), expected_output)
        
        # Test case 2
        message = 'How are you, EmberBot?'
        expected_output = 'Message sent successfully'
        self.assertEqual(send_message(message), expected_output)
        
        # Test case 3
        message = 'Goodbye, EmberBot!'
        expected_output = 'Message sent successfully'
        self.assertEqual(send_message(message), expected_output)


if __name__ == '__main__':
    unittest.main()
