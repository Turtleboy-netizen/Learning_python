#type casting is the process of converting a value of one 
#data type to another. can convert (string, integer, floats boolean)
#explicit type casting - manually converting
name = "Enes"
age = 20
gpa = 2.6
is_student = True

#print (type(name))
#print (type(age))
#print (type(gpa))
#print (type(is_student))

#Converting integer to float. (str, int, float, bool)
age = float(age)
print(age)

#Implicit type casting is when a value is 
# converted into a different data type automatically

x = 10
y = 3
x = x/y
print(x)
string_a = "I am "+ str(x) + " years old "+ str(5)
#string_a = "I am 20 "+"years old"
print(string_a)


