#ex1 
import json
x='{"name": "John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y["age"])
#ex2
x={
    "name": "John",
    "age": 30,
    "city": "New York"
}
y=json.dumps(x)
print(y)
#ex3 
print(json.dumps({"name":"John", "age":30}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#ex4
x={
    "name":"John",
    "age": 30,
    "married":True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge", "mpg":24.1}
    ]
}
print(json.dumps(x))

#ex5
json.dumps(x, indent=4)
#ex6
json.dumps(x,indent=4,separators=(".", "="))
#ex7
json.dumps(x, indent=4, sort_keys = True)