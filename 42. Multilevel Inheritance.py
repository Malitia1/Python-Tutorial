# multi-level inheritance = Möglichkeit, Klassen von einer anderen abgeleiteten Klasse zu erben, wodurch eine Hierarchie von Vererbungsbeziehungen entsteht


class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)            # Erbung aus Organism Class
dog.eat()                   # Erbung aus Animal class
dog.bark()                  # Definiert in Dog Class