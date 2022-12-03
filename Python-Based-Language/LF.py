from DeclarationError import *
# Useful Vars
data = {}
# Mathimatical Functions
def add(a, b):
    list = [a, b]
    for i in list:
        if i in data:
            pass
        else:
            print(a + b)
    print(data[a] + data[b])
def minus(a, b):
    print(a - b)
def multiplicate(a, b):
    print(a * b)
def divise(a, b):
    print(a / b)
# Regulare Function
def show(data):
    print(data)
def setvar(varname, varvalue):
    data[varname] = varvalue
    global varindex
    varindex = list(data).index(varname)
def showvar(varname):
    print(data[varname])
