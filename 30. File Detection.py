# File Detection = Prozess, bei dem überprüft wird, ob eine bestimmte Datei oder ein bestimmter Dateityp vorhanden ist oder nicht

import os

# path = "C:\Users\karol\Desktop" :
path = "C:\\Users\\karol\\Desktop\\test.txt" 


if os.path.exists(path):                # Suchen, ob Dokument auf dem PC vorhanden ist
    print("That location exist!")
    if os.path.isfile(path):            # Herausfinden, ob es sich um eine Datei handelt
        print("That is a file")
    elif os.path.isdir(path):           # Herausfinden, ob es sich um ein Ordner handelt
        print("That is a directory!")
else:
    print("That location doesn't exist!")