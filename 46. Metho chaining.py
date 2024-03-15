# method chaining =  Aufrufen mehrerer Methoden nacheinander
#                    Jeder Aufruf führt eine Aktion für dasselbe Objekt aus und gibt selbst zurück

class Car:

    def turn_on(self):
        print("You start the engine")

    def drive(self):
        print("Yout drive the car")

    def brake(self):
        print("You step on the brakes")

    def turn_off(self):
        print("You turn off the engine")
