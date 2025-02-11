'''
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

        '''

#esercizio_2

print("\n esercizio 2 \n")

nord_sud = int(input("Inserisci numero di veicoli nella direzione Nord Sud  "))
est_ovest = int(input("Inserisci numero di veicoli nella direzione Est Ovest  "))
soglia = int(input("Inserisci la soglia predefinita  "))
if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
else:
    if nord_sud > soglia:
        time_ns = 60
        time_eo = 40
    else:
        if est_ovest > soglia:
            time_ns = 40
            time_eo = 60
        else: 
            time_ns = (nord_sud/(nord_sud + est_ovest))*100
            time_eo = (est_ovest/(nord_sud + est_ovest))*100
print(f"Il tempo assegnato alla direzione Nord-Sud è {time_ns:.1f}")
print(f"Il tempo assegnato alla direzione Est-Ovest è {time_eo:.1f}")


#esercizio3

print("\n esercizio 3 \n")

