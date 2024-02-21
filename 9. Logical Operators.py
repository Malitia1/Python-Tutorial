# Logical Operators (and,or,not) = Überprüft, ob zwei oder mehr bedingte Anweisungen wahr sind

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:                    # AND: Beides MUSS erfüllt sein
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperatur is bad today!")
    print("Stay inside!")                       # OR: Solange eins von beiden erfüllt ist, ist das ganze Statement korrekt



# Wenn NOT eingebaut wird, wird True zu False und umgekehrt:
if not(temp >= 0 and temp <= 30):
    print("The temperatur is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")