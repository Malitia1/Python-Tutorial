# list = Mehrere Elemente sollen in einer einzigen Variable gespeichert werden

food = ["Pizza", "Hamburger", "Hotdog", "Spaghetti", "Pudding"]        # Pizza = 0, Hamburger = 1, Hotdog = 2, Spaghetti = 3, Pudding = 4

food[0] = "Sushi"                                                      # UPDATE: Sushi = 0, dadurch wird Pizza ersetzt

food.append("Ice Cream")    # Weitere Sachen werden hinzugefügt, ohne Zeile 3 zu ändern
food.remove("Hotdog")       # Es werden Dinge entfernt, ohne Zeile 3 zu ändern
food.pop()                  # Löscht letztes Element, hier "Pudding" aus Zeile 3
food.insert(0,"Cake")       # 0 = Pizza und wird durch Cake ersetzt 
food.sort()                 # Sortiert alphabetisch
food.clear()                # Löscht alle Elemente aus der Liste


for x in food:                                                         # Gibt so alle Werte an, die in der Liste (hier "food") angegeben wurden
    print(x)