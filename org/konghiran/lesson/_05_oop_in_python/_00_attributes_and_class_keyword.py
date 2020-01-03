class Dog():
    def __init__(self, name,spots):
        self.name = name
        # True/False
        self.spots = spots
    def print_details(self):
        print(self.name + ' ' + str(self.spots))

my_dog = Dog(name='Jojo',spots=True)

my_dog.print_details()