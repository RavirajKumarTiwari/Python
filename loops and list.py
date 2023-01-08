i = 1
#while loop
while i <= 5:
    print(i * " *")
    i = i+1

#for loop 
for item in range(6):
    print(item)

#list
marks = [90, 89, 78, 80, "Ravi", "Raju", "Vivek", "Saurabh" ]
print(marks)
print(marks[5])
print(marks[-1])
print(marks[-4])
print(marks[0:4])

marks.append(100)
marks.insert(0, 500)

#print this list using for loop
print("---Print list using for loop---")
for score in marks:
    print(score)
    
print(95 in marks) #check that 93 is present in list "marks"
print(len(marks)) #legth of the list marks

#print the list uisng while loop
print("---Print the list using while loop---")
n = 0
while n < len(marks):
    print(marks[n])
    n = n+1
    
marks.clear() #clear function clear the given list
print(marks)