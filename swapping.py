# num1 = 12
# num2 = 15
num1 = int(input("enter the value: "))
num2 = int(input("enter the value: "))

print("value of num1 before swapping:",num1)
print("value of num2 befre swapping:",num2)

# approch 1
# temp=num1
# num1=num2
# num2=temp

# approch 2
num1,num2 = num2,num1

print("value of num1 after swapping:",num1)
print("value of num2 after swapping:",num2)

