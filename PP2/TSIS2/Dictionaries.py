#ex1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
#ex2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020
print(car)
#ex3
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
print (car)
#ex4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
print(car)
#ex5
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
print(car)