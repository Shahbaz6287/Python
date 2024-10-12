# def my_function(*kids):
#   print("the youngest child is " + kids[2])
# my_function("emil", "tobias", "linus")

#default parameter value
# def my_function(country = "Norway"):
#     print("i am from " + country)
# my_function("sweden")
# my_function("india")
# my_function()
# my_function("brazil")

#return value:
# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(6))
# print(my_function(7))
# print(my_function(8))

#recursion ex:
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Result")
tri_recursion(8)