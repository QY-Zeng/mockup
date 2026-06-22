from flask import Blueprint
from flask import request
from flask import jsonify

from models.thermal import thermal
from models.workload import workload

bp = Blueprint(
    "control",
    __name__
)


@bp.route(
    "/control/fan1",
    methods=["POST"]
)
def set_fan1():

    data = request.get_json()

    if "enabled" in data:

        thermal.fan1_enabled = \
            data["enabled"]

    if "pwm" in data:

        thermal.fan1_pwm = \
            data["pwm"]

    return jsonify({
        "result": "ok"
    })


@bp.route(
    "/control/fan2",
    methods=["POST"]
)
def set_fan2():

    data = request.get_json()

    if "enabled" in data:

        thermal.fan2_enabled = \
            data["enabled"]

    if "pwm" in data:

        thermal.fan2_pwm = \
            data["pwm"]

    return jsonify({
        "result": "ok"
    })


@bp.route(
    "/control/workload",
    methods=["POST"]
)
def set_workload():

    data = request.get_json()

    if "cpu" in data:

        workload.cpu_util = \
            int(data["cpu"])

    return jsonify({
        "result": "ok"
    })


