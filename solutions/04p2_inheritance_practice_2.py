import os
import platform

def clear_screen():
    """
    Clears the terminal screen to improve readability.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ====================
# INHERITANCE PRACTICE
# ====================

# Step 1: Define Parent Class `Vehicle`
# - Initialize make, model, and year attributes in `__init__`.
# - Implement `start` and `stop` methods that return messages.
#       - "<make> <model> (<year>) has started."
#       - "<make> <model> (<year>) has stopped."

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} ({self.year}) has started."

    def stop(self):
        return f"{self.make} {self.model} ({self.year}) has stopped."

# Step 2: Create Child Classes
# - `Car`: inherits `Vehicle` without adding new attributes or methods.
# - `Truck`: inherits `Vehicle`, adds `cargo_capacity` attribute in `__init__`,
#   overrides `start` method to include cargo capacity in the message.
# - `Motorcycle`: inherits `Vehicle`, adds `rev_engine` method.
#       - "<make> <model> (<year>) engine is revving loudly!"

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def start(self):
        base_message = super().start()
        return f"{base_message} Cargo capacity: {self.cargo_capacity}kg."

class Motorcycle(Vehicle):
    def rev_engine(self):
        return f"{self.make} {self.model} ({self.year}) engine is revving loudly!"

# Step 3: Test Vehicle Hierarchy
# - Instantiate `Car`, `Truck`, and `Motorcycle` with appropriate attributes.
# - Call `start`, `stop`, and `rev_engine` (where applicable) on each instance.
# - Print the make, model, and year of each vehicle.

car = Car("Toyota", "Corolla", 2020)
truck = Truck("Ford", "F-150", 2019, 1000)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021)

print(car.start())
print(car.stop())

print(truck.start())
print(truck.stop())

print(motorcycle.start())
print(motorcycle.rev_engine())
print(motorcycle.stop())