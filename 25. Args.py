# *args = Parameter, der es einer Funktion ermöglicht, eine variable Anzahl von nicht-schlüsselwortbasierten Argumenten entgegenzunehmen und sie als Tupel zu behandeln


def add(*args):             # Name irreveant, wichtig ist das * 
    sum = 0
    args = list(args)       # So können zusätzliche Listen erstellt werden
    args[0] = 0
    for i in args:          # Muss Namen oben übereinstimmen
        sum += i
    return sum

print(add(1,2))