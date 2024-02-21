# Datei wird ins Desktop verschoben:


import os

source = "test.txt"                                          # oder Dateipfad
destination = "C:\\Users\\karol\\Desktop\\test.txt"          # "C:\Users\karol" war Original, Rest manuell hinzugefügt


try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")