

#esercizio_1
print("    Esercizio 1\n ")
x = 2.57
y = 1.0 / x
prod = x * y
dif = prod - x
print(f"x = {x}")
print(f"y = {y}")
print(f"x * y = {prod}")
print(f"(x * y) - x = {dif}")




#esercizio_2
print("\n   Esercizio 2\n")
x = 6.57
y = x % 2.0 
print(f"x = {x}")
print(f"Resto della divisione x % 2.0 = {y}")



#esercizio_3
print("\n   Esercizio 3 versione 1\n")
x = int(input("inserisci il numero per calcolare la media  "))
y = int(input("inserisci il numero per calcolare la media  "))
z = int(input("inserisci il numero per calcolare la media  "))
media = (x + y + z)/3
print(f"Media di 3 numeri inseriti è {media:.1f}")

print("\n   Esercizio 3 versione 2\n")
somma=0
quantita_numeri=3
for i in range(quantita_numeri):
    x = int(input("inserisci il numero per calcolare la media  "))
    somma += x
media = somma / quantita_numeri
print(f"Media di {quantita_numeri} numeri inseriti è {media:.1f}")



#esercizio_4
print("\n   Esercizio 4\n")
x = "2024"
for i in x:
    print(i)



#esercizio_5
print("\n   Esercizio 5\n")
x = int(input("Inserisci temperatura in gradi Fahrenheit  "))
y = 5 * (x - 32) / 9
print(f"{x} gradi Fahrenheit corrispondono a {y:.1f} gradi Celsius")



#esercizio_6
print("\n   Esercizio 6\n")
menu = {"Pizza":9.00, 
"Pasta":10.50,
"Zuppa":7.00,
"Hamburger":15.50,
"Cotoletta":10.00,
"Salmone":20.20,
"Patatine fritte":5.50,
"Patate al forno":5.50,
"Verdura del giorno":7.00,
"Cheesecake":6.00,
"Tiramisu":6.00,
"Focaccia cin Nutella":6.00,
"Coca Cola":3.50,
"Acqua":1.50,
"Vino":5.00}

ordine = {"Zuppa":7.00,
"Salmone":20.20,
"Verdure del giorno":7.00,
"Tiramisu":6.00,
"Acqua":1.50}

print("  Menu contiene:")
for k,v in menu.items():
   print(k,v)

print("\n  Ordine del cliente")
for k,v in ordine.items():
    print(k,v)

da_pagare = 0
da_pagare = da_pagare + ordine["Zuppa"]
da_pagare += ordine["Salmone"]
da_pagare += ordine["Verdure del giorno"]
da_pagare += ordine["Tiramisu"]
da_pagare += ordine["Acqua"]
print(f"\nTotale da pagare è {da_pagare}") 

somma = 0
for i in ordine.values():
    somma += i
print(f"\nTotale da pagare è {somma}\n")
 

for k, v in ordine.items():
    print(f"Piatto: {k} Prezzo: {v} Euro")
 

