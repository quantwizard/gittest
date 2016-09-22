class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print "%s, %s, %s, %s" % (meta, name, bases, class_dict)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object):
    __metaclass__ = Meta
    stuff = 123

    def foo(self):
        pass


my = MyClass()
