from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires

    def toString(self):
        winter_tires_status = f"has winter tires: {self.has_winter_tires}"
        return super().toString() + "\n" + winter_tires_status



if __name__ == "__main__":
    car = Car("Yellow", True)
    print(car.toString())
