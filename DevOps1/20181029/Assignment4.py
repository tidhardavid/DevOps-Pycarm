import PIL
from PIL import Image

#Tidhar Ben David
#Class 3 - Extra
print('Class 3 - Extra:')


#1 #2
def main1():
    print('1.')
    try:
        a = 1/0
    except ZeroDivisionError:
        a = 'Zero division error!!!'
    finally:
        print(a)


#3 - A try without except is useless, but is legal.

#4 - All kinds of errors.

#5 - we won't be able to identify what was the error type was.

#6 -
# IOError -I/O operation fails,  (such as a print() statement, the built-in open() function or a method of a file object)
# ZeroDivisionError - ArithmeticError

#7,8,9,10 -
def main7():
    try:
        print('\n7.')
        My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/words.txt', 'w', encoding='utf-8')
        My_file.close()

        print('\n8.')
        My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/words.txt', 'w', encoding='utf-8')
        My_file.write('Tidhar')
        My_file.close()

        print('\n9.')
        My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/words.txt', 'r', encoding='utf-8')
        print(My_file.read())
        My_file.close()

        print('\n10.')
        My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/words.txt', 'a', encoding='utf-8')
        My_file.write('\nתדהר')
        My_file.close()

        My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/words.txt', 'r', encoding='utf-8')
        print(My_file.read())
        My_file.close()

    except IOError:
        print('IOError')


#challange - 11


def main11():
    print('\nchallange 11.')
    size = (128, 128)
    color = (128, 128, 128)
    # color = ('#345544')
    My_image = PIL.Image.new('RGB', size, color)
    My_image.save('pic.png', 'PNG')
    print(My_image.format, My_image.size, My_image.mode)
    My_image.show()


if __name__ == '__main__':
    main1()
    main7()
    main11()