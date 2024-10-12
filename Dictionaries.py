#STRING,INT,BOOLEAN, AND LIST DATA TYPES:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "date": 2022,
    "colors": ["red", "white", "blue"]
    
}
print(thisdict)

#NEW ITEM ADD TO THE GENERAL DICTIONARY,
car = {
    "brand": "ford",
    "model": "mustang",
    "year": 2022
}
x = car.keys()
print(x)  #before the change
car["color"] = "white"
print(x)  # after the change

#prectice
quality = {
    "product": "Himaliya",
    "price": 200,
    "colour": "broun",
     
}
x = quality.keys()
quality["brand"] = "lotus"
quality["colour"] = "red"
print(quality)


