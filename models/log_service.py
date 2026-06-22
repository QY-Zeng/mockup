from models.event_log import event_log


class EventLogService:

    def to_redfish(self):

        return {
            "@odata.id": "/redfish/v1/Systems/System1/LogServices",
            "@odata.type": "#LogServiceCollection.LogServiceCollection",
            "Name": "Log Services",
            "Members": [
                {
                    "@odata.id": "/redfish/v1/Systems/System1/LogServices/EventLog"
                }
            ],
            "Members@odata.count": 1
        }


class EventLogResource:

    def to_redfish(self):

        return {
            "@odata.id": "/redfish/v1/Systems/System1/LogServices/EventLog",
            "@odata.type": "#LogService.v1_1_0.LogService",
            "Id": "EventLog",
            "Name": "System Event Log",
            "Entries": {
                "@odata.id": "/redfish/v1/Systems/System1/LogServices/EventLog/Entries"
            }
        }


class EventLogEntries:

    def to_redfish(self):

        return {
            "@odata.id": "/redfish/v1/Systems/System1/LogServices/EventLog/Entries",
            "@odata.type": "#LogEntryCollection.LogEntryCollection",
            "Members": [
                {
                    "Id": str(i),
                    "Message": e["message"],
                    "Severity": e["severity"]
                }
                for i, e in enumerate(event_log.logs)
            ],
            "Members@odata.count": len(event_log.logs)
        }


log_service = EventLogService()
event_log_resource = EventLogResource()
event_log_entries = EventLogEntries()