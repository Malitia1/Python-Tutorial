# copyfile() =  Kopiert den Inhalt einer Datei
# copy() =      copyfile() + Berechtigungsmodus + Ziel kann ein Verzeichnis sein
# copy2() =     copy() + kopiert Metadaten (Erstellungs- und Änderungszeiten der Datei)

import shutil

shutil.copyfile("testfür32.txt","copytestfür32.txt")   # SOURCE: Ursprung/Ausgangsposition eines Elements, DESTINATION: Ziel/Bestimmungsort, an den ein Element verschoben, kopiert oder übertragen wird