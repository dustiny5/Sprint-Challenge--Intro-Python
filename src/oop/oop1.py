# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base/Main Class
class Vehicle:
    pass

# Inherits from Vehicle
class FlightVehicle(Vehicle):
    pass

# Inherits from FlightVehicle which inherits from Vehicle
class Starship(FlightVehicle):
    pass

# Inherits from FlightVehicle which inherits from Vehicle
class Airplane(FlightVehicle):
    pass

# Inherits from Vehicle
class GroundVehicle(Vehicle):
    pass

# Inherits from GroundVehicle which inherits from Vehicle
class Car(GroundVehicle):
    pass

# Inherits from GroundVehicle which inherits from Vehicle
class Motorcycle(GroundVehicle):
    pass