class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mercedes", 2024, "Black",False)
car2 = Car("BMW", 2026, "White",True)
car3 = Car("Charger", 2025, "Yellow",True)

car3.describe()
