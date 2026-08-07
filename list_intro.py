#-----an intro to lists
#example 1 - simple list

numbers = [1, 3, 5, 7, 11]
names = ["muaz", "murat", "lele" ]

#print(names)
#print(numbers)

#example 2 - a list of lists

likes = [["apple", "green"], ["yellow", "zeha"]]
#print(likes)

#example 3 -> a list of lists of lists

mixed = [[2, 3], "animal", "human", [4, True, "dragon", "ape"]]
#print(mixed)

#example 4 -> a list of identical items

Dragons = ["Drake"] * 10
#print(Dragons)

#example 4 -> a list merging or concatenation

numbers = [2, 3, 5, 6, 1]
cities = ["NYC", "Birmingham", "London", "Istanbul", "Bursa"]
games = ["Oblivion Remaster", "Skyrim", "Witcher 3", "Fallout NV"]

mix_them = numbers + cities + games
#print(mix_them)

#--------The list method------------
#example 1

number = list(range(100))
#print(number)

#example 2
name = list("yakub abdullahi wallahi billahi tillahi")
#print(name)

#example 3
#print(len(name))

#--------Accessing lists items-----------
#example 1

numero = [3, "Enes", "leko", 12, "muaz", "syntax"]
numero[4] = "zeho"
#print(numero)

#print(numero[2])

# example 2 - range
#print(numero [0: 4])

#example 3 -acces list item via step
#print(numero[::2])
#print(numero[::2])
#print(numero[::-1])
#print(numero[2::2])
#print(numero[0:5:2])

#---------list unpacking--------
#example 1

#numbers = [23, 34, 56]
#num1, num2, num3 = numbers

#print(num1)
#print(num2)
#print(num3)

#example 2
numbers = [23, 34, 56, 3, 4, 14, 51, 5]
#num1, num2, *other_nums = numbers
#print(num2)
#print(other_nums)

#-------------looping over lists--------
#example 1
letters = ["a", "b", "c"]

#for letter in letters:
 #   print(letter)

#example 2
for letter in enumerate(letters):
    print(letter)

#example 3
#item = (0,"a")
#index, letter = item
#print(index, letter)

#example 4
for index, item in enumerate(letters):
    print(index, item)

#---------modifying list items part 1----------
#numbers = [2, 5, 6, 7, 8, 9, 10]
names = ["john", "pork", "wilson", "mukesh", "lela"]
food = ["kebab", "pizza", " pasta", "cake", "humus"]

#example 1 append()
names.append("blackbeard")
print(names)

#example 2 insert()
food.insert(2, "poop")
print(food)

#example 3 pop()
#numbers.pop(2)
#print(numbers)

#example 3 remove()
#food.remove("kebab")
#print(food)

#example 4 del statement
#del numbers [0:4]
#print(numbers)

#---------modifying list items part 2------------
#example 1 clear()
print(food.clear())

#example 2 reverse()

numbers.reverse()
print(numbers)

#example 3 join()
print("./ ".join(names))

#-------finding list items
food = ["kebab", "pizza", "pizza", "pasta", "cake", "humus"]

#example 1 index()
print(food.index("pizza"))

#example 2

#if "apple" in food:
#    print(food.index("apple"))

#example 3
print(food.count("apple"))
print(food.count("pizza"))
print(food.count("pasta"))

#--------sorting lists------------
#example 1 sort()
#number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#number.sort()
#print(number)

#number.sort(reverse=True)
#print(number)

#example 2 sorted()
#print(sorted(number))
#print(sorted(number, reverse=True))

#example 3 sort()

product = [
    ("t-rex", 10),
    ("laptop", 500),
    ("apple watch", 299),
    ("shirt", 100),
]

#product.sort()
#print(product)

#example 4 sort() from cheap to expensive
def sort_products(product):
    return product[1]

product.sort(key=sort_products)
print(product)

#-----list comprehension expression part 1-----
numbers = [2, 22, 23, 42, 49, 69]
fruits = ["apple", "grape", "banana", "watermelon"]

#example 1
#numbers2 =[num for num in numbers]
#print(numbers2)

#example 2 - multiply
numbers2 = [num*2 for num in numbers]
print(numbers2)

#example 3 - divide then multiply
numbers2 = [(num / 2)* 45 for num in numbers]
print(numbers2)

#example 4
fruits2 = [fruit.upper() for fruit in fruits]
print(fruits2)

fruits2 = [fruit.lower() for fruit in fruits]
print(fruits2)

#example 5
products = [
    ("t-rex", 10),
    ("laptop", 500),
    ("apple watch", 299),
    ("shirt", 100),
]

items = [item for item in products]
items = [item[1] for item in products]
print(items)

#-----------list comprehension expression part 2-----
#example 1 - single condition
item = [item[1] for item in products if item[1] >= 150]
print(item)

#example 2 - dividing the numbers that are greater or lower
numberss= [ 24, 51, 55, 221, 42, 111, 1234, 422, 14, 50]
modified_numbers = [num if num > 100 else num / 2 for num in numberss]
modified_numbers = [num if num < 100 else num / 2 for num in numberss]
print(modified_numbers)

#---------swapping list items----------
#example 1
full_name = ["Enes", "Eroglu"]
full_name[0], full_name[1] = full_name[1], full_name[0]
print(full_name)
