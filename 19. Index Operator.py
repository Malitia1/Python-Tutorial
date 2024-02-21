# Index Operator [] = Wird mit eckigen Klammern ([]) verwendet, ermöglicht den Zugriff auf einzelne Elemente in einer Sequenz (String, Liste oder Tuple)


# Benutzen String:
name = "Bob Schulz!"

if(name[0].islower()):
    name = name.capitalize()        # Falls der erste Buchstabe des Names klein ist, wird es hier groß angegeben

first_name = name[:3].upper()       # Bestimmen Vornamen und wollen nur die ersten 3 Buchstaben, die komplett Groß dargestellt werden sollen
last_name = name[4:].lower()        # Bestimmen Nachnamen und wollen nur die letzten Buchstaben, die komplett Klein dargestellt werden sollen
last_character = name[-1]           # Gibt nur negativen Index wieder => letztes Zeichen -1, zweitletztes Zeichen -2, etc.


print(first_name)
print(last_name)
print(last_character)


