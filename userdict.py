class UserDict:
    def __init__(self, dict=None):
        self.data={}
        if dict is not None: self.data.update(dict)
    def items(self): return self.data.items()
    def clear(self): return self.data.clear()

if __name__ == "__main__":
    ud = UserDict({"1":"one", "2":"two"})
    print ud.data

    print "call items"
    print ud.items()

    print "call clear, then items()"
    print ud.clear()
    print ud.items()

    if hasattr(ud, "clear"):
        print "there is attribute clear"
    else:
        print "there is no clear"
    

    if isinstance(ud, UserDict): print "yes"

    print ud.__class__
