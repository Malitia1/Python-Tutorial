# Loop Control Statements =  Anweisungen, die innerhalb von Schleifen verwendet werden um das Verhalten der Schleife zu steuern

# break =       Wird verwendet, um die Schleife vollständig zu beenden
# continue =    Springt zur nächsten Iteration der Schleife
# pass =        Tut nichts, fungiert als Platzhalter



# BREAK:
while True:
    name = input("Enter your name: ")
    if name != "":                          # != bedeutet "nicht gleich"
        break                               # Loop wird hier beendet 



# CONTINUE:
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue                            # Restlichen Anweisungen in der aktuellen Schleife sollen übersprungen und direkt mit dem nächsten Schleifendurchlauf fortgefahren werden
    print(i, end="")                        # end="" sorgt dafür, dass die Zahlen in einer einzigen Reihe bleiben


# PASS:
for i in range(1,21):

    if i == 13:
        pass                                # Platzhalter, der verhindert, dass das Programm eine Fehlermeldung ausgibt (hier wird 13 ausgelassen)
    else:
        print(i)