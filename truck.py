from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def toString(self):
        trailer_status = f"has trailer: {self.has_trailer}"
        return super().toString() + "\n" + trailer_status



if __name__ == "__main__":
    truck = Truck("Yellow", True)
    print(truck.toString())