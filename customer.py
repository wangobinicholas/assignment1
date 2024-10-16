class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def toString(self):
        return f"Customer Name: {self.name}, Address: {self.address}"


if __name__ == "__main__":
    customer = Customer("Yokana Kafumisi", "Bugujju")
    print(customer.toString())