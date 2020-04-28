def raise1():
    raise IndexError


def noraise():
    return


def raise2():
    raise SyntaxError

for func in (raise1, noraise, raise2):
    print('\n', func, sep=' ')
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
    finally:
        print('finally run')
