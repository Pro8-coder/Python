'''
Создать метакласс для паттерна Синглтон (см. конец вебинара)
'''
from threading import Lock


class MyMetaClass(type):
    _data = {}
    '''Создаём экземпляр класса 'Lock'.'''
    _Lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._Lock:
            if cls not in cls._data:
                cls._data[cls] = super().__call__(*args, **kwargs)
        return cls._data[cls]


class MySingleton(metaclass=MyMetaClass):
    def __init__(self):
        self.name = "Single"


my_single1 = MySingleton()
my_single2 = MySingleton()
print(my_single1, my_single2)
my_single1.name = "New Single"
print(f'my_single2 содержит {my_single2.__dict__}')
print(id(my_single1) == id(my_single2))
