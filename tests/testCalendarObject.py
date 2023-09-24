import unittest
from calendar_object import CalendarObject


class TestCalendarObject(unittest.TestCase):
    def test_get_event_id(self):
        # Test case 1
        event_id = 'event1'
        start_time = '2022-01-01 10:00:00'
        end_time = '2022-01-01 12:00:00'
        calendar_object = CalendarObject(event_id, start_time, end_time)
        self.assertEqual(calendar_object.get_event_id(), event_id)
        
        # Test case 2
        event_id = 'event2'
        start_time = '2022-01-01 14:00:00'
        end_time = '2022-01-01 16:00:00'
        calendar_object = CalendarObject(event_id, start_time, end_time)
        self.assertEqual(calendar_object.get_event_id(), event_id)
        
        # Test case 3
        event_id = 'event3'
        start_time = '2022-01-01 18:00:00'
        end_time = '2022-01-01 19:00:00'
        calendar_object = CalendarObject(event_id, start_time, end_time)
        self.assertEqual(calendar_object.get_event_id(), event_id)


if __name__ == '__main__':
    unittest.main()
