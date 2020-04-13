class Super:
    def method(self):
        # Поведение по умолчанию
        print('in Super.method')

    def delegate(self):
        # Ожидаемый метод
        self.action()


class Inheritor(Super):
    # Наследует методы без изменений
    pass


class Replacer(Super):
    # Полностью замещает method
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    # Расширяет поведение метода method
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    # Определяет необходимый метод
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for _class in (Inheritor, Replacer, Extender):
        print('\n' + _class.__name__ + '...')
        _class().method()
    print('\nProvider...')
    x = Provider()
    x.delegate
