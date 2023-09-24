import unittest
from EmailParser import parse_email

class TestEmailParser(unittest.TestCase):
    def test_parse_email(self):
        # Test case 1
        email = 'Subject: Test Subject\nFrom: test@example.com\nBody: This is a test email.'
        expected_output = {
            'subject': 'Test Subject',
            'sender': 'test@example.com',
            'body': 'This is a test email.'
        }
        self.assertEqual(parse_email(email), expected_output)
        
        # Test case 2
        email = 'Subject: Another Subject\nFrom: another@example.com\nBody: This is another test email.'
        expected_output = {
            'subject': 'Another Subject',
            'sender': 'another@example.com',
            'body': 'This is another test email.'
        }
        self.assertEqual(parse_email(email), expected_output)
        
        # Test case 3
        email = 'Subject: No Body\nFrom: nobody@example.com'
        expected_output = {
            'subject': 'No Body',
            'sender': 'nobody@example.com',
            'body': None
        }
        self.assertEqual(parse_email(email), expected_output)


if __name__ == '__main__':
    unittest.main()
