# natural number >1
# which has only 2 factor 1 and itself
# 19=>1 and 19=>prime number
# 20=> 1,2,4,5,10,20 it is not prime number

num = int(input("enter the numebr: "))
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i) ==0:
            count=count+1
    if count ==2:
        print("number is prime number")

    else:
        print("number is not prime")
