#Tidhar Ben David
#First class
print('First class:')
#A
print('A.')
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second /first)

#B
a = 9 #last assignment is 9
b = 8 #last assignment is 8
c = 15 #last assignment is a+b, when a was 9 and b was 5

#C
print('\nC.')
#no difference when we declare a string if we use single or double quotes.

my_number = 5+5
print("my result:", my_number)
print("my result: "+str(my_number))

#D
print('\nD.')
x = 5
y = 2.56
print(x + int(y))
#when casting float to int, the number looses its decimal fracture value.

#challange
print('\nchallange:')
a = 8
b = '123'
print(a + int(b))

#first class - extra:
print('\nfirst class - extra:')
#1
print('1.')
print('hello')
print('Tidhar Ben David')

#2
print('\n2.')
print(4 + 6)

#3
print('\n3.')
import sys
import re
#print(sys.version)
print(re.match('[^\s]*', sys.version)[0])

#print(sys.version_info)
print(str(sys.version_info.major) + '.' + str(sys.version_info.minor) + '.' + str(sys.version_info.micro))

import platform
print(platform.python_version())

#4
print('\n4.')
def reverseWord(word):
    reversedWord = ''
    for i in range(len(word) - 1, -1, -1):
        reversedWord += word[i]
    return reversedWord

print(reverseWord('hello'))
print(reverseWord('hello world'))

#5
print('\n5.')
def wordLength(word):
    return len(word)

print(wordLength('hello'))
print(wordLength('hello world'))

#6
print('\n6.')
import datetime

x = datetime.datetime.now()
print(x)

hour = x.hour
periodinDay = ' at '
if (hour >= 6) & (hour < 12):
    periodinDay += 'morning'
elif (hour >= 12) & (hour < 16):
    periodinDay += 'noon'
elif (hour >= 16) & (hour < 19):
    periodinDay += 'afternoon'
elif (hour >= 19) & (hour < 23):
    periodinDay += 'evening'
elif (hour == 23) | (hour < 6):
    periodinDay += 'night'
else:
    periodinDay = ''
print('Now is ' + x.strftime('%I') + ':' + x.strftime('%M') + periodinDay)

#7
print('\n7.')
def max(x, y):
    if x == y:
        res = 'both are equal :-)'
    else:
        if x > y:
            res = x
        else:
            res = y
        res = str(res) + ' is Bigger!'
    return res

print(max(5,6))
print(max(5,5))
print(max(5,2))



#8
print('\n8.')

if (120 < 200) & (120 > 5):
    print('Match')





