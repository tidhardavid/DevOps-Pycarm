#Tidhar Ben David
#Assignment 3
print('Assignment 3:')
#A
class Dog:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age


def mainA():
    print('A.')
    rexi = Dog('rexi', 3)
    print(rexi.name, ' is ', rexi.age, ' years old')


#B the code will print the instance age - 3


#C
class Car:
    @staticmethod
    def start():
        print('engine is running...')


def mainC():
    print('\nC.')
    Car().start()


#D
class Husky(Dog):
    @staticmethod
    def howl():
        print('ahoooooo')

def mainD():
    print('\nD.')
    Husky.howl()


#E
class BlackHusky(Husky):
    @staticmethod
    def return_color():
        print('Black')

def mainE():
    print('\nE.')
    blackhusky = BlackHusky()
    blackhusky.return_color()
    blackhusky.howl()

#F a. it's not a good practice to run code in the __main__ function.
#  b. we should create a function that will run the code:
class Dog2:
    def bark(self):
        print(123)


def mainF():
    print('\nF.')
    Dog2().bark()


#G
import array as arr

def mainG():
    print('\nG.')
    a = arr.array('i', [3, 6, 9])
    for i in range(len(a) - 1, -1, -1):
        print(a[i])

    dogList = [Dog('Johnie', 5), Dog('Flocky', 2), Dog('Nina',3)]
    for i in range(len(dogList)):
        print(dogList[i].name, 'is', dogList[i].age, 'years old')


#Challange H
class Animal:
    def breath(self):
        print('inhale.. exhale..')

class BlackHusky2(Husky, Animal):
    @staticmethod
    def return_color():
        print('Black')

def mainH():
    print('\nChallange H.')
    newhusky = BlackHusky2()
    newhusky.breath()


if __name__ == '__main__':
    mainA()
    mainC()
    mainD()
    mainE()
    mainF()
    mainG()
    mainH()