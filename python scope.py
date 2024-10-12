# def myfunc():
#     x = 300
#     print(x)
# myfunc()

# GLOBAL FUNCTION
x = 500
def myfunc():
    print(x)
myfunc()
print(x)

myfunc()
print()

#USE GLOBAL KEYWORD

def myfunc():
    global x 
    x = 500
myfunc()
print(x)

