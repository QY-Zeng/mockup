"""
專門管理：

/redfish/v1/Systems
/redfish/v1/Systems/System1
/redfish/v1/Systems/System1/Actions/ComputerSystem.Reset





"""

from flask import Blueprint
from flask import jsonify
from flask import request

import time

from models.system import system
from models.event_log import event_log
from models.processor import cpu1

from models.memory import memory
from models.log_service import log_service, event_log_resource, event_log_entries
from models.bios import bios
from models.bios_settings import bios_settings

bp = Blueprint(
    "systems",
    __name__
)


@bp.route(
    "/redfish/v1/Systems",
    methods=["GET"]
)
def systems():

    return jsonify({

        

        "@odata.type":"#ComputerSystemCollection.ComputerSystemCollection",

        "Name":"Computer System Collection",
        
        "Members@odata.count": 1,
        
        "Members": [

            {
                "@odata.id":"/redfish/v1/Systems/System1"
            }

        ],
        
        "@odata.id":"/redfish/v1/Systems"
        
    })



@bp.route(
    "/redfish/v1/Systems/System1",
    methods=["GET"]
)
def system1():

    return jsonify(
        system.to_redfish()
    )



    

@bp.route(
    "/redfish/v1/Systems/System1/Actions/ComputerSystem.Reset",
    methods=["POST"]
)
def reset_system():

    from models.system import system
    from models.event_log import event_log

    data = request.json or {}

    reset_type = data.get("ResetType", "ForceRestart")

    if reset_type == "On":

        system.power_state = "On"

        event_log.add("System Power On", "OK")

    elif reset_type == "ForceOff":

        system.power_state = "Off"

        event_log.add("System ForceOff", "Warning")

    elif reset_type == "GracefulShutdown":

        event_log.add("GracefulShutdown requested", "OK")
        system.power_state = "Off"

    elif reset_type == "GracefulRestart":

        event_log.add("GracefulRestart requested", "OK")
        system.power_state = "Off"
        time.sleep(1)
        system.power_state = "On"

    elif reset_type == "ForceRestart":

        event_log.add("ForceRestart", "Warning")
        system.power_state = "Off"
        time.sleep(1)
        system.power_state = "On"

    elif reset_type == "ForceOn":

        system.power_state = "On"
        event_log.add("ForceOn", "Warning")

    elif reset_type == "Nmi":

        event_log.add("NMI triggered", "Critical")

    elif reset_type == "PushPowerButton":

        event_log.add("Power Button pressed", "OK")

        system.power_state = (
            "Off" if system.power_state == "On" else "On"
        )

    return jsonify({
        "ResetType": reset_type,
        "result": "ok"
    })











@bp.route(
    "/redfish/v1/Systems/System1/Processors",
    methods=["GET"]
)
def processors_collection():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Systems/System1/Processors",

        "@odata.type":
        "#ProcessorCollection.ProcessorCollection",

        "Name":
        "Processors Collection",

        "Members": [

            {
                "@odata.id":
                "/redfish/v1/Systems/System1/Processors/CPU1"
            }

        ],

        "Members@odata.count": 1
    })


@bp.route(
    "/redfish/v1/Systems/System1/Processors/CPU1",
    methods=["GET"]
)
def processor_cpu1():

    return jsonify(
        cpu1.to_redfish()
    )





@bp.route("/redfish/v1/Systems/System1/LogServices", methods=["GET"])
def logservices():

    return jsonify(log_service.to_redfish())


@bp.route("/redfish/v1/Systems/System1/LogServices/EventLog", methods=["GET"])
def eventlog():

    return jsonify(event_log_resource.to_redfish())


@bp.route("/redfish/v1/Systems/System1/LogServices/EventLog/Entries", methods=["GET"])
def eventlog_entries():

    return jsonify(event_log_entries.to_redfish())

    









@bp.route("/redfish/v1/Systems/System1/Memory", methods=["GET"])
def memory_collection():

    return jsonify(memory.to_collection())


@bp.route("/redfish/v1/Systems/System1/Memory/<mem_id>", methods=["GET"])
def memory_detail(mem_id):

    m = memory.get(mem_id)

    if m is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(m.to_redfish())



@bp.route(
    "/redfish/v1/Systems/System1/Bios",
    methods=["GET"]
)
def bios_resource():

    return jsonify(
        bios.to_redfish()
    )    

@bp.route(
    "/redfish/v1/Systems/System1/Bios/Settings",
    methods=["GET"]
)
def bios_settings_resource():

    return jsonify(
        bios_settings.to_redfish()
    )
    