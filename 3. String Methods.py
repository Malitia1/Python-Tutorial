name = "Bob Schulz"

#Anzahl der Buchstaben
print(len(name))

#Buchstaben finden
print(name.find("B"))

#Großschreiben (Nur ersten Buchstaben im ersten Wort)
print(name.capitalize())

#Alle Buchstaben groß
print(name.upper())

#Alle Buchstaben klein
print(name.lower())

#True or False, ob es sich um eine Dizimalzahl (0 - 9) handelt
print(name.isdigit())

#True or False, ob es ein Buchstabe ist (macht False, wenn Leerzeichen dazwischen sind)
print(name.isalpha())

#Zählt, wie viele Buchstaben vorhanden sind
print(name.count("B"))

#Einzelne Buchstaben austauschen
print(name.replace("o", "i"))

#String mehrmals wiederholen
print(name*3)