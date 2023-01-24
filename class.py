
# Revision of Opps till now 10.01.2023

class Revision():
    def __init__(self):
        self.__name = "Ravi Tiwari" #Encapsulation
        self.__roll_no = "123"
        self.marks = {}
    
    def get_name(self): #getter function
        print("Name",self.__name)
        print("Roll No.",self.__roll_no)
        
    def add_marks(self, maths, physics, chemistry):
        self.marks["maths"] = maths
        self.marks["physics"] = physics
        self.marks["chemistry"] = chemistry

revision = Revision()
revision.add_marks(
    maths=90,
    physics=78,
    chemistry=88
)
revision.get_name()
print(f"Your marks are :\n {revision.marks} ")

#
class NewRevison(Revision):
    def show_type(self):
        print("\nExample of Inheritance")

new = NewRevison()
new.add_marks(
    maths=99,
    physics=89,
    chemistry=90
)
new.show_type()
print(f"\nFinal marks :\n {new.marks} ")