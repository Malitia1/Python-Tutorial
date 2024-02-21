# scope = Gültigkeitsbereich einer Variablen, das heißt, wo und wie lange eine Variable innerhalb eines Programms verwendet werden kann


name = "Bob"              # Globaler Gültigkeitsbereich (innerhalb und außerhalb der Funktion verfügbar)

def display_name():
    name = "Schulz"       # Lokaler Gültigkeitsbereich (nur innerhalb dieser Funktion verfügbar)
    print(name)

display_name()
print(name)



# Die LEGB-Methode in Python legt die Reihenfolge fest, in der Variablen nach ihrem Gültigkeitsbereich gesucht werden, 
# beginnend mit dem lokalen Bereich, gefolgt von umgebenden, globalen und eingebauten Bereichen

# L = Local     (Lokaler Bereich)
# E = Enclosing (Umgebender Bereich)
# G = Global    (Globaler Bereich)
# B = Built-in  (Eingebauter Bereich)




# Beispielcode aus ChatGTP:
x = 10                  # Globaler Gültigkeitsbereich

def outer():
    y = 20              # Umgebender Gültigkeitsbereich
    
    def inner():
        z = 30          # Lokaler Gültigkeitsbereich
        print(x, y, z)  # Zugriff auf Variablen aus verschiedenen Gültigkeitsbereichen
    
    inner()

outer()