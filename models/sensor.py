from models.thermal import thermal
from models.power import power


class SensorItem:

    def __init__(self, sensor_id, name, value_func, units):

        self.id = sensor_id
        self.name = name

        # function (dynamic value)
        self.value_func = value_func

        self.units = units

    def get_reading(self):

        return self.value_func()

    def to_ref(self):

        return {
            "@odata.id": f"/redfish/v1/Chassis/Chassis1/Sensors/{self.id}"
        }

    def to_redfish(self):

        return {
            "@odata.id": f"/redfish/v1/Chassis/Chassis1/Sensors/{self.id}",
            "@odata.type": "#Sensor.v1_6_0.Sensor",
            "Id": self.id,
            "Name": self.name,
            "Reading": self.get_reading(),
            "ReadingUnits": self.units,
            "Status": {
                "State": "Enabled"
            }
        }


class SensorCollection:

    def __init__(self):

        self.sensors = {

            "CPUTemp": SensorItem(
                "CPUTemp",
                "CPU Temperature",
                lambda: round(thermal.cpu_temp, 1),
                "Cel"
            ),

            "Fan1": SensorItem(
                "Fan1",
                "Fan 1 RPM",
                lambda: thermal.fan1_rpm,
                "RPM"
            ),

            "Fan2": SensorItem(
                "Fan2",
                "Fan 2 RPM",
                lambda: thermal.fan2_rpm,
                "RPM"
            ),

            "Power": SensorItem(
                "Power",
                "System Power",
                lambda: round(power.power_watts, 1),
                "W"
            )
        }

    def to_collection(self):

        return {
            "@odata.id": "/redfish/v1/Chassis/Chassis1/Sensors",
            "@odata.type": "#SensorCollection.SensorCollection",
            "Name": "Chassis Sensors",
            "Members": [
                s.to_ref() for s in self.sensors.values()
            ],
            "Members@odata.count": len(self.sensors)
        }

    def get(self, sensor_id):

        sensor = self.sensors.get(sensor_id)

        if sensor is None:
            return None

        return sensor


sensor = SensorCollection()