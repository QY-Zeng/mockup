from datetime import datetime


class EventLog:

    def __init__(self):

        self.entries = []

    def add(self, message, severity="OK"):

        if len(self.entries) > 0:

            if self.entries[-1]["Message"] == message:
                return

        self.entries.append({

            "Id":
            str(len(self.entries) + 1),

            "Created":
            datetime.utcnow().isoformat(),

            "Severity":
            severity,

            "Message":
            message
        })

    def get_entries(self):

        return self.entries


event_log = EventLog()