from models.psu import psu1


class PowerModel:

    def __init__(self):

        self.power_watts = 120

    def to_redfish(self):

        return {

            "@odata.id":
            "/redfish/v1/Chassis/Chassis1/Power",

            "@odata.type":
            "#Power.v1_7_0.Power",

            "PowerControl": [

                {
                    "MemberId": "0",

                    "Name":
                    "System Power",

                    "PowerConsumedWatts":
                    round(
                        self.power_watts,
                        1
                    )
                }
            ],

            "PowerSupplies": [

                psu1.to_redfish()

            ]
        }


power = PowerModel()