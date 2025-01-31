
#esercizio_2-3
print("\n esercizio_2-3\n")
x = input("whrite your name  ")
print(f"Hello {x}, would you like to learn some Python today?")

name: str = "Flavio"
print(f"Ciao {name}, come stai?")



#esercizio_2-4
print("\n esercizio_2-4\n")
name: str = "Marco"
print(f"lower: {name.lower()}, title: {name.title()}, upper: {name.upper()}")



#esercizio_2-5
print("\n esercizio_2-5\n")
name: str = "Lao Tzu"
quote: str = "A journey of a thousand miles begins with\
 a single step"
print(f"{name} once said, \n \"{quote}\"")


#esercizio_2-6



#esercizio_3-1
print("\n esercizio_3-1\n")
mylist: list = ["Anna", "Carla", "Alex", "Pipo"]
for i in mylist:
    print(i)



#esercizio_3-2
print("\n esercizio_3-2\n")
mylist2: list = ["Anna", "Carla", "Alex", "Pipo"]
for i in mylist2:
    print(f"{i} i'am very glad to see you!")
#print(f"\n Lista dei nomi {*mylist})
print(*mylist2)



#esercizio_3-3
print("\n esercizio_3-3\n")
mylist3: str = ["Mersedes", "BMW", "Tesla"]
#print(*mylist3)
for i in mylist3:
    print(f"I would like to own a {i} car")



#esercizio_3-4
print("\n esercizio_3-4\n")
guest_list: list = ["Marilyn Monroe", "John F. Kennedy", "Jacqueline Kennedy"]
for i in guest_list:
    print(f"Dear {i} would you like to come to diner?")



#esercizio_3-5
print("\n esercizio_3-5\n")
guest_list_refuse: list = ["John F. Kennedy"]
print(f"{guest_list_refuse} can not come")
guest_list.remove("John F. Kennedy")
guest_list.insert(1, "Elton John")
for i in guest_list:
    print(f"Dear {i} would you like to come to diner?")



#esercizio_3-6
print("\n esercizio_3-6\n")
print("I found a bigger table, so we have more avaible space")
guest_list.extend(["Anna", "Marco", "Stefano"])
for i in guest_list:
    print(f"Dear {i} would you like to come to diner?")



#esercizio_3-7
print("\n esercizio_ 3-7\n")
print(*guest_list, sep= ", ")
print("I am so sorry, we have space only for 2 people")
for i in guest_list[2:]:
    print(f"Dear {i} we are so sorry, we can't invite you to diner")
    guest_list.pop()
print(*guest_list, sep= ", ")
for i in guest_list:
    print(f"Dear {i} would you like to come to diner?")

del guest_list
#print(guest_list)



#esercizio_3-8
print("\n esercizio_3-8\n")
loc_list: list = ["Japone", "America", "Swizzera", "Francia", "Nepal"]
print(*loc_list, sep= ", ")
sort_list = sorted(loc_list)
print(*sort_list, sep= ", ")
sort_list.reverse()
print(*sort_list, sep= ", ")
sort_list.reverse() 
print(*sort_list, sep= ", ")
loc_list.sort()
print(*loc_list, sep= ", ")
loc_list.sort(reverse=True)
print(*loc_list, sep= ", ")



#esercizio_3-9
print("\n esercizio_3-9\n")
guest_list: list = ["Marilyn", "John", "Jacqueline", "Anna", "Marco", "Stefano"]
x = len(guest_list)
print(f"We invited {x} people to dinner")



#esercizio_3-10
print("\n esercizio_3-10\n")
mylist: list = ["asterisco", "apice", "doppio aoice", "backslash", "hashtag"]
mylist.sort()
print(*mylist, sep= ", ")
mylist.sort(reverse=True)
print(*mylist, sep= ", ")


