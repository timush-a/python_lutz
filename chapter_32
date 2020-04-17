class tracer:
    def __init__(self, func):
        # remember original, init counter
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        # in later calls: add logic, run original
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    spam('a', 'b', 'c')
