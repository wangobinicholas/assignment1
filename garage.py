from car import Car
from truck import Truck

class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def setVehicle(self, parked):
        self.parked_vehicle = parked

    def toString(self):
        # I used an if statement to check if there is any vehicle that has been parked in the  garage
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle.toString()}"
        return "No vehicle parked in the garage."

