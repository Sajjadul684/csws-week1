names = ["Bob", "Timothy", "Jones"]
greetings = ["Hello By", "Good Evening", "Danke"]

print (greetings [0] + " " + names [0])
print (greetings [1] + " " + names [1])
print (greetings [2] + " " + names [2])

names.append ("Samuel")
print (names) #Adds name onto end of list

names.insert(3, "Liam") #inserting via element

del names[1] #deleting name

names.remove("Samuel") #removing via element

x = names.pop(3) #reusing deleted element