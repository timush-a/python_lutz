"""
Выполняет обход дерева наследования, используяю ссылки
на пространства имён и отображает суперклассы
"""


def classtree(cls, indent):
    print('.' * indent + cls.__name__)  # Print class name
    for supercls in cls.__bases__:      # Recursive traversal of superclasses
        classtree(supercls, indent + 3)


def intancetree(inst):
    print('Tree of', inst)  # Print object
    classtree(inst.__class__, 3)


def selftest():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass

    intancetree(B())
    intancetree(F())


if __name__ == '__main__':
    selftest()
