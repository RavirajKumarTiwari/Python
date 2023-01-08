# Function

def multiplier(param1, param2):  # function declaration
    # body of function
    return param1*param2


print(multiplier(12, 2))  # calling the function


employeeList = [
    {
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
]

print(type(employeeList))

def get_employee_pin_list(employee_list, addressKey):
    emp_pin_list = []
    for emp in employee_list:
        emp_pin_list.append({"name": emp["name"]})
        emp_pin_list[employee_list.index(emp)][addressKey] = []

        for address in emp["address"]:
            emp_pin_list[employee_list.index(emp)][addressKey].append(
                address[addressKey])
    return emp_pin_list


func_list = get_employee_pin_list(employeeList, addressKey="state")
print(func_list)


#for more todo folder 