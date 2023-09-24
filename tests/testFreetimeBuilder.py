import unittest
from freetime_builder import build_free_times
from calendar_object import CalendarObject


class TestFreetimeBuilder(unittest.TestCase):
    def test_build_free_times(self):
        # Test case 1
        busy_times = [
            CalendarObject('busy1', '2022-01-01 10:00:00', '2022-01-01 12:00:00'),
            CalendarObject('busy2', '2022-01-01 14:00:00', '2022-01-01 16:00:00')
        ]
        start_time = '2022-01-01 08:00:00'
        end_time = '2022-01-01 18:00:00'
        expected_output = [
            CalendarObject('free', '2022-01-01 08:00:00', '2022-01-01 10:00:00'),
            CalendarObject('free', '2022-01-01 12:00:00', '2022-01-01 14:00:00'),
            CalendarObject('free', '2022-01-01 16:00:00', '2022-01-01 18:00:00')
        ]
        self.assertEqual(build_free_times(busy_times, start_time, end_time), expected_output)
        
        # Test case 2
        busy_times = [
            CalendarObject('busy1', '2022-01-01 10:00:00', '2022-01-01 12:00:00'),
            CalendarObject('busy2', '2022-01-01 14:00:00', '2022-01-01 16:00:00')
        ]
        start_time = '2022-01-01 09:00:00'
        end_time = '2022-01-01 17:00:00'
        expected_output = [
            CalendarObject('free', '2022-01-01 09:00:00', '2022-01-01 10:00:00'),
            CalendarObject('free', '2022-01-01 12:00:00', '2022-01-01 14:00:00'),
            CalendarObject('free', '2022-01-01 16:00:00', '2022-01-01 17:00:00')
        ]
        self.assertEqual(build_free_times(busy_times, start_time, end_time), expected_output)
        
        # Test case 3
        busy_times = [
            CalendarObject('busy1', '2022-01-01 10:00:00', '2022-01-01 12:00:00'),
            CalendarObject('busy2', '2022-01-01 14:00:00', '2022-01-01 16:00:00')
        ]
        start_time = '2022-01-01 08:00:00'
        end_time = '2022-01-01 15:00:00'
        expected_output = [
            CalendarObject('free', '2022-01-01 08:00:00', '2022-01-01 10:00:00'),
            CalendarObject('free', '2022-01-01 12:00:00', '2022-01-01 14:00:00')
        ]
        self.assertEqual(build_free_times(busy_times, start_time, end_time), expected_output)


if __name__ == '__main__':
    unittest.main()
