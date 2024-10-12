# creat a class named person,with firastname and lasstname and a printname method:
class persion:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname (self):
        print(self.firstname, self.lastname)
x = persion("shahbaz", "anjoom")
x.printname()

# # prectice:
# class method():
#     def ___init___(self, fclass, lclass, mclass,):
#         self.firstclass = fclass
#         self.lastclass = lclass
#         self.mclass = mclass
#     def printname (self):
#         print(self.firstclass, self.lastclass, self.mclass,)
# x = method("10th", "11th", "12th",)
# x.printname()

# prectice



# class student:    
     
#     def __init__(self, name, email):    
#         self.name = name    
#         self.email = email    
         
# # This line will generate an error    
# #st = student("rahul")    
    
# # This line will call the second constructor    
# # st = student("rahul", "rahul@gmail.com")    
# # print("Name: ", st.name)  
# # print("Email id: ", st.email)  


# def creating_gen(index):  
#     months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
#     yield months[index]  
#     yield months[index+2]  
# next_month = creating_gen(3)  
# print(next(next_month), next(next_month))  

month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
converting_list = tuple(month)  
print(converting_list)  
print(type(converting_list))  

