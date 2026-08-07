#----------- Escape Sequences----------------

import math


story_desc = "it\"s a touching story \n but For the Empire!!!!"
print(story_desc)

#---------number methods & operations ##---------

#Arithmetic Operations or math
#print(5+30)
#print(69-2)
#print(5*10)
#print (50/5)
#print(2 ** 5) 

#augmented assignment operator
number = 10
#number = number + 9
number += 9
print(number)

# 1- number method ()
print(round(4.281731))

# 2- abs ()
print(abs(-1.45))

# https://docs.python.org/3/library/math.html

print(math.sin(180))
print(math.cos(0))
print(math.ceil(1.1))

#-------------type conversion----------------

number = input("number: ")
print(type(number))

# int()
# float()
# str()
# bool()

#y = int(number) + 202
#print(y)
#print(type(y))

number = 1001

print(id(number))
print(id(1001))

a = 2
print("a:", id(a))

a = a + 1
print("a1:", id(a))
print("Three:", id(3))

something = 12
something = "Jack"
something = ["a", 2, True]

def hello():
    print("hello world")

something = hello
something()

#--------namespace part 2---------------

def outer():
    outer_number = 100
    print(id(outer_number))

    def inner():
        inner_number = 200
        print("inner number =", inner_number)

        print(id(outer_number))
        print("outer number=", outer_number)
       
    inner()
 
global_number = 300

outer()

#-------------input & output------------------
#example output
first_name = "enes"
last_name = "eroglu"

print("my first name is {} and my last name is {}, so my full name is {} {}".format(first_name, last_name, first_name, last_name))

#example input
