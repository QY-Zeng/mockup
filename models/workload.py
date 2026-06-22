class WorkloadModel:

    def __init__(self):
        self.cpu_util = 20

    def get_heat(self):

        return self.cpu_util / 10
        
workload = WorkloadModel()