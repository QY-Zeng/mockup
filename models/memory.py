class MemoryItem:

    def __init__(self, mem_id, size_gb):

        self.id = mem_id
        self.size_gb = size_gb
        self.health = "OK"

    def to_redfish(self):

        return {
            "@odata.id": f"/redfish/v1/Systems/System1/Memory/{self.id}",
            "@odata.type": "#Memory.v1_7_1.Memory",
            "Id": self.id,
            "Name": f"DIMM {self.id}",
            "CapacityMiB": self.size_gb * 1024,
            "Status": {
                "State": "Enabled",
                "Health": self.health
            }
        }


class MemoryCollection:

    def __init__(self):

        self.memory = {
            "DIMM1": MemoryItem("DIMM1", 16),
            "DIMM2": MemoryItem("DIMM2", 16)
        }

    def to_collection(self):

        return {
            "@odata.id": "/redfish/v1/Systems/System1/Memory",
            "@odata.type": "#MemoryCollection.MemoryCollection",
            "Name": "System Memory",
            "Members": [
                {"@odata.id": f"/redfish/v1/Systems/System1/Memory/{m}"} 
                for m in self.memory
            ],
            "Members@odata.count": len(self.memory)
        }

    def get(self, mem_id):

        return self.memory.get(mem_id)


memory = MemoryCollection()