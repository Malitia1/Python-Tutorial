# Set = (dt. "Mengen") Spezielle Art von Datentyp, der eine ungeordnete Sammlung von einzigartigen und unveränderlichen Elementen enthält, wobei jedes Element nur einmal in einem Set vorhanden sein kann


utensils = {"Fork","Spoon","Knife"}
dishes = {"Bowl","Plate","Cup"}

utensils.add("Napkin")          # fügt was hinzu
utensils.remove("Fork")         # entfert was
utensils.clear()                # entfernt alles
utensils.update(dishes)         # fügt in "utensils" komplett "dishes" dazu
dishes.update(utensils)         # fügt in "dishes" komplett "utensils" dazu

dinner_table = utensils.union(dishes)       #dishes.union(utensils) geht auch, Zeile 10 & 11 werden so zsm.gefasst

for x in dinner_table:
    print(x)                    # Reihenfolge wird willkürlich




# Um zu Vergleichen, was unterscheidet:
print(utensils.difference(dishes))

# Um zu Vergleichen, was gleich ist:
print(utensils.intersection(dishes))
