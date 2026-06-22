from flask import Blueprint
from flask import jsonify

from models.chassis import chassis
from models.thermal import thermal
from models.power import power
from models.sensor import sensor


bp = Blueprint(
    "chassis",
    __name__
)


@bp.route(
    "/redfish/v1/Chassis",
    methods=["GET"]
)
def chassis_collection():

    return jsonify({

        "@odata.id":
        "/redfish/v1/Chassis",

        "@odata.type":
        "#ChassisCollection.ChassisCollection",

        "Name":
        "Chassis Collection",

        "Members": [

            {
                "@odata.id":
                "/redfish/v1/Chassis/Chassis1"
            }

        ],

        "Members@odata.count": 1
    })


@bp.route(
    "/redfish/v1/Chassis/Chassis1",
    methods=["GET"]
)
def chassis_resource():

    return jsonify(
        chassis.to_redfish()
    )


@bp.route(
    "/redfish/v1/Chassis/Chassis1/Thermal",
    methods=["GET"]
)
def thermal_resource():

    return jsonify(
        thermal.to_redfish()
    )



@bp.route(
    "/redfish/v1/Chassis/Chassis1/Power",
    methods=["GET"]
)
def power_resource():

    return jsonify(
        power.to_redfish()
    )


@bp.route("/redfish/v1/Chassis/Chassis1/Sensors")
def sensors():

    return jsonify(sensor.to_collection())



@bp.route(
    "/redfish/v1/Chassis/Chassis1/Sensors/<sensor_id>",
    methods=["GET"]
)
def sensor_detail(sensor_id):

    from models.sensor import sensor

    s = sensor.get(sensor_id)

    if s is None:

        return jsonify({
            "error": "Sensor not found"
        }), 404

    return jsonify(
        s.to_redfish()
    )

    

