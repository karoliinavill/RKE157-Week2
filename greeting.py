""" 
Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“ 
"""

#Pseudokood:
#Programm alustab
#Küsi kasutajalt: "Mis on sinu perekonnanimi?".
#Salvesta vastus muutujasse surname.
#Küsi kasutajalt: "Mis on sinu sugu? (m/n)".
#Salvesta vastus muutujasse gender.
#Kui gender on võrdne sõnaga "m", siis väljasta ekraanile: "Tere, härra [Name]!".
#Kui gender on võrdne sõnaga "n", siis väljasta ekraanile: "Tere, proua [Name]!".
#Kui gender on midagi muud, siis väljasta ekraanile: "Tere tulemast, [Name]! (sugu ei olegi tähtis)."
#Programm lõppeb.

surname = input("Mis on sinu perekonnanimi?: ")
gender = input("Mis on sinu sugu? (m/n): ")
if gender == "m":
    print(f"Tere, härra {surname}!")
elif gender == "n":
    print(f"Tere, proua {surname}!")
else:
    print(f"Tere tulemast, {surname}! (sugu ei olegi tähtis).")