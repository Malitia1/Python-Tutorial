# Dictionary = (dt. "Wörterbuch") Datenstruktur, die eine Sammlung von Schlüssel-Wert-Paaren speichert und es ermöglicht, schnell auf die Werte zuzugreifen, indem man den zugehörigen Schlüssel verwendet


# Set erstellen mit Key:Value
capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Germany": "Berlin"})  # Es wird dem bereits codierten Dictionary was hinzugefügt
capitals.update({"USA":"Las Vegas"})    # Gibt dem Key ein neues Value an
capitals.pop("China")                   # Entfernt Key mit dazugehörigen Value
capitals.clear()                        # Entfernt komplettes Dictionary


print(capitals["Russia"])               # Key auswählen, in den [] werden die Keys statt Nummern ausgewählt
print(capitals.get("Germany"))          # Gibt an, ob Key im Dictionary vorhanden ist 
print(capitals.keys())                  # Gibt alle Keys an, die existieren
print(capitals.values())                # Gibt alle Values zu den Keys an, die existieren
print(capitals.items())                 # Gibt komplettes Dictionary an, was erstellt wurde

for key,value in capitals.items():      # For Loop, um komplettes Dictionary anzugeben (so wie in Zeile 14)
    print(key,value)    

