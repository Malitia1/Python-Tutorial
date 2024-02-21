# Variables = Wird verwendet, um Daten zu speichern und auf sie zu verweisen

# String (str) =        Eine Sequenz von Zeichen, die in " oder ' eingeschlossen wird
# Integer (int) =       Ganze Zahl ohne Dezimalstellen
# Float (float) =       Zahl mit einer Dezimalstelle oder einem Bruchteil
# Boolean (bool) =      Datentyp, der entweder True oder False als Wert haben kann               


#STR 
first_name = "Bob"
last_name = "Schulz"
full_name = first_name +" "+ last_name
print("Hello "+full_name)

#INT 
age = 21
age = age + 1   # oder: age += 1
print(age)

#INT + STR 
age = 21
age  += 1
print("Your age is: "+str(age))

#FLOAT + STR
height = 180.5
print("Your height is: "+str(height)+" cm")

#BOOL + STR
human = True
print("Are you a human?: "+str(human))