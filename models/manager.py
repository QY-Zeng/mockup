class ManagerModel:

    def __init__(self):

        self.id = "BMC"

        self.name = "Mock BMC"

        self.firmware_version = "1.0.0"

        self.health = "OK"

    def to_redfish(self):

        return {

            "@odata.id":
            "/redfish/v1/Managers/BMC",

            "@odata.type":
            "#Manager.v1_17_0.Manager",

            "Id":
            self.id,

            "Name":
            self.name,

            "FirmwareVersion":
            self.firmware_version,

            "Status": {

                "State":
                "Enabled",

                "Health":
                self.health
            },

            "LogServices": {

                "@odata.id":
                "/redfish/v1/Managers/BMC/LogServices"
            },

            "EthernetInterfaces": {

                "@odata.id":
                "/redfish/v1/Managers/BMC/EthernetInterfaces"
            }
        }


manager = ManagerModel()