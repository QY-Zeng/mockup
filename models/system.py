from models.workload import workload


class ComputerSystem:

    def __init__(self):

        self.id = "System1"

        self.name = "WebFrontEnd483"

        self.manufacturer = "Contoso"

        self.model = "3500"

        self.submodel = "RX"

        self.serial_number = "437XR1138R2"

        self.part_number = "224071-J23"

        self.sku = "8675309"

        self.asset_tag = "Chicago-45Z-2381"

        self.description = "Web Front End node"

        self.hostname = "web483"

        self.power_state = "On"

        self.health = "OK"

        self.uuid = "38947555-7742-3448-3784-823347823834"

    def to_redfish(self):

        return {

            

            "@odata.type":
            "#ComputerSystem.v1_27_0.ComputerSystem",

            #
            # Basic Information
            #
            "Id":
            self.id,

            "Name":
            self.name,

            "SystemType":
            "Physical",

            "AssetTag":
            self.asset_tag,

            "Manufacturer":
            self.manufacturer,

            "Model":
            self.model,

            "SubModel":
            self.submodel,

            "SKU":
            self.sku,

            "SerialNumber":
            self.serial_number,

            "PartNumber":
            self.part_number,

            "Description":
            self.description,

            "UUID":
            self.uuid,

            "HostName":
            self.hostname,

            #
            # Status
            #
            "Status": {

                "State":
                "Enabled",

                "Health":
                self.health,

                "HealthRollup":
                self.health
            },

            #
            # Roles
            #
            "HostingRoles": [
                "ApplicationServer"
            ],

            #
            # LED
            #
            "IndicatorLED":
            "Off",

            #
            # Power
            #
            "PowerState":
            self.power_state,

            #
            # Boot
            #
            "Boot": {

                "BootSourceOverrideEnabled":
                "Once",

                "BootSourceOverrideTarget":
                "Pxe",

                "BootSourceOverrideTarget@Redfish.AllowableValues": [

                    "None",
                    "Pxe",
                    "Cd",
                    "Usb",
                    "Hdd",
                    "BiosSetup",
                    "Utilities",
                    "Diags",
                    "SDCard",
                    "UefiTarget"
                ],

                "BootSourceOverrideMode":
                "UEFI",

                "UefiTargetBootSourceOverride":
                "/0x31/0x33/0x01/0x01"
            },

            #
            # Boot Progress
            #
            "BootProgress": {

                "LastState":
                "OSRunning",

                "LastStateTime":
                "2021-03-13T04:14:13+06:00",

                "LastBootTimeSeconds":
                676
            },

            #
            # BIOS
            #
            "BiosVersion":
            "P79 v1.45 (12/06/2017)",

            #
            # TPM
            #
            "TrustedModules": [

                {

                    "FirmwareVersion":
                    "1.13b",

                    "InterfaceType":
                    "TPM1_2",

                    "Status": {

                        "State":
                        "Enabled",

                        "Health":
                        "OK"
                    }
                }
            ],

            #
            # Processor Summary
            #
            "ProcessorSummary": {

                "Count":
                2,

                "CoreCount":
                8,

                "LogicalProcessorCount":
                16,

                "Model":
                "Multi-Core Intel(R) Xeon(R) processor 7xxx Series",

                "Status": {

                    "State":
                    "Enabled",

                    "Health":
                    "OK",

                    "HealthRollup":
                    "OK"
                }
            },

            #
            # Memory Summary
            #
            "MemorySummary": {

                "TotalSystemMemoryGiB":
                96,

                "TotalSystemPersistentMemoryGiB":
                0,

                "MemoryMirroring":
                "None",

                "Status": {

                    "State":
                    "Enabled",

                    "Health":
                    "OK",

                    "HealthRollup":
                    "OK"
                }
            },

            #
            # OEM
            #
            "Oem": {

                "Contoso": {

                    "@odata.type":
                    "#Contoso.ComputerSystem",

                    "ProductionLocation": {

                        "FacilityName":
                        "PacWest Production Facility",

                        "Country":
                        "USA"
                    }
                },

                "Chipwise": {

                    "@odata.type":
                    "#Chipwise.ComputerSystem",

                    "Style":
                    "Executive"
                },

                "Mockup": {

                    "CpuUtilizationPercent":
                    workload.cpu_util
                }
            },

            #
            # Resources
            #
            "Bios": {
                "@odata.id":
                "/redfish/v1/Systems/System1/Bios"
            },

            "SecureBoot": {
                "@odata.id":
                "/redfish/v1/Systems/System1/SecureBoot"
            },

            "Processors": {
                "@odata.id":
                "/redfish/v1/Systems/System1/Processors"
            },

            "Memory": {
                "@odata.id":
                "/redfish/v1/Systems/System1/Memory"
            },

            "EthernetInterfaces": {
                "@odata.id":
                "/redfish/v1/Systems/System1/EthernetInterfaces"
            },

            "SimpleStorage": {
                "@odata.id":
                "/redfish/v1/Systems/System1/SimpleStorage"
            },

            "GraphicsControllers": {
                "@odata.id":
                "/redfish/v1/Systems/System1/GraphicsControllers"
            },

            "USBControllers": {
                "@odata.id":
                "/redfish/v1/Systems/System1/USBControllers"
            },

            "Certificates": {
                "@odata.id":
                "/redfish/v1/Systems/System1/Certificates"
            },

            "VirtualMedia": {
                "@odata.id":
                "/redfish/v1/Systems/System1/VirtualMedia"
            },

            "LogServices": {
                "@odata.id":
                "/redfish/v1/Systems/System1/LogServices"
            },

            #
            # Links
            #
            "Links": {

                "Chassis": [

                    {
                        "@odata.id":
                        "/redfish/v1/Chassis/Chassis1"
                    }
                ],

                "ManagedBy": [

                    {
                        "@odata.id":
                        "/redfish/v1/Managers/BMC"
                    }
                ]
            },

            #
            # Actions
            #
            "Actions": {

                "#ComputerSystem.Reset": {

                    "target":
                    "/redfish/v1/Systems/System1/Actions/ComputerSystem.Reset",

                    "ResetType@Redfish.AllowableValues": [

                        "On",
                        "ForceOff",
                        "GracefulShutdown",
                        "GracefulRestart",
                        "ForceRestart",
                        "Nmi",
                        "ForceOn",
                        "PushPowerButton"
                    ]
                },

                "Oem": {

                    "#Contoso.Reset": {

                        "target":
                        "/redfish/v1/Systems/System1/Oem/Contoso/Actions/Contoso.Reset"
                    }
                }
            },
            "@odata.id":
            "/redfish/v1/Systems/System1"
        }


system = ComputerSystem()