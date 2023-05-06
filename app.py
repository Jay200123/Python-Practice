print("This is a Shape")

print("    /|")
print("   / | ")
print("  /  |")
print(" /   |")
print("/____|")


fname = "Renyel Jay"
lname = "Sioc"
school = "TUP Taguig"
address = "Arago Street"
town = "Central Bicutan"
city = "Taguig City"
course = "Bachelor of Science in Information Technology"
age = 21

print("Hello Everyone Im", fname, lname)
print(age, "years old,")
print("Im from", address, town, city)
print("Currently Taking", course, "in", school)

university = "Technological University of the Philippines\n Taguig Branch"

print(university.lower()) # its makes all the capital letters in string to become lower case

string = "LIONS AND TIGERS"
print(string.lower().islower()) #islower functions check if the string being print is a lower case letter
#will return TRUE if the string is Lowercase
print(string.upper().islower()) #wil return a FALSE since the string is being printed as an Upper case letter

lowers = "uss iowa"
print(lowers.upper().isupper()) #isupper functions checks if the string  being print is an upper case letters
# will return TRUE if the string is Uppercase
print(lowers.lower().isupper()) # will return a FALSE since the string is in Lower Case

python= "Python is a Programming Language"
print("There is a total of ",len(python), "letters in the variable python") #len functions count the total characters a variable has

print(python[0]) #counts the index for the String inside the variable python 
# the count for string will start at 0 = P which is the first index of the variable python
print(python.index("P")) #P = 0 since the python counts the index starting to 0

My_name = "Renyel Jay Jimunsala"
print(My_name.replace("Jimunsala", "Sioc")) #replaces the string that was being printed in the console

country = "PHILIPPINES"
print("Country:",country.lower())
print("Country is in lower case:",country.lower().islower())
print("else", country.lower().isupper())
print("Country Character Length:", len(country))

my_City = "taguig"
print("City:", my_City.upper())
print("City is in Upper Case:", my_City.upper().isupper())
print("else", my_City.upper().islower())
print("City Character Length:", len(my_City))

names = ["Renyel Jay", "Ian Mark", "Edmon", "Neri"]
print("The First Name is:",names[0])
print("Second Name is:", names[1])
print("Third Name is:", names[2])
print("Last Name is:", names[3])