import array as arr

a = arr.array('i', [3,6,8])
b = arr.array('i', [4,8,9])

a.insert(1,7)
print(a)
a.pop(2)
print(a)
print(len(a))
print(type(a))

# for temp_num in a:
#     print(temp_num)

for i in range(len(a) - 1, -1, -1):
    print(a[i])


my_list = [5, 'a', True]
print(my_list)
print(len(my_list))
print(type(my_list))

x_tuple = 1,2,3,4,5
y_tuple = 'a','b','c','d'

print(x_tuple)
print(len(x_tuple))
print(type(x_tuple))


my_dictionary = {'A':1, 'B':2, 'C':3}
print(my_dictionary)
print(len(my_dictionary))
print(type(my_dictionary))

print(my_dictionary.keys())
print(my_dictionary.values())

del(my_dictionary['B'])
print(my_dictionary)
