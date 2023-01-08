info = {
    "Name": "Raviraj Tiwari",
    "Age": 19,
    "Elegible": True
}
print(info)
print(info["Name"])
print(info.get("Age"))
print(info.keys()) # to get all keys
print(info.values()) # to get all values

for key in info.keys():
    print(f"The corresponding values to the key {key} is {info[key]}")
