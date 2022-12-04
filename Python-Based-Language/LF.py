from DeclarationError import *
# Useful Vars
data = {}
file_writer = open("db.txt", "a")
file_reader = open("db.txt", "r")
# Mathimatical Functions
def add(a, b):
    if a in data:
        print(data[a] + b)
    elif b in data:
        print(a + data[b])
    elif a in data and b in data:
        print(data[a] + data[b])
    elif a not in data and b not in data:
        print(a + b)
def minus(a, b):
    if a in data:
        print(data[a] - b)
    elif b in data:
        print(a - data[b])
    elif a in data and b in data:
        print(data[a] - data[b])
    elif a not in data and b not in data:
        print(a - b)
def multiplicate(a, b):
    if a in data:
        print(data[a] * b)
    elif b in data:
        print(a * data[b])
    elif a in data and b in data:
        print(data[a] * data[b])
    elif a not in data and b not in data:
        print(a * b)
def divise(a, b):
    if a in data:
        print(data[a] / b)
    elif b in data:
        print(a / data[b])
    elif a in data and b in data:
        print(data[a] / data[b])
    elif a not in data and b not in data:
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
def store(Element):
    if Element in data:
        file_writer.write(str(data[Element]))
    else:
        file_writer.write(str(Element))
def is_it_var(Element):
    if Element in data:
        print(True)
    else:
        print(False)
