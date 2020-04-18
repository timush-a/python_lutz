class MyList(list):
    """
    sublcass built-in list type/class
    map 1..N to 0..N-1
    call back to built-in version
    """
    def __getitem__(self, offset):
        print(f'indexing{self} at {offset}')
        return list.__getitem__(self, offset - 1)


if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')  # __init__ inherited from list
    print(x)  # __repr__ inherited from list

