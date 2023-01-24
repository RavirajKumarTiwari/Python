# lambda function
# global and local variable

def multiply(var1, var2):
    result = var1*var2
    return result
res = multiply(5, 6)
print(res)

# lambda function
print("---Lambda function---")
multiplyX = lambda var1, var2: var1*var2
print(multiplyX(5, 6))

# global and local variable

print("\n---global and local variable---\n")

temp = 56
print("Value of temp before the function: ",temp)

def test():
    global temp #making the 'test' variable local to golbal using golobal keyward 
    temp = 9
    print("Value of temp before the function: ",temp)
test()

print("Value of temp after the function: ",temp)