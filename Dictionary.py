print("Dictionary")

dict = {
        "Name":"Narendra",
        "age":21,
        "Country":"India"
}

# dict.clear()
print(dict)

print(dict["Name"])
print(dict["age"])
dict.update({"age":20})
print(dict)

print(dict.keys())
print(dict.values())

dict.pop("age")
print(dict)