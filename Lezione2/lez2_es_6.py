#esercizio_6-1
print(" \n   Esercizio_6-1\n")

mydict: dict = { "first_n": "Anna", 
"last_n": "Bozi", "age": 29, "city": "Rome"}
for k, v in mydict.items():
    print(k,v)
    
#esercizio_6-2
print(" \n   Esercizio_6-2\n")

mydict1: dict = { "Anna":7, "Marco":17,
"Giuseppe":88, "Feserica":25}
for k, v in mydict1.items():
    print(f"A {k} piace numero {v}")
    
    
#esercizio_6-3
print(" \n   Esercizio_6-3\n")

mydict3: dict = {
    ".append": "aggiunge elemento",
    ".remove": "elimina elemento",
    ".extend": "allargaa la lista",
    ".sort": "mette elementi in ordine alf.",
    ".reverse": "cambia indici dei elementi al contrario"}

for k, v in mydict3.items():
    print(f" {k} \n      {v}")
    
#esercizio_6-3
print(" \n   Esercizio_6-3\n")

first_dict: dict = { "first_n": "Anna", 
"last_n": "Bozi", "age": 29, "city": "Rome"}

second_dict: dict = { "first_n": "Marco", 
"last_n": "Rossi", "age": 21, "city": "Napoli"}

third_dict: dict = { "first_n": "Stefano", 
"last_n": "D'Omo", "age": 32, "city": "Milano"}
  
name_list: list = [first_dict, second_dict, third_dict]  
for i in name_list:
    print(i)

    
    

#esercizio_6-1
print(" \n   Esercizio_6-1\n")

mydict: dict = { "first_name": "Anna", 
"last_name": "Bozi", "age": 29, "city": "Rome"}
for k, v in mydict.items():
    print(k,v)
    



#esercizio_6-2
print(" \n   Esercizio_6-2\n")

mydict1: dict = { "Anna":7, "Marco":17,
"Giuseppe":88, "Feserica":25}
for k, v in mydict1.items():
    print(f"A {k} piace numero {v}")
    


    
#esercizio_6-3
print(" \n   Esercizio_6-3\n")

mydict3: dict = {
    ".append": "aggiunge elemento",
    ".remove": "elimina elemento",
    ".extend": "allargaa la lista",
    ".sort": "mette elementi in ordine alf.",
    ".reverse": "cambia indici dei elementi al contrario"}

for k, v in mydict3.items():
    print(f" {k} \n      {v}")


    
    
#esercizio_6-7
print(" \n   Esercizio_6-7\n")

first_dict: dict = {
    "first_n": "Anna", 
    "last_n": "Bozi", 
    "age": 29, 
    "city": "Rome"}

second_dict: dict = {
    "first_n": "Marco", 
    "last_n": "Rossi", 
    "age": 21, 
    "city": "Napoli"}

third_dict: dict = {
    "first_n": "Stefano", 
    "last_n": "D'Omo", 
    "age": 32, 
    "city": "Milano"}
  
name_list: list = [first_dict, second_dict, third_dict]  
for i in name_list:
    print(i)

    


#esercizio_6-8
print(" \n   Esercizio_6-8\n")

asia_dict: dict = {
    "animal": " cat",
    "name": "Asia", 
    "owner's_name": "Alex",
    "gender": "female",
    "color": "brown",
    "age": 12}

lilu_dict: dict = {
    "animal": " dog",
    "name": "Lilu", 
    "owner's_name": "Natallia",
    "gender": "female",
    "color": "panna",
    "age": 7}

tancredi_dict: dict = {
    "animal": " cat",
    "name": "Tancredi", 
    "owner's_name": "Rita",
    "gender": "male",
    "color": "wight",
    "age": 9}

pets_list: list = [asia_dict, lilu_dict, tancredi_dict]
for i in pets_list:
    print(i)

print("\n    versione 2\n")
pets_dict: dict ={1:asia_dict,
                  2:lilu_dict,
                  3:tancredi_dict}

# for value in pets_dict.values():
#     for k,v in value.items():
#        #print(k,v)
#     print(value)

for k, v in pets_dict.items():

    for k1, v1 in v.items():

        print(f"{k1}, {v1}")



#esercizio_6-9
print(" \n   Esercizio_6-9\n")

favorite_place: dict = {
    "Chiara": "Roma",
    "Daniele": "Valenzia",
    "Esubalew": "Cancune",
    "Gian Marco": "Bali"}
for k, v in favorite_place.items():
    print(f"Il posto preferito di {k} è {v}")


 
#esercizio_6-10
print(" \n   Esercizio_6-10")

mydict1: dict = { "Anna":[7,5,77,56], "Marco":[17,94,8,3],
"Giuseppe":[88,63,83,3], "Feserica":[28,7,29,25]}
for k, v in mydict1.items():
    print(f"A {k} piaciono i numeri {v}")
    


#esercizio_6-11
print(" \n   Esercizio_6-11")

city_dict: dict = {
    "Roma": {"country":"Italy",
             "popolation": "2.76 million",
             "monuments": "Colosseo"},
    "Paris": {"country":"France",
             "popolation": "2,1 million",
             "monuments": "Eiffel Tower"},
    "Berlin": {"country":"German",
             "popolation": "3,44 million",
             "monuments": "Branderbuge Gate"}}

for k,v in city_dict.items():
    print(k,v)
