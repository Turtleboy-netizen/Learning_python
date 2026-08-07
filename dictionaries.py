#--------an introduction to dictionaries--------
#example 1

employee_info = {
    "name": "morwin",
    "age": 19,
    "ethnicity": "black",
    "best friend": "gerald"
    
}

print(employee_info)

#example 2 dict()

animal_name = dict(cat= "maya", dog="woof")
print(animal_name)

#----------accessing dictionary key values---------
#example 1
print(employee_info["name"])

#example 2 remove or change value or add
employee_info["age"] = 20
print(employee_info)

#example 3 checking if it exist/ get()
print(employee_info.get("height"))

#example 4
print(employee_info.get("height", 6.2))

#------dictionary methods part 1----------
#example 1 clear()
#employee_info = employee_info.clear()

#example 2 copy()
#employee_info = employee_info.copy()
#print(employee_info)

#example 3 fromkeys()

letters = {"a", "b", "c", "d", "e"}
numbers = [ 2, 3]

vowels = dict.fromkeys(letters, numbers)
print(vowels)

#print({}.fromkeys(employee_info))

#------dictionary methods part 2----------
#example 1 items()

#print(employee_info.items())
#print(employee_info)

#example 2 - delete selected one
#del employee_info['age']
#print(employee_info)

#example 3 keys()
#print(employee_info.keys())

#example 4
#del employee_info["name"]
#print(employee_info.keys())

#------dictionary methods part 3----------
#example 1 values()
print(employee_info.values())

#example 2 popitem()
#print(employee_info.popitem())
#print(employee_info)

#example 3 setdefault()
print(employee_info.setdefault("age"))

print(employee_info.setdefault("drinking"))

print(employee_info.setdefault("allergies", "yes"))
print(employee_info)

#-------------dictionary methods 4--------------
#example  1 pop()
#case 1 - a key that exist
#target_item1 = employee_info.pop("age")
#print(target_item1)
#print(employee_info)

#case 2 - a key that does not exist
#target_item2 = employee_info.pop("smoking","no" )
#print(target_item2)
#print(employee_info)

#case 3 
#target_item3 = employee_info.pop("Drinking" )
#print(target_item3)
#print(employee_info)

#example 2 update()
lost_key = {"game": "fallout"}
employee_info.update(lost_key)
print(employee_info)

employee_info.update (cat="mya", dog="vurto")
print(employee_info)

#---------------dictionary comprehensions part 1---------
#example 1
#coordinate = {}
#for x in range(5):
#    coordinate[x] = (((x * 5) / 2) + 12) - (2.4/1.2) * 6
#    print(coordinate)

coordinate = {x:(((x * 5) / 2) + 12) - (2.4/1.2) * 6 for x in range (5)}
print(coordinate)

#example 2 - change dollars to pound
#in dollar price
old_price = {"apple": 0.99, "bread": 1.99, "eggs": 2.50}

dollar_to_pound = 0.76

uk_price = {item: value * dollar_to_pound for (item, value) 
            in old_price.items()}
print(uk_price)
print(old_price)

#example 3
original_dict = {"john": 28, "maximus": 33, "stockton": 25, "jack": 20,
                 "jean": 37}

#even_dict = {k: v for (k,v) in original_dict.items() if v % 2 == 0}
#print(even_dict)

#-------------dictionary comprehensions part 2-----------
#example 1
#new_dict = {k: v for (k,v) in original_dict.items() if v % 2 != 0 if v>30}

#example 2 if else conditional dictionary

new_dict = {k: "old" if v > 30 else "young" for (k,v) in original_dict.items()}
print(new_dict)

#example 3 - nested dictionary 
#new_dictt = {}
#for k1 in range(2, 5):
#    new_dictt[k1] = {k2: k1 * k2 for k2 in range (1,6)}
#    print(new_dictt)

#example 4 
new_dictt = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2,5)
}
print(new_dictt)

#-----------iterating over dictionaries------------
random = {
    1: 456,
    2: 789,
    35:"yo",
    "is_employed": False
}

for key in random:
    print(key)

#example 2

employee_infos = {
    "name": "morwin",
    "age": 19,
    "ethnicity": "black",
    "best friend": "gerald"
    
}

for i in employee_infos:
    print(employee_infos[i])
