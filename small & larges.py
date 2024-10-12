# mylist=[8,4,5,74,56,25]
# mylist.sort()
# print(mylist)
# print("smallest elements is:", mylist[0])
# print("gretset elements is:", mylist[-1])

# prectice
# mylist=[8,4,5,74,56,25]
# new_list=set(mylist)
# new_list.remove(max(new_list))
# print("after remove max list:", new_list)
# new_list.remove(min(new_list))
# print("after remove min list:", new_list)

# palandrome program
# s=input("enter a string:")
# rverst=(s[::-1])
# if rverst==s:
#     print("palandrom")
# else:
#     print("not palidrom")


# reverse word in a string
str="welcome to vgi"
word=str.split(" ")
word=word[-1::-1]
print(word)

# substring in python programing
str="welcome to vgi"
sub_str="to"
print(str.find(sub_str))

if (str.find(sub_str)== -1):
    print("not found")
else:
    print("found")


