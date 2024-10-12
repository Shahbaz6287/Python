str1="B7DJDN"
alphabets=[]
number=[]
for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        number.append(ch)
final_list=(sorted(alphabets))+(sorted(number))
output= ''.join(final_list)
print(output)

# prectice
str1=input("enter the string: ")
n = int(input("enter a count"))
str1=str1.split()
counts=dict()
for word in str1:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
    print(counts)

 