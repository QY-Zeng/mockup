class EthernetInterfaceModel:

    def __init__(self):

        self.id = "eth0"

        self.hostname = "mockup-bmc"

        self.mac_address = "00:11:22:33:44:55"

        self.dhcp_enabled = False

        self.ipv4_address = "192.168.1.100"

        self.gateway = "192.168.1.1"

        self.subnet_mask = "255.255.255.0"

    def to_redfish(self):

        return {

            "@odata.id":
            "/redfish/v1/Managers/BMC/EthernetInterfaces/eth0",

            "@odata.type":
            "#EthernetInterface.v1_11_0.EthernetInterface",

            "Id":
            self.id,

            "Name":
            "BMC Ethernet Interface",

            "HostName":
            self.hostname,

            "MACAddress":
            self.mac_address,

            "DHCPv4": {
                "DHCPEnabled":
                self.dhcp_enabled
            },

            "IPv4Addresses": [

                {
                    "Address":
                    self.ipv4_address,

                    "SubnetMask":
                    self.subnet_mask,

                    "Gateway":
                    self.gateway
                }

            ]
        }


eth0 = EthernetInterfaceModel()