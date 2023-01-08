user_input = 'random'
data = list()

def showMenue(): #function defination
    print("Menu:")
    print("1. Add an item: ")
    print("2. Mark as done: ")
    print("3. View items: ")
    print("4. Exit: ")

while user_input != '4':
    showMenue() #functiion call
    user_input = input("Enter your choice: ")
    
    if user_input == '1':
        item = input("What is to be done? ")
        data.append(item)
        print("Added item: ",item)
    elif user_input == '2':
        item = input("What is to be marked as done ")
        # checkin that, If item is present in list then remove that item 
        if item in data:
            data.remove(item)
            print("Removed item: ",item)
        else:
            print("Item does not exist in the to-do list ")
    elif user_input == '3':
        print("List of to-do items: ")
        for items in data:
            print(items)
    elif user_input == '4':
        print("Good Bay")