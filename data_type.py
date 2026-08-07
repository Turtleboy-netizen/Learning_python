#--------------Data typespart 1-----------------
#integer
age = 20
print(age)
print(type(age))

#floats
grade = 10
print(grade)
print(type(grade))

#booleans
alarm = True
offline = False
print(alarm, offline)
print(type(alarm))

#--------strings------------

movie_name = "the good, bad and ugly"
print(movie_name)
print(type(movie_name))

#------------Data Types part 2---------------------
# ordered
mixed = [1, 2, 3, 4, 5, True, "Enes Eroglu", [3, 2, 1] ]

#dictionary
#unordered
user_info = {"user_name": "TurtleBoy", "user_id": 69}
print(user_info)
print(type(user_info))

#Tuple
#ordered
mixed_tuple = (1, 2, 3, 4, 5, True, "Enes Eroglu", [3, 2, 1] )
#print(mixed_tuple)
#print(type(mixed_tuple))

#----Set-------
#unordered
mixed_set = {1, 2, 3, 4, 5, "its me", "Enes Eroglu", }
print(mixed_set)
print(type(mixed_set))

#-----------------String methods----------------------

# 1- len()
address = "United Kingdom"
print(len(address))

# 2- [] notation
print(address[0])
print(address[10])
print(address[-5])

# 3- [] Notation
print(address[0:14])
print(address[-8:-3])

#concatination ->>>> formatted strings combines or connects
country = "United Kingdom"
city = "Birmingham"
#full_address = city + ", " + country
full_address = f"{city}, {country}"
print(full_address)

#5- upper()
print(country.upper())

#6- lower()
print(city.lower())

#7- title
print(city.title())

#8- strip()
job = "    Programmer       "
print(job.strip())
print(job.lstrip())
print(job.rstrip())

#9- find()
print(address.find("N"))

# 10- replace()
print(address.replace("i", "o"))

# 11- in operetor = checks if the letters exists
print("ne" in city)
print("Bir" in city)
print("Un" in country)
print("ham" in city)

# 12- not operator = checks if the letters does not exist
print("Un" not in country)
print("Un" not in city)

