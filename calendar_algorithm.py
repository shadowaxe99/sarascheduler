from calendar_object import CalendarObject


def find_busy_times(calendar1, calendar2):
    busy_times = []
    
    for event1 in calendar1:
        for event2 in calendar2:
            if event1.get_start_time() < event2.get_end_time() and event1.get_end_time() > event2.get_start_time():
                start_time = max(event1.get_start_time(), event2.get_start_time())
                end_time = min(event1.get_end_time(), event2.get_end_time())
                
                busy_times.append(CalendarObject('busy', start_time, end_time))
    
    return busy_times
