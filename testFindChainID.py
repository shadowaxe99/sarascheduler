import unittest


class TestFindChainID(unittest.TestCase):
    def test_find_chain_id(self):
        # Test case 1
        input_data = [1, 2, 3, 4, 5]
        expected_output = 1
        self.assertEqual(find_chain_id(input_data), expected_output)
        
        # Test case 2
        input_data = [5, 4, 3, 2, 1]
        expected_output = 5
        self.assertEqual(find_chain_id(input_data), expected_output)
        
        # Test case 3
        input_data = [2, 4, 1, 3, 5]
        expected_output = 2
        self.assertEqual(find_chain_id(input_data), expected_output)


if __name__ == '__main__':
    unittest.main()
