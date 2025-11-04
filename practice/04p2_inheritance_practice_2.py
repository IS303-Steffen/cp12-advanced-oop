from helper_functions import clear_screen
clear_screen()

# ====================
# INHERITANCE PRACTICE
# ====================

# Step 1: Define Parent Class `Vehicle`
# - Initialize make, model, and year attributes in `__init__`.
# - Implement `start` and `stop` methods that return messages.
#       - "<make> <model> (<year>) has started."
#       - "<make> <model> (<year>) has stopped."


# Step 2: Create Child Classes
# - `Car`: inherits `Vehicle` without adding new attributes or methods.
# - `Truck`: inherits `Vehicle`, adds `cargo_capacity` attribute in `__init__`,
#   overrides `start` method to include cargo capacity in the message.
# - `Motorcycle`: inherits `Vehicle`, adds `rev_engine` method.
#       - "<make> <model> (<year>) engine is revving loudly!"



# Step 3: Test Vehicle Hierarchy
# - Instantiate `Car`, `Truck`, and `Motorcycle` with appropriate attributes.
# - Call `start`, `stop`, and `rev_engine` (where applicable) on each instance.
# - Print the make, model, and year of each vehicle.

