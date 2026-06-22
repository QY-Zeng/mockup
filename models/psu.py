class PowerSupplyModel:

    def __init__(self):

        self.id = "PSU1"
        self.name = "Power Supply 1"

        self.enabled = True
        self.health = "OK"

        self.efficiency = 0.92

        self.input_watts = 230
        self.output_watts = 120

    def update(self, system_power):

        if not self.enabled:
            self.output_watts = 0
            self.input_watts = 0
            self.health = "Critical"
            return

        self.output_watts = system_power
        self.input_watts = system_power / self.efficiency

        self.health = "OK"

    def to_redfish(self):

        return {

            "MemberId": self.id,
            "Name": self.name,

            "PowerInputWatts": round(self.input_watts, 1),
            "PowerOutputWatts": round(self.output_watts, 1),

            "Status": {
                "State": "Enabled" if self.enabled else "Disabled",
                "Health": self.health
            }
        }


psu1 = PowerSupplyModel()