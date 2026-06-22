class ChassisModel:

    def __init__(self):

        self.id = "Chassis1"

        self.name = "Mock Chassis"

        self.manufacturer = "Mockup Inc."

        self.model = "Virtual Chassis"

        self.chassis_type = "RackMount"

    def to_redfish(self):

        return {

            "@odata.id":
            "/redfish/v1/Chassis/Chassis1",

            "@odata.type":
            "#Chassis.v1_20_0.Chassis",

            "Id":
            self.id,

            "Name":
            self.name,

            "Manufacturer":
            self.manufacturer,

            "Model":
            self.model,

            "ChassisType":
            self.chassis_type,

            "Thermal": {

                "@odata.id":
                "/redfish/v1/Chassis/Chassis1/Thermal"
            },

            "Power": {

                "@odata.id":
                "/redfish/v1/Chassis/Chassis1/Power"
            },

            "Sensors": {

                "@odata.id":
                "/redfish/v1/Chassis/Chassis1/Sensors"
            }
        }


chassis = ChassisModel()