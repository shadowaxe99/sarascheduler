import unittest
from EntityExtractionExample import extract_entities


class TestEntityExtractionExample(unittest.TestCase):
    def test_extract_entities(self):
        # Test case 1
        text = 'I love pizza'
        expected_output = ['pizza']
        self.assertEqual(extract_entities(text), expected_output)
        
        # Test case 2
        text = 'I have a cat and a dog'
        expected_output = ['cat', 'dog']
        self.assertEqual(extract_entities(text), expected_output)
        
        # Test case 3
        text = 'I enjoy playing tennis'
        expected_output = ['tennis']
        self.assertEqual(extract_entities(text), expected_output)


if __name__ == '__main__':
    unittest.main()
