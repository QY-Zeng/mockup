class BiosSettingsModel:

    def __init__(self):

        self.attributes = {

            "AdminPhone": "(404) 555-1212",

            "BootMode": "Uefi",

            "EmbeddedSata": "Ahci",

            "NicBoot1": "NetworkBoot",

            "NicBoot2": "NetworkBoot",

            "PowerProfile": "MaxPerf",

            "ProcCoreDisable": 0,

            "ProcHyperthreading": "Enabled",

            "ProcTurboMode": "Disabled",

            "UsbControl": "UsbEnabled"
        }

    def to_redfish(self):

        return {

            "@odata.type":
            "#Bios.v1_2_3.Bios",

            "Id":
            "Settings",

            "Name":
            "BIOS Configuration Pending Settings",

            "AttributeRegistry":
            "BiosAttributeRegistryP89.v1_0_0",

            "Attributes":
            self.attributes,

            "@odata.id":
            "/redfish/v1/Systems/System1/Bios/Settings"
        }


bios_settings = BiosSettingsModel()