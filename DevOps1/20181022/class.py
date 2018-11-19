class Shark:
    name = 'shark'
    def swim(self):
        print('The Shark is swimming')

    def eat(self):
        print('the shark is eating')

class Shark2:
    @staticmethod
    def swim():
        print(132)


def main():
    sammy = Shark()
    print(sammy.name)
    sammy.name = 'sammy'
    sammy.swim()
    sammy.eat()
    print(sammy.name)
    if isinstance(sammy, Shark):
        print('yes')


if __name__ == '__main__':
    main()
    Shark2.swim()
    import