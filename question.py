# Q. How can I make a tuple out of a list?
# month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
# converting_list = tuple(month)  
# print(converting_list)  
# print(type(converting_list)) 

# 
# name = ['arpna', 'sharma', 'radha', 'mohan']
# converting_list = list(name)
# print(converting_list)
# print(type(converting_list))

# Q.In Python, in what ways can you make an empty NumPy array?
# import numpy  
#method 1  
# array_1 = numpy.array([])  
# print(array_1)  
# #method 2  
# array_2 = numpy.empty(shape=(3,3))  
# print(array_2)  

# Q.Is it possible to construct a Python program that calculates the mean of numbers in a list?
# n = int(input("Number of Elements to take average of: "))  
# l=[]  
# for i in range(1,n+1):  
#     element = int(input("Enter the element: "))  
#     l.append(element)  
# average = sum(l)/n  
# print("Average of the elements in list",round(average,2)) 

# # Q.Is it possible to build a Python program that reverses a number?
# n = int(input("Enter number: "))  
# reverse = 0  
# while(n>0):  
#     digit = n%10  
#     reverse = reverse*10+digit  
#     n=n//10  
# print("The reverse of the number:",reverse)  

# Q.
# list_comp = [i for i in range(50)]  
# print(list_comp) 

# Q.How is a local variable different from a global variable?
var = 58
def addition():
    var1 = 50
    d = var + var1
    print("in local scope: ", var1)
    print("Adding a global scope and a local scope varibale: ",d)
addition()
print("in global scope: ", var)

# Q.What exactly is __init__?
class Student:
    def __init__(self,st_name, st_class, st_marks):
        self.st_name = st_name
        self.st_class = st_class
        self.st_marks = 67
s1 = Student("raja", 52, 67)
print(s1.st_name)
print(s1.st_class)
print(s1.st_marks)

# Q.creating a lambda function for addition
Sum = lambda x, y, z : x + y + z
print("Sum using lambda function is: ", Sum(2, 5, 8))

# importing the random module
import random
list = ["python", "java", "django", "html", "css"]
print("Orignal list: ", list)
random.shuffle(list)
print("After randomising the list: ", list)

# Q.Python program to show how to make an empty class  
class my_class:  
    pass  
object_ = my_class()  
object_.name = "Javatpoint"  
print("Name = ", object_.name)  
