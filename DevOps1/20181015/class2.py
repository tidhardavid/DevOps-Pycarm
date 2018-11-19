myName = 'Tidhar'

class A:
    def abc(self):
        print(123)

    def x(self):
        return 4

    def y(self, e):
        print(e)

    def z(self, d):
        return 'hi ' + d


if __name__ == '__main__':
    A().abc()
    print(A().x())

    A().y('tidhar')
    A().y('')

    A().y(A().z('tidhar'))

    A().y(A().z(myName + ' !!!'))

    x = input('please enter a number')
    print(x)