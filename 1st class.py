
#----------------DAY - 1------------------

#dynamical type language
name = "R"
age = 20
print(name)
print(age)

print("type of the variable",type(name))


for i in range(1, 6):
    print(i)
    i = i+1

elements = []
for i in range(10):
    elements.append(i)
    print(elements)
    


"""
This is multiline comment
"""
# firstName = input("Enter your name: ")
# lastName = input("Enter your lastname")
# print("your name is ",firstName+ " " +lastName)

#string
val = "HUNTER"
print(type(val))

for i in range(len(val)):
    print(val[i], type(val[i]))

#list
ele = [1, 2, 3, "ram"]
print(ele)
print(ele[-1])

superHero = ["a", "y", "x", "z"]
ratingList = [10, 8, 9, 5]

ratedList = []

for i in range(len(superHero)):
    ratedList.append(superHero[i])
    ratedList.append(ratingList[i])
print(ratedList)
print(type(ratedList))

#Tuple
print("Tuple is inmutable. You can not change the elements of tuple like delete")
marks = (90, 100, 50, 89, 100)
print(marks)
print(type(marks))
tup = 90, "Ravi", 89, 90

s1 = set(tup)
print(s1)
print(type(s1))    
print(marks.count(100))
print(marks.index(100))
#Dictionary
avengerDict = {"Ironman":10,
               "Cap America":9,
               "Thor":8
               
               }
print(avengerDict)
print(type(avengerDict))
print(avengerDict.keys())
print(list(avengerDict.keys()))

avengerDict = {
    "ironman":[
        {"spiderman":8},
        {"balck panther":7}
    ],
    "thor":[
        {"hulk":6},
        {"groot":4}
    ]
}
print("spiderman scoop",avengerDict["ironman"])
print(avengerDict["ironman"][0])
print(avengerDict["thor"][1])

