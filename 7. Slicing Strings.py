# slicing = Erstellt einen Teilstring, indem Elemente aus einem anderen String extrahieren werden
#           indexing[] or slice []
#           [start:stop:step]


#INDEXING[]:
name = "Karoline Klein"     # 0 ist die erste Zahl, also ist der gesamte Name 14 Ziffern lang

first_name = name[:4]           # [start]:  Man kann auch [0:4] schreiben, aber bei einem freien "start" Feld geht Python davon aus, dass 0 der Anfang ist
last_name = name[8:]            # [stop]:   Man kann auch [8:14] schreiben, aber bei einem freien "stop" Feld geht Python davon aus, dass es bis zum Ende des strings lesen soll ist
funky_name = name[::3]          # [step]:   Man kann auch [0:14:3] schreiben, aber bei freien "start" und "stop" Feldern macht Python oben genannte Schritte 
reversed_name = name [::-1]     # Umgedreht 


#SLICE():
website = "http://google.com" 
website2 = "http://wikipedia.com"

slice = slice(7,-4,)            # Beginn Websitenamen, dadurch fällt "http://" weg
                                # Ende Websitenamen mit negativer Index => letztes Zeichen -1, zweitletztes Zeichen -2, etc., dadurch fällt ".com" weg

print(website[slice]+" "+website2[slice])

