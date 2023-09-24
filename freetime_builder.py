from calendar_object import CalendarObject


def build_free_times(busy_times, start_time, end_time):
    free_times = []
    
    # Sort busy times by start time
    busy_times.sort(key=lambda x: x.get_start_time())
    
    # Add free time before the first busy time
    first_busy_time = busy_times[0]
    if start_time < first_busy_time.get_start_time():
        free_times.append(CalendarObject('free', start_time, first_busy_time.get_start_time()))
    
    # Add free time between busy times
    for i in range(len(busy_times) - 1):
        current_busy_time = busy_times[i]
        next_busy_time = busy_times[i + 1]
        
        if current_busy_time.get_end_time() < next_busy_time.get_start_time():
            free_times.append(CalendarObject('free', current_busy_time.get_end_time(), next_busy_time.get_start_time()))
    
    # Add free time after the last busy time
    last_busy_time = busy_times[-1]
    if last_busy_time.get_end_time() < end_time:
        free_times.append(CalendarObject('free', last_busy_time.get_end_time(), end_time))
    
    return free_times
