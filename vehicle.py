class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"This vehicle is {self.color}."


if __name__ == "__main__":
    Vehicle1 = Vehicle("Yellow")
    print(Vehicle1.getColor())

    print(Vehicle1.toString())