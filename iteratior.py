 # RETURN AN ITERATOR FROM A TUPPLE AND PRINT EACH VALUE:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#ITERATE THE CHARACTERS OF A STRING:
mystr = "banana"
for x in mystr:
    print(x)

#STOP AFTER 20 ITERATIONS:
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
