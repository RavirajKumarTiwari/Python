ratedAvengerList2D=[
    ["Spiderman",8],
    ["Groot",7],
    ["Black Widow",8]
]
for i in range(0, len(ratedAvengerList2D)):
    for j in range(0, len(ratedAvengerList2D[i])):
        print(ratedAvengerList2D[i][j])

print("---   ---   ---    ---") 

for ele in ratedAvengerList2D:
    for ele2 in ele:
        print(ele2)
        
print("--------------------")

employee = {
    "name": "Tony Stark",
    "emp_id": 3,
    "address":[
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "7773"
        },
        {
            "line1": "fffgg",
            "lien2": "dskfjh",
            "state": "bihar",
            "pincode": "87998"
        }
    ]
}

print(type(employee))

for i in range(0, len(employee["address"])):
    print(employee["address"][i]["state"])
    print(employee["address"][i]["pincode"])

print("-------------------------")

employeeList = {
    "name": "Tony Stark",
    "emp_id": 3,
    "address": [
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "7773"
        },
        {
            "line1": "fffgg",
            "lien2": "dskfjh",
            "state": "bihar",
            "pincode": "87998"
        }
    ]
},
{
    "name": "xxxxxxx",
    "emp_id": 10,
    "address": [
        {
            "line1": "fffiiii",
            "line2": "hhhiiiii",
            "state": "wbiiiiiiiii",
            "pincode": "7773000000"
        },
        {
            "line1": "fffggiiiiii",
            "lien2": "dskfjhiiiiiiiii",
            "state": "bihariiiiiiiii",
            "pincode": "87998000000"
        }
    ]
}

emp_pin_list = []
for emp in employeeList:
    emp_pin_list.append({"name":emp["name"]})
    # print(emp_pin_list)
    # print(employeeList.index(emp))
    emp_pin_list[employeeList.index(emp)]["pincode"] = []
    
    for address in emp["address"]:
        emp_pin_list[employeeList.index(emp)]["pincode"].append(address["pincode"])
        # print("Pincode: ", address["pincode"])

print(emp_pin_list)

def mul(a,b):
    return a*b


ans=mul(4,5)
print(ans)

list = [54, 78, 898, 100]
list.sort()
print(list)

