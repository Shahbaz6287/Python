# mylist=[5,98,5,6,7,6,90]
# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print("list after sawpping:", mylist)

# approch2: using tuple
# get = (mylist[-1],mylist[0]) 
# mylist[0],mylist[-1]=get
# print("list after swapping:", mylist)

# approch3: *oprend
# 


# simpal swap
# mylist=[58,56,74,14,15,16]
# print(mylist)
# pos1,pos2=1,3
# mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
# print(mylist)

# Approch 2: using inbuilt list.pop() function
# mylist=[58,56,74,14,15,16]
# pos1,pos2 = 1,3
# first_ele=mylist.pop(pos1)
# sec_ele=mylist.pop(pos2-1)
# mylist.insert(pos1,sec_ele)
# mylist.insert(pos2,first_ele)
# print(mylist)

# remove word:
# mylist=["shahbaz", "in", "vgi"]
# word = "shahbaz"
# n=2
# count=0
# for i in range(0,len(mylist)):
#     if (mylist[i]==word):
#         count=count+1
#         if(count==n):
#             del mylist[i]
# print("updated list:",mylist)

# using loop
# mylist=[4,5,6,2,1,4,9]
# ele=4
# if(ele in mylist):
#     print("element found")
# else:
#     print("element is not found")

# approch:1
# using clear()methode
mylist=[4,5,6,9,8,7,2]
print("mylist before clear: ",mylist)
mylist.clear()
print("mylist after clear: ",mylist)

# Approch :2
mylist=[4,5,6,9,8,7,2]
print("mylist before clear:",mylist)
mylist*=0
print("mylist after clear:",mylist)
# approch :3
mylist=[4,5,6,9,8,7,2]
print("mylist before clear:",mylist)
del mylist[1:5]
print(mylist)

# reverse a list
mylist=[4,5,6,9,8,7,2]
print("mylist befor reverse:", mylist)
mylist.reverse()
print("mylist befor reverse:", mylist)
# slicing in reverse
mylist=[4,5,6,9,8,7,2]
print("mylist before reverse:",mylist)
mylist2=mylist[::-1]
print("mylist after reverse:",mylist2)

