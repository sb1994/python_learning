class A:
    def func(self):
        return 'A.Func'


class B(A):
    def func(self):
        return 'B.Func'


class C(A):
    def func(self):
        return 'C.Func'


class D(B, C):
    pass

# class.mro() shows the inheritance
