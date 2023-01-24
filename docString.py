'''docString is always right below the function name and write before the function body and always in triple quotes symbol'''

def docString(n):
    '''This is a example of docString.'''
    print(n**2)

docString(5)
print(docString.__doc__)

def doc():
    print("This is not a docString")
    '''This is not docString'''
doc()
print(doc.__doc__)