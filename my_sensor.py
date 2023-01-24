import numpy as np
from sensorModule import *


class Accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")


acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

acc = Accelerometer(
    name="Accelerometer",
    location="Haldia",
    record_date="2023-01-09"
)

acc.add_data(
    data=acc_data,
    time=acc_time
)

print("Accelerometer Data:", acc_data)

print("\n-------5th class--------\n")  # 5th classsssssss...................


class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location} ")


gyro_data = np.random.randint(-15, 15, 10)
gyro_time = np.arange(10)

gyro = Gyro(
    name="Gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)
gyro.add_data(time=gyro_time, data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()

# print("Accelerometer Data: "acc.data)
# GPS attributes:
# Name
# location
# recorded_data
# brand


class GPS(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand


gps = GPS(
    name="GPS",
    location="Chennai",
    record_date="2023-01-10",
    brand="espressif"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
