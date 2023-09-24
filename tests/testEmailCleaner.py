import unittest
from EmailCleaner import clean_email

class TestEmailCleaner(unittest.TestCase):
    def test_clean_email(self):
        # Test case 1
        email = 'Hello! This is a test email.'
        expected_output = 'hello this is a test email'
        self.assertEqual(clean_email(email), expected_output)
        
        # Test case 2
        email = 'This is another test email with special characters!@#$%^&*()'
        expected_output = 'this is another test email with special characters'
        self.assertEqual(clean_email(email), expected_output)
        
        # Test case 3
        email = 'Email with multiple spaces    between words'
        expected_output = 'email with multiple spaces between words'
        self.assertEqual(clean_email(email), expected_output)


if __name__ == '__main__':
    unittest.main()
