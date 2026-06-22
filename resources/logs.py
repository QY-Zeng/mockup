from flask import Blueprint
from flask import jsonify

from models.event_log import event_log

bp = Blueprint(
    "logs",
    __name__
)


@bp.route(
    "/redfish/v1/Managers/BMC/LogServices",
    methods=["GET"]
)
def logservices():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Managers/BMC/LogServices",

        "Members": [

            {
                "@odata.id":
                "/redfish/v1/Managers/BMC/LogServices/EventLog"
            }

        ],

        "Members@odata.count": 1
    })


@bp.route(
    "/redfish/v1/Managers/BMC/LogServices/EventLog",
    methods=["GET"]
)
def eventlog():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Managers/BMC/LogServices/EventLog",

        "Id":
        "EventLog",

        "Name":
        "System Event Log",

        "Entries": {

            "@odata.id":
            "/redfish/v1/Managers/BMC/LogServices/EventLog/Entries"
        }
    })


@bp.route(
    "/redfish/v1/Managers/BMC/LogServices/EventLog/Entries",
    methods=["GET"]
)
def entries():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Managers/BMC/LogServices/EventLog/Entries",

        "Members":
        event_log.get_entries(),

        "Members@odata.count":
        len(event_log.get_entries())
    })