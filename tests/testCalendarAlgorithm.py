import unittest
from calendar_algorithm import find_busy_times, build_free_times
from calendar_object import CalendarObject


class TestCalendarAlgorithm(unittest.TestCase):
    def test_find_busy_times(self):
        # Test case 1
        calendar1 = [
            CalendarObject('event1', '2022-01-01 10:00:00', '2022-01-01 12:00:00'),
            CalendarObject('event2', '2022-01-01 14:00:00', '2022-01-01 16:00:00')
        ]
        calendar2 = [
            CalendarObject('event3', '2022-01-01 11:00:00', '2022-01-01 13:00:00'),
            CalendarObject('event4', '2022-01-01 15:00:00', '2022-01-01 17:00:00')
        ]
        expected_output = [
            CalendarObject('busy', '2022-01-01 11:00:00', '2022-01-01 12:00:00'),
            CalendarObject('busy', '2022-01-01 15:00:00', '2022-01-01 16:00:00')
        ]
        self.assertEqual(find_busy_times(calendar1, calendar2), expected_output)
        
        # Test case 2
        calendar1 = [
            CalendarObject('event1', '2022-01-01 10:00:00', '2022-01-01 12:00:00'),
            CalendarObject('event2', '2022-01-01 14:00:00', '2022-01-01 16:00:00')
        ]
        calendar2 = [
            CalendarObject('event3', '2022-01-01 16:00:00', '2022-01-01 18:00:00'),
            CalendarObject('event4', '2022-01-01 19:00:00', '2022-01-01 20:00:00')
        ]
        expected_output = []
        self.assertEqual(find_busy_times(calendar1, calendar2), expected_output)
        
        # Test case 3
        calendar1 = [
            CalendarObject('event1', '2022-01-01 10:00:00', '2022-01-01 12:00:00'),
            CalendarObject('event2', '2022-01-01 14:00:00', '2022-01-01 16:00:00')
        ]
        calendar2 = [
            CalendarObject('event3', '2022-01-01 12:30:00', '2022-01-01 13:30:00'),
            CalendarObject('event4', '2022-01-01 16:30:00', '2022-01-01 17:30:00')
        ]
        expected_output = [
            CalendarObject('busy', '2022-01-01 12:30:00', '2022-01-01 13:30:00')
        ]
        self.assertEqual(find_busy_times(calendar1, calendar2), expected_output)

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
        end_time = '2022-01-01 20:00:00'
        expected_output = [
            CalendarObject('free', '2022-01-01 08:00:00', '2022-01-01 10:00:00'),
            CalendarObject('free', '2022-01-01 12:00:00', '2022-01-01 14:00:00'),
            CalendarObject('free', '2022-01-01 16:00:00', '2022-01-01 20:00:00')
        ]
        self.assertEqual(build_free_times(busy_times, start_time, end_time), expected_output)


if __name__ == '__main__':
    unittest.main()
