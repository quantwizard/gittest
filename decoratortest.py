class B():
    def __init__(self):
        self.__prop = 1
    @property
    def prop(self):
        print "call get"
        return self.__prop
    @prop.setter
    def prop(self, value):
        print "call set"
        self.__prop = value
    @prop.deleter
    def prop(self):
        print "call del"
        del self.__prop

def main():
    b = B()
    b.prop = 3
    print b.prop

    
if __name__ == '__main__':
    main()