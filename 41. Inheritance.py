# Inherutance = Möglichkeit, Attribute und Methoden von einer Elternklasse zu erben und in einer abgeleiteten Klasse wiederzuverwenden


class Animal:               # Eltern-Klasse

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):       # Kinder-Klasse. Alles was in der Eltern-Klasse ist, wird automatisch übernommen

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):

        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()