#esercizio_1

print("\n esercizio_1 \n")
posti_tot = int(input("inserisci numero massimo di posti nel parcheggio "))
posti_lib = posti_tot
posti_ocup = 0

for i in range(posti_tot):
    scelta = input("inserisci una delle seguenti opzioni 'ingresso', 'uscita, 'stato', 'esci' ")
    if scelta == "ingresso" and posti_lib > 0:
        print(f"Ci sono {posti_lib} posti liberi, entrate")
        posti_lib -= 1
        posti_ocup += 1
        print(f"Sono rimasti {posti_lib} liberi nel parcheggio")
    elif scelta == "uscita":
        posti_lib += 1
        posti_ocup -= 1
        print(f"Sono rimasti {posti_lib} liberi nel parcheggio")
    elif scelta == "stato":
        print(f"Sono rimasti {posti_lib} liberi nel parcheggio")
        print(f"Sono rimasti {posti_ocup} occupati nel parcheggio")
    else:
        scelta == "esci"
        break
