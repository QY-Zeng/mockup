class ThermalModel:

    def __init__(self):

        self.cpu_temp = 50

        self.inlet_temp = 28

        self.fan1_enabled = True
        self.fan1_pwm = 70
        self.fan1_rpm = 5600

        self.fan2_enabled = True
        self.fan2_pwm = 70
        self.fan2_rpm = 5600
        
        self.fan1_failure_logged = False
        self.fan2_failure_logged = False
        self.shutdown_logged = False

    def to_redfish(self):
    
        #
        # CPU health
        #
        if self.cpu_temp < 70:
    
            cpu_health = "OK"
    
        elif self.cpu_temp < 85:
    
            cpu_health = "Warning"
    
        else:
    
            cpu_health = "Critical"
    
        return {
    
            "@odata.id":
            "/redfish/v1/Chassis/Chassis1/Thermal",
    
            "@odata.type":
            "#Thermal.v1_7_0.Thermal",
    
            "Id":
            "Thermal",
    
            "Name":
            "Thermal",
    
            "Temperatures": [
    
                {
                    "@odata.id":
                    "/redfish/v1/Chassis/Chassis1/Thermal#/Temperatures/0",
    
                    "MemberId":
                    "0",
    
                    "Name":
                    "CPU Temp",
    
                    "PhysicalContext":
                    "CPU",
    
                    "ReadingCelsius":
                    round(
                        self.cpu_temp,
                        1
                    ),
    
                    "UpperThresholdNonCritical":
                    70,
    
                    "UpperThresholdCritical":
                    85,
    
                    "UpperThresholdFatal":
                    100,
    
                    "Status": {
    
                        "Health":
                        cpu_health,
    
                        "State":
                        "Enabled"
                    },
    
                    "RelatedItem": [
    
                        {
                            "@odata.id":
                            "/redfish/v1/Systems/System1/Processors/CPU1"
                        }
                    ]
                },
    
                {
                    "@odata.id":
                    "/redfish/v1/Chassis/Chassis1/Thermal#/Temperatures/1",
    
                    "MemberId":
                    "1",
    
                    "Name":
                    "Inlet Temp",
    
                    "PhysicalContext":
                    "Intake",
    
                    "ReadingCelsius":
                    self.inlet_temp,
    
                    "UpperThresholdNonCritical":
                    35,
    
                    "UpperThresholdCritical":
                    40,
    
                    "UpperThresholdFatal":
                    50,
    
                    "Status": {
    
                        "Health":
                        "OK",
    
                        "State":
                        "Enabled"
                    }
                }
            ],
    
            "Fans": [
    
                {
                    "@odata.id":
                    "/redfish/v1/Chassis/Chassis1/Thermal#/Fans/0",
    
                    "MemberId":
                    "0",
    
                    "Name":
                    "Fan1",
    
                    "PhysicalContext":
                    "Backplane",
    
                    "Reading":
                    self.fan1_rpm,
    
                    "ReadingUnits":
                    "RPM",
    
                    "Status": {
    
                        "Health":
                        "OK"
                        if self.fan1_enabled
                        else "Critical",
    
                        "State":
                        "Enabled"
                        if self.fan1_enabled
                        else "Disabled"
                    }
                },
    
                {
                    "@odata.id":
                    "/redfish/v1/Chassis/Chassis1/Thermal#/Fans/1",
    
                    "MemberId":
                    "1",
    
                    "Name":
                    "Fan2",
    
                    "PhysicalContext":
                    "Backplane",
    
                    "Reading":
                    self.fan2_rpm,
    
                    "ReadingUnits":
                    "RPM",
    
                    "Status": {
    
                        "Health":
                        "OK"
                        if self.fan2_enabled
                        else "Critical",
    
                        "State":
                        "Enabled"
                        if self.fan2_enabled
                        else "Disabled"
                    }
                }
            ]
        }        
 


thermal = ThermalModel()