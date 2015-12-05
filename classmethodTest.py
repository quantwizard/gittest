class Color(object):
    _color = (0, 0, 0)

    @classmethod
    def value(cls):
        # here cls is child class not Parent.
        if cls.__name__ == 'Red':
            cls._color = (255, 0, 0)

        elif cls.__name__ == 'Green':
            cls._color = (0, 255, 0)

        return cls._color


class Red(Color):
    pass


class Green(Color):
    pass


class UnknownColor(Color):
    pass


def main():
    red = Red()
    green = Green()
    xcolor = UnknownColor()
    print 'red = ', red.value()
    print 'green = ', green.value()
    print 'xcolor =', xcolor.value()


if __name__ == '__main__':
    main()