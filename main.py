"""
Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal sobiva sõnumi.
Kasutaja sisestab ühe sõna:
"tööpäev"
või "puhkepäev"
Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst: "Ma lähen magama, head ööd!"
Kui sisestus on "puhkepäev", siis kuvatakse ekraanile tekst: "Veel üks osa Netflixist" 
"""

#Programm alustab.
#Küsi kasutajalt: "Mis päev homme on (tööpäev või puhkepäev)?".
#Salvesta vastus muutujasse day.
#Kui day on võrdne sõnaga "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!".
#Kui day on võrdne sõnaga "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist".
#Kui sisestus ei olnud õige, siis väljasta ekraanile: "Vale väärtus".
#Programm lõppeb.

""" 
day = input("Mis päev homme on? (tööpäev või puhkepäev): ")
if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist")
else:
    print("Vale väärtus") 
"""

#Finantsnõustaja
""" 
Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palkanud range ja vastutustundliku finantsnõustaja prgorammi kujul.
See programm:
- küsib, kui palju sul praegu raha on,
- võrdleb seda iPhone 17 Pro hinnaga (näiteks 2500 €)
- ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. 
"""
"""
print("Tere tulemast programmi 'Finantsnõustaja!'")
print("Sinu isiklik nõustaja ei tee emotsioonaalseid oste.")
money = int(input("Kui palju raha sul praegu on? "))
if money < 2500:
    print("Sul pole veel piisavalt raha. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta uue iPhone 17 Pro!")
else:
    print("Palju õnne, saad osta uue iPhone 17 Pro ja raha jääb isegi üle!")
"""

#Sammulugeja
"""
Sul on eesmärk teha iga päev vähemalt 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
- Kui protset < 50: "Alles poolel teel, liigu edasi!"
- Kui protsent < 75: "Tubli, oled peaaegu kohal!"
- Kui protsent >= 100: "Palju õnne, oled oma eesmärgi täitnud!"
"""

goal = 10000
steps = int(input("Mitu sammu oled juba teinud?: "))
percent = (steps/goal)*100
print(f"{percent}% eesmärgist täidetud.")
if percent < 50:
    print("Alla poole tehtud, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")

