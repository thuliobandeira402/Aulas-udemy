from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name
        self._name = None

    @property
    @abstractmethod
    def name(self):...

   


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Sou inútil')
    
    @AbstractFoo.name.setter
    def name(self, value):
        self._name = value
        print('Sou inútil também')


foo = Foo('Bar')
print(foo.name)