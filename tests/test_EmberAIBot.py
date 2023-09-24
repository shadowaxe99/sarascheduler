import unittest

from EmberAIBot import EmberAIBot


class TestEmberAIBot(unittest.TestCase):
    def setUp(self):
        self.bot = EmberAIBot()

    def test_process_email(self):
        email = 'test@example.com'
        result = self.bot.process_email(email)
        self.assertEqual(result, 'Processed email: test@example.com') if result is not None else self.fail('Result is None')

    def test_extract_entities(self):
        text = 'This is a test'
        result = self.bot.extract_entities(text)
        self.assertEqual(result, ['test']) if result is not None else self.fail('Result is None')

    def test_generate_response(self):
        entities = ['test']
        result = self.bot.generate_response(entities)
        self.assertEqual(result, 'Generated response: test') if result is not None else self.fail('Result is None')


if __name__ == '__main__':
    unittest.main()
