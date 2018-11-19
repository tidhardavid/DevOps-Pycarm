#Tidhar Ben David
#Class 3 - Extra
print('Class 3 - Extra:')

#1
class Car:
    def __init__(self,manufacturer = None):
        self.manufacturer = manufacturer

def main1():
    print('1.')
    for i in range(10):
        print(i+1)
    volvo = Car('Volvo')
    print(volvo.manufacturer)


#2 - No, the purpose of class is to be a template for many objects, as many as we need.


#3 - Yes


#4 - Yes


#5 - to be the main function where we run the code.


#6
def main6():
    list = []
    for i in range(5):
        list.insert(i, Car(str(i)))
        print(list[i].manufacturer)



if __name__ == '__main__':
    main1()
    main6()