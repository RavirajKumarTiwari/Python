students = ["ravi", "raj", "ram", "radha", "vivek", "saurabh"]

for student in students:
    if student == "radha":
        break;
    print(student)

print("# Working of continue keyword")
for student in students:
    if student == "radha":
        continue;
    print(student)
