# while loop = Eine Anweisung, die ihren Codeblock ausführt, solange ihre Bedingung wahr bleibt

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)



# Alternativer Code, um NOT einzubringen:
name = None

while not name:
    name = input("Enter your name: ")

print("Hello "+name)