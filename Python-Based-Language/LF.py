from Errors import *
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
def show(data_to_show):
    if data_to_show in data:
        print(data[data_to_show])
    else:
        print(data_to_show)   
def setvar(varname: str, varvalue, vartype: str):
    if vartype == "str":
        data[varname] = str(varvalue)
    elif vartype == "int":
        data[varname] = int(varvalue)
    elif vartype == "float":
        data[varname] = float(varvalue)
    elif vartype == "bool":
        data[varname] = bool(varvalue)
    else:
        raise TypeNotFoundError(vartype)
def store(Element):
    if Element in data:
        file_writer.write(str(data[Element]))
    else:
        raise DeclarationError(Element)
def is_it_var(Element):
    if Element in data:
        print(True)
    else:
        print(False)
