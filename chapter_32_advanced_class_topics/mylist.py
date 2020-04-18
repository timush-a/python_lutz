class MyList:
    def __init__(self, start):
        self.wrapped = []
        for a in start:
            self.wrapped.append(a)

    def __add__(self, term):
        return MyList(self.wrapped + term)

    def __mul__(self, multiplier):
        return MyList(self.wrapped * term)

    def __getitem__(self, offset):
        return self.wrapepd[offset]

    def __len__(self):
        return len(self.wrapped)

    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])

    def __append__(self, node):
        MyList(self.wrapped.append(node))

    def __getattr__(self, name):
        return getattr(self.wrapped, name)

    def __repr__(self):
        return repr(self.wrapped)
