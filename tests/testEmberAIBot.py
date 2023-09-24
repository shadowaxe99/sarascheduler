import unittest
from EmberAIBot import process_message


class TestEmberAIBot(unittest.TestCase):
    def test_process_message(self):
        # Test case 1
        message = 'Hello, EmberAIBot!'
        expected_output = 'Hello! How can I assist you today?'
        self.assertEqual(process_message(message), expected_output)
        
        # Test case 2
        message = 'What is the weather like today?'
        expected_output = 'The weather is sunny and warm.'
        self.assertEqual(process_message(message), expected_output)
        
        # Test case 3
        message = 'Tell me a joke!'
        expected_output = 'Why don't scientists trust atoms? Because they make up everything!'
        self.assertEqual(process_message(message), expected_output)


if __name__ == '__main__':
    unittest.main()
