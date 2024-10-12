# Approch1:using slicing technique
# mylist=[7,8,5,1,4,5,8]
# mylist_copy=mylist[:]
# print(mylist_copy)
# extend() in the slicing
# mylist=[7,8,5,1,4,5,8]
# mylist_copy=[4,8,2,56,15]
# mylist_copy.extend(mylist)
# print(mylist_copy)

# using the list() methode
# mylist=[5,8,6,7,2]
# mylist_copy=list(mylist)
# print(mylist_copy)
# copy()methode
# mylist=[7,8,5,1,4,5,8]
# mylist_copy=mylist.copy()
# print(mylist_copy)
# using list comprehension:
# mylist=[7,8,5,1,4,5,8]
# mylist_copy=[i for i in mylist]
# print(mylist_copy)
# count ocurrence pyhton:
# mylist=[5,8,6,2,4,7,7,5,5]
# x=10
# count=0
# for ele in mylist:
#     if(ele==x):
#         count=count+1
# print

# multiply in list
mylist=[5,6,8,1,7,3]
result=1
for x in mylist:
    result=result * x
print(result)

# use numpay
import numpy
mylist=[5,8,6,8,9]
result=numpy.prod(mylist)
print(numpy)