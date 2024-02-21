# exception = Fehler oder Ausnahme, die während der Ausführung eines Programms auftritt und den normalen Ablauf unterbricht

try: 
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:                           # Wenn 0 eingegeben wird
    print(e)                                             # Optional: Erklärt im Terminal, was genau das Problem ist
    print("You can't divide by zero, idiot.")
except ValueError as e:                                  # Wenn ein Wort eingeben wird
    print(e)                                             # Erklärt im Terminal, was genau das Problem ist
    print("Enter only numbers plz")
except Exception as e:                                   # Wenn normalerweise hier Fehler auftritt
    print(e)                                             # Erklärt im Terminal, was genau das Problem ist
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will alway execute.")