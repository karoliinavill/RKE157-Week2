""" Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """

#Pseudokood:
#Programm alustab
#Küsi kasutajalt: "Kui mitu klaasi vett oled juba joonud? (üks klaas = 250 ml)".
#Salvesta vastus muutujasse glasses.
#Arvuta täidetud protsent = (glasses * 250) / 2000 * 100
#Kui protsent < 50, siis väljasta: "Joo rohkem vett, keha vajab seda!".
#Kui protsent < 100, siis väljasta: "Tubli, jätka samas vaimus!".
#Kui protsent ≥ 100, siis väljasta: "Suurepärane, oled oma päevase eesmärgi täitnud!".
#Programm lõppeb.

goal = 2000
glasses = int(input("Kui mitu klaasi vett oled juba joonud? (üks klaas = 250 ml): "))
percentage = (glasses * 250) / goal * 100
if percentage < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percentage < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
