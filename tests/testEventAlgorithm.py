import unittest
from event_algorithm_v_1 import calculate_event_duration


class TestEventAlgorithm(unittest.TestCase):
    def test_calculate_event_duration(self):
        # Test case 1
        start_time = '2022-01-01 10:00:00'
        end_time = '2022-01-01 12:00:00'
        expected_output = 120
        self.assertEqual(calculate_event_duration(start_time, end_time), expected_output)
        
        # Test case 2
        start_time = '2022-01-01 14:00:00'
        end_time = '2022-01-01 16:30:00'
        expected_output = 150
        self.assertEqual(calculate_event_duration(start_time, end_time), expected_output)
        
        # Test case 3
        start_time = '2022-01-01 18:00:00'
        end_time = '2022-01-01 19:30:00'
        expected_output = 90
        self.assertEqual(calculate_event_duration(start_time, end_time), expected_output)


if __name__ == '__main__':
    unittest.main()
