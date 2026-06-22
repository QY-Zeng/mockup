from flask import Blueprint
from flask import jsonify

from models.manager import manager
from models.network import eth0

bp = Blueprint(
    "managers",
    __name__
)


@bp.route(
    "/redfish/v1/Managers",
    methods=["GET"]
)
def managers_collection():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Managers",

        "@odata.type":
        "#ManagerCollection.ManagerCollection",

        "Name":
        "Manager Collection",

        "Members": [

            {
                "@odata.id":
                "/redfish/v1/Managers/BMC"
            }

        ],

        "Members@odata.count": 1
    })


@bp.route(
    "/redfish/v1/Managers/BMC",
    methods=["GET"]
)
def manager_resource():

    return jsonify(
        manager.to_redfish()
    )



@bp.route(
    "/redfish/v1/Managers/BMC/EthernetInterfaces",
    methods=["GET"]
)
def ethernet_collection():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Managers/BMC/EthernetInterfaces",

        "Members": [

            {
                "@odata.id":
                "/redfish/v1/Managers/BMC/EthernetInterfaces/eth0"
            }

        ],

        "Members@odata.count": 1
    })



@bp.route(
    "/redfish/v1/Managers/BMC/EthernetInterfaces/eth0",
    methods=["GET"]
)
def ethernet_eth0():

    return jsonify(
        eth0.to_redfish()
    )