import unittest
from ember_nlp import EmberNLP


class TestEmberNLP(unittest.TestCase):
    def test_extract_entities(self):
        # Test case 1
        ember_nlp = EmberNLP()
        text = 'I love pizza'
        expected_output = ['pizza']
        self.assertEqual(ember_nlp.extract_entities(text), expected_output)
        
        # Test case 2
        text = 'I have a cat and a dog'
        expected_output = ['cat', 'dog']
        self.assertEqual(ember_nlp.extract_entities(text), expected_output)
        
        # Test case 3
        text = 'I enjoy playing tennis'
        expected_output = ['tennis']
        self.assertEqual(ember_nlp.extract_entities(text), expected_output)


if __name__ == '__main__':
    unittest.main()
