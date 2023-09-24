class CalendarObject:
    def __init__(self, event_id, start_time, end_time):
        self.event_id = event_id
        self.start_time = start_time
        self.end_time = end_time

    def get_event_id(self):
        return self.event_id

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
