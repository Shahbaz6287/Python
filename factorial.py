# factorial = 1
# num = 5
# if num<0:
#     print("factorial does not exist for negative numbers")
# elif num==0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         factorial=factorial * i
#     print("the factorial of", num, "is", factorial)

# 2nd method
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# num=10
# print("factorial of", num,"is",factorial(num))

# febonacci series
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)

# for i in range (2,10):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum

# maximum and minimum value
# arr = [12,15,45,56,25]
# max=arr[0]
# n=len(arr)

# for i in range(1,n):
#     if arr[i]>max:
#         max=arr[i]

# print(max)

# finding the min elemnet
# arr=[45,86,2,15,78]
# min=arr[0]
# n=len(arr)

# for i in range(1,n):
#     if arr[i]<min:
#         min=arr[i]
# print("Minimum element is: ", min)

# count in list
mylist=[10,15,14,12,18,56]
print(mylist)
count=0
for i in mylist:
    count=count+1
print("Length of list is:", count)

# 
mylist=[10,15,14,12,18,56]
print(mylist)
print("length of list is:", len(mylist))

