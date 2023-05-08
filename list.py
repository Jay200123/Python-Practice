names = ['Renyel','Ian','Neri','Edmon']

print("1st Name:", names[0])
print("2nd Name:", names[1])
print("3rd Name:", names[2])
print("4th Name:", names[3])

# counts the list backwards1
print("Last Name:", names[-1])
print("Second Last Name:", names[-2])

# specify the list range 
print(names[1:])
print(names[1:3])

#update the list content
names[0] = "Renyel Jay"
print(names[0])

name2 = ["Jhofel",'Ashong','Arnel','Wayle']
# name2.extend(names)

name2.append("Kevin")
name2.insert(3,"Iien")
name2.remove("Jhofel")

# name2.sort()
# name2.reverse()

print(name2)

