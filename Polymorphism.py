# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves...")

# Child classes with different move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")


vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()
