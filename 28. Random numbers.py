import random

x = random.randint(1,6)
y = random.random()             # Random floating number zwischen 0 und 1

print(x)
print(y)


# Zufällige Auswahl aus einer Liste:
myList =["Rock","Paper","Scissors"]
z = random.choice(myList)

print(z)


# Shuffle-Modus aus einer Liste:
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(cards)