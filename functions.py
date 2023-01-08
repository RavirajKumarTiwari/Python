# FUNCTION SINTEX
"""
def functionName(parameter):
    //do something
"""

def printSum(first, second):
    print(first, "+", second, "= ", first + second)
    
printSum(20, 100) #function call

def printSum(first, second = 200): #if you not pass second value then by defult value(200) will be taken as input
    print(first, "+", second, "= ", first + second)
    
printSum(50) #here in function call I pass only one parameter