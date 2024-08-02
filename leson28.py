class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind


    def __str__(self):
        return f'Transport {self.kind} mark {self.brand} max speed {self.max_speed} km/h'



class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue, kind='Car'):
        super().__init__(brand, max_speed, kind)
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Gasoline left for {self.__gasoline_residue}'


    @gasoline.setter
    def gasoline(self, new_gasoline):
        if isinstance(new_gasoline, int):
            self.__gasoline_residue += new_gasoline
        else:
            print(f'Error zaprawka')



class Boat(Transport):
    def __init__(self, brand, max_speed, owner_name, kind='Boat'):
        super().__init__(brand, max_speed, kind)
        self.owner_name = owner_name

    def __str__(self):
        return f'The owner this boat is {self.owner_name}'



class Plane(Transport):
    def __init__(self, brand, max_speed, capacity, kind='Plane'):
        super().__init__(brand, max_speed, kind)
        self.capacity = capacity

    def __str__(self):
        return f'The plane mark {self.brand} Accommodates {self.capacity} people'




transport = Transport('Telega', 10)
print(transport)
bike = Transport('shkolnik', 20, "bike")

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)
first_car = Car('BMW', 230, 75000, 300)
print(first_car)
print(first_car.gasoline)
first_car.gasoline = 20
print(first_car.gasoline)
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)
