class A(object):
    def f(self):
        print('hello from A')
        super(A, self).f()

    def __init__(self, a, b, *args, **kwargs):
        self.a = 1
        self.b = 2
        super(A, self).__init__(*args, **kwargs)


class B(object):
    def f(self):
        print('hello from B')

    def __init__(self, c, d):
        self.c = c
        self.d = d


class C(A, B):
    pass


x = C(1, 2, 3, 4)
assert x.a is 1
assert x.b is 2
assert x.c is 3
assert x.d is 4
