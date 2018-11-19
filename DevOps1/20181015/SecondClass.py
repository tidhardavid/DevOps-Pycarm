#Second class
#A
print('#A.')

x = input('please enter x:')
y = input('please enter y:')

def bigOrSmall(x,y):
    if(x > y):
        print('Big')
    elif(x < y):
        print('Small')


bigOrSmall(x, y)


#B
print('\n#B.')

for x in range(5):
    print(x)


#C
print('\n#C.')

a = int(input('Please enter a number between 1 and 4:'))
switcher = {
    1: 'summer',
    2: 'winter',
    3: 'fall',
    4: 'spring'
}
print (switcher.get(a, 'Number is not in range!'))


#D
print('\n#D.')

#the loop will run 10 times, the las number that will be printed will be 10, that we increment but the condition for the while loop will be false.
count = 1
while count < 11:
    print(count)
    count += 1


#E
print('\n#E.')

data = {
    'age': 37,
    'firstletterofsure': 'B',
    'dollarNis': 3.65331502,
    'didIflew': True,
    'appNum': 12
}

for d in data:
    print(data[d])

print('\nage + dollar/nis: ', data['age'] + data['dollarNis'])


#F
print('\n#F.')

phone = input('Please enter your phone number:')
print('phone number: ', phone)

#G
print('\n#G.')

def printHello():
    print('Hello')

printHello()

def calculate():
    print(5 + 3.2)

calculate()


#H
print('\n#H.')

def name(name):
    print('Youre Name:', name)

name(input('Please type your name:'))


def divideby2(num):
    print(num/2)

divideby2(int(input('please enter a number:')))


#I
print('\n#I.')

def sum(a, b):
    return (a + b)

print(sum(5,4))

def add2str(a, b):
    return (a + ' '+ b)

print(add2str('hello', 'world'))


#Challanges
print('\n#Challanges')

#K
print('\n#K.')

def createPyramide(num):
    for x in range(num):
        str = ''
        for y in range(x +1):
            str += '#'
        print(str)

createPyramide(5)
#createPyramide(int(input('Enter the requested height:')))


#L
print('\n#L.')

def createX(num):
    for x in range(num):
        str = ''
        for y in range(num):
            if(x == y) | (y == (num -1 - x)):
                str += '#'
            else:
                str += ' '
        print(str)


createX(7)
#createX(int(input('Enter the requested height:')))


#M
print('\n#M.')

def getNum():
    return input('Please enter a number:').strip()

#print(getNum())

def calculateSumOfdigits():
    num = str(getNum())
    sum = 0
    for x in range(len(num)):
        sum += int(num[x])
    return sum

print('sum of digits:', calculateSumOfdigits())