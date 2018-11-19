# My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/test.txt', 'r')
# content = My_file.read()

# My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/test.txt', 'r+', encoding='utf-8')
# content = My_file.write('text to add\nצבלגדהצך\n')

# My_file = open('C:/Users/Tidhar/PycharmProjects/DevOps1/20181029/test.txt', 'r', encoding='utf-8')
# # My_file.write('vds vdsv vdsvs')
# print(My_file.read())
# My_file.close()

try:
    My_file = open('C:/Users/Tidhar/PycharmProjects/vhj/DevOps1/20181029/test.txt', 'r', encoding='utf-8')
    print(My_file.read())
except IOError:
    print('IOError')
finally:
    print('nvjkdsvn')

