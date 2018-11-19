class Car:
    def __init__(self, modal, color):
        self.modal = modal
        self.color = color


class ElectricCar(Car):
    def __init__(self, modal, color, battery_type):
        #Car.__init__(self, modal, color)
        super(ElectricCar, self).__init__(modal, color)
        self.battery_type = battery_type


def main():
    regular_volvo = Car('volvo', 'white')
    electric_volvo = ElectricCar('electronic_volvo', 'red', 'lithium')
    if isinstance(regular_volvo, Car):
        print('regular volvo is instance of Car')
    if isinstance(electric_volvo, Car):
        print('electric volvo is instance of Car')

    if type(electric_volvo) is ElectricCar:
        print('electric volvo is type of ElectricCar')
    if type(electric_volvo) is Car:
        print('electric volvo is type of Car')

if __name__ == '__main__':
    main()