import weakref, gc

class A(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

a = A(10)
print a

d = weakref.WeakValueDictionary()
d['key'] = a    # normally, this creates a reference to the memory address of a
# but a weakref doesn't create a reference to a :)
