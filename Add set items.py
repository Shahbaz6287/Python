#ADD ELEMENT FROM TROPICAL INTO THISSET:
# thisset = {"apple", "banana", "papaya"}
# tropical = {"pineapple", "mango", "cherry"}

# thisset.update(tropical)
# print(thisset)

# ADD ELEMENT OF A LIST TO AT SET
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)
# prectice
thisset = {"radha", "mira", "radha"}
mylist = ["gopalganj", "barauli"]
thisset.symmetric_difference_update(mylist)
print(thisset)
