
# try:
with open("C:\\Selbstlernen\\Youtube - Tutorial\\31. test.txt") as file:
    print(file.read())
# except FileExistsError:
#     print("That file was not found :( ")    

print(file.closed)              # True: Datei bereits geschlossen, False: Datei noch geöffnet
                                # Dient zur Überprüfung, ob eine Datei erfolgreich geschlossen wurde