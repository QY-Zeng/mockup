from models.workload import workload
from models.system import system


class ProcessorModel:

    def __init__(self):

        self.id = "CPU1"

        self.socket = "CPU Socket 1"

        self.model = "Mock CPU"

        self.manufacturer = "Mockup Inc."

        self.total_cores = 8

        self.total_threads = 16

    def to_redfish(self):

        return {

            "@odata.id":
            "/redfish/v1/Systems/System1/Processors/CPU1",

            "@odata.type":
            "#Processor.v1_18_0.Processor",

            "Id":
            self.id,

            "Name":
            self.socket,

            "Manufacturer":
            self.manufacturer,

            "Model":
            self.model,

            "ProcessorType":
            "CPU",

            "TotalCores":
            self.total_cores,

            "TotalThreads":
            self.total_threads,

            "Status": {

                "State":
                "Enabled",

                "Health":
                system.health
            },

            "Oem": {

                "Mockup": {

                    "UtilizationPercent":
                    workload.cpu_util
                }
            }
        }


cpu1 = ProcessorModel()