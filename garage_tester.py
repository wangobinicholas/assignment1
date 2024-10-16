from truck import Truck
from garage import Garage

class GarageTester:
    @staticmethod
    def getExample():
        truck = Truck(color="black", has_trailer=False)
        garage = Garage()
        garage.setVehicle(truck)
        return garage

if __name__ == "__main__":
    garage = GarageTester.getExample()
    print(garage.toString())
