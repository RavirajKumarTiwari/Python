# OOPs in python

class SuperHeroes(): 
    def __init__(self, name, superpower):  # __init__ this is a constructor
        self.name = name
        self.seperpower = superpower
        
    def get_superpower(self): #method
        print(f"I am {self.name} and my power is {self.seperpower} ")
        
ironMan = SuperHeroes( #ironMan is Object of Class SuperHeroes
    name="Iron Man",
    superpower ="Suit"
)
ironMan.get_superpower()

print("\n----Sensor Class----\n")

class Sensor():
    def __init__(self, name, location, record_data):
        self.name = name
        self.location = location
        self.record_data = record_data
        self.data = {}
    
    def add_data(self, data, time):
        self.data["data"] = data
        self.data["time"] = time
        print("Data points added successfully")
        
    def clear_data(self):
        self.data = {}
        print("Data removed successfully")

import numpy as np

sensor1 = Sensor(
    name="sensor1",
    location="Haldia",
    record_data="2023-01-09"
)

data = np.random.randint(-10, 10, 10)
time = np.arange(10)

sensor1.add_data(
    data=data,
    time=time
)
print(sensor1.data)

class Accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")
        
import numpy as np

acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

acc = Accelerometer(
    name="Accelerometer",
    location="Haldia",
    record_data="2023-01-09"
)

acc.add_data(
    data=acc_data,
    time= acc_time
)

print("Accelerometer Data:",acc_data)

print("\n-------5th class--------\n") #5th classsssssss...................

class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location} ")
        
gyro_data = np.random.randint(-15, 15, 10)
gyro_time= np.arange(10)

gyro = Gyro(
    name = "Gyroscope",
    location = "Kolkata",
    record_data = "2023-01-10"
)
gyro.add_data(time = gyro_time, data = gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()

# print("Accelerometer Data: "acc.data)
# GPS attributes:
# Name
# location
# recorded_data
# brand



class GPS(Sensor):
    def __init__(self, name, location, record_data, brand):
        super().__init__(name, location, record_data)
        self.brand = brand
        
gps = GPS(
    name="GPS",
    location="Chennai",
    record_data="2023-01-10",
    brand="espressif"
)
print(gps.name)
print(gps.location)
print(gps.record_data)
print(gps.brand)
