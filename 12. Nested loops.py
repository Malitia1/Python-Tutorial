# nested loop = Eine Schleife innerhalb einer anderen Schleife

rows = int(input("How many rows?: "))                   # Reihe       
columns = int(input("How many columns?: "))             # Spalte
symbol = (input("Enter a symbol to use: "))             # Symbol 

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")                           # Verhindert so, danach in die nächste Zeile zu springen. Es wird in einer Reihe geschrieben, bis rows beendet ist   
    print()                         
