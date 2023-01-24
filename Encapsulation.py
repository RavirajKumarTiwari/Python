
"""
Encapsulation and Abstraction
"""

class Sensor():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__record_date = "2023-01-10"
        self.__version = "0.0112"
    
    #getter
    def get_record_data(self):
        print(f"The record date is {self.__record_date}")
    def get_version(self):
        print(f"The version is {self.__version}")
        
    #setter
    def set_version(self, version):
        self.__version = version
        print(f"The version is {self.__version}")
    def set_record_date(self, record_date):
        self.__record_date = record_date
        print(f"The record date is {self.__record_date}")


sensor1 = Sensor(
    name="Sensor 1", location="Haldia"
)

print(sensor1.name)
print(sensor1.location)
# print(sensor1.version)
# print(sensor1.record_date)

sensor1.get_record_data()
sensor1.get_version()

sensor1.set_record_date(record_date="2024-01-10")
sensor1.set_version(version="0.212")
