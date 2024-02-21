# str.format() = Methode, mit der Platzhalter in einem String durch Werte oder Variablen ersetzt werden können, um formatierte Zeichenketten zu erzeugen


animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)


# Elegantere Möglichkeiten zu Zeile 7:
print("The {} jumped over the {}".format(animal,item))                                  # Alternativ .format("cow","moon")
print("The {0} jumped over the {1}".format(animal,item))                                # Positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))           # Keyword argument


# Elegantere Möglichkeit zu Zeile 12:
text = "The {} jumped over the {}"
print(text.format(animal, item))







# Wenn wir die format-Methode verwenden, können wir einer Zeichenkette eine zusätzliche Lücke hinzufügen, wenn wir sie anzeigen möchten

name = "Bob"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10} Nice to meet you.".format(name))         # 10 Leerzeichen hinter dem Namen
print("Hello, my name is {:<10} Nice to meet you.".format(name))        # "Left align" = Auf linke Seite ausgerichtet
print("Hello, my name is {:>10} Nice to meet you.".format(name))        # "Right align" = Auf rechte Seite ausgerichtet
print("Hello, my name is {:^10} Nice to meet you.".format(name))        # "Center align" = Zentriert






# Mit Nummern arbeiten:

number = 3.14159

print("The number Pi is {:.3f}".format(number))                         # Gibt nur die ersten 3 Zahlen nach dem Komma wieder. Rundet auf


number = 1000

print("The number is {:,}".format(number))                              # Fügt automatisch ein Komma in Tausenderschritte ein
print("The number is {:b}".format(number))                              # Gibt in Binärzahl wieder
print("The number is {:o}".format(number))                              # Gibt in Oktalzahl wieder
print("The number is {:x}".format(number))                              # Gibt in Hexadecimal wieder (kleines x in Kleinbuchstaben, großes X in Großbuchstaben)
print("The number is {:e}".format(number))                              # Gibt in wissenschaftlicher Notation bzw. Exponentialdarstellung wieder (kleines e in Kleinbuchstaben, großes E in Großbuchstaben)