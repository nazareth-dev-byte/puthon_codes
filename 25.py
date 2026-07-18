class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f" {self.name} = {self.position}"

#With a static method, you only need to access that class, you don't even need to create any objects from that class
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugine", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")


print(Employee.is_valid_position("Manager"))

#For an instance method, you access an object then call the instance method
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
