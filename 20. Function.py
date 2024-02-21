# Function = Isolierter Block von Code, der spezifische Aufgaben ausführen kann und wiederverwendbar ist


def hello(first_name,last_name,age):                # "def" = Schlüsselwort, um eine Funktion zu definieren und ihren Namen sowie ihre Parameter und den auszuführenden Code festzulegen  
                                                    # hello(first_name,last_name,age) = Parameter, dient um spezifische Aktionen auszuführen oder einen Wert zurückzugeben 
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print ("Have a nice day!")


# Folgende Funktion ist wichtig, sonst wird der Code ignoriert:
hello("Bob","Schulz",21)            # Hier kommt "Parentheses" (engl. Begriff für Klammern): Wird hier eingesetzt, weil Funktionen immer mit einer Reihe von Klammern enden
                                    # Werden Informationen in der Funktion () hinterlegt, heißen sie Argumente                   