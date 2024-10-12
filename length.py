# methode:1
str="welcome"
counter=0
for i in str:
    counter=counter+1
print(counter)

# methode 2 using while loop and slicing
str="welcome"
counter=0
while str[counter:]:
    counter=counter+1
print(counter)
# using built-in funcvtion len()
str="welcome"
print(len(str))
# using join and count
str="welcome"
random_str="x"
print((random_str).join(str).count(random_str)+1)

# cheak string in special charatcer
import re
str="welcome@@to%%python programming@!!!"
regex=re.compile('[@#$5^&*^%$&(%)]')
if(regex.search(str)==None):
    print("no special character present in the string")
else:
    print("string contains special character")
    




