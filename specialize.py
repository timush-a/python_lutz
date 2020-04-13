class Super:
    def method(self):
        print('in Super.method')            # Поведение по умолчанию

    def delegate(self):
        self.action()                       # Ожидаемый метод


class Inheritor(Super):                     # Наследует методы без изменений
    pass


class Replacer(Super):                      # Полностью замещает метод
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for _class in (Inheritor, Replacer, Extender):
        print('\n' + _class.__name__ + '...')
        _class().method()
    print('\nProvider...')
    x = Provider()
    x.delegate
