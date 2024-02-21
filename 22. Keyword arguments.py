# Keyword arguments =   Aufruf einer Funktion mit einem oder mehreren Argumenten, die durch ihre Parameter-Bezeichner (Schlüsselwörter) gekennzeichnet sind, 
#                       um die Lesbarkeit und Klarheit des Codes zu verbessern.
#                       Besonders nützlich, wenn eine Funktion viele Parameter hat oder der Aufrufer die Parameter-Reihenfolge nicht kennt.

#                       Argumente = Reihenfolge wichtig
#                       Keywords = Reihenfolge egal


def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

# Argumente:
hello("Bob","Bobby","Schulz")

# Keywords:
hello(last="Schulz",first="Bob",middle="Bobby")
