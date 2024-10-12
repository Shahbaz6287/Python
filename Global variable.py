x = "fantastics"
def myfunc():
    print("the tajmahal is " + x)
myfunc()

#creat a variable inside a function, with the same name as the global variable

x = "handsome"
def myfunc():
    x = "awesome"
    print("Alok is " + x)
myfunc()
print("Alok is " + x)

# USE THE global KEYWORD, THE VARIABLE BELONGS TO THE GLOBAL SCOPE:
from re import X


def myfunc():
    global X
    X = "beautiful"
myfunc()
print("kajol is " + X)
#prectice
x= "handsome and intelligent"
myfunc()
print("suraj is " + x)
