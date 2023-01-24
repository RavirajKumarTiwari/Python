class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, data, time):
        self.data["data"] = data
        self.data["time"] = time
        print("Data points added successfully")

    def clear_data(self):
        self.data = {}
        print("Data removed successfully")
