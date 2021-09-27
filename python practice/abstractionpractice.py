from abc import ABC , abstractmethod
class WorldBank(ABC):
    @abstractmethod
    def save(self,x):
        pass
    @abstractmethod
    def loan(self,x):
        pass
class icici(WorldBank):
    def save(self,x):
        print('I am saving from icici')

    def loan(self,x):
        print('i am loan from icici ')
class SBI(WorldBank):
    def save(self, x):
        print('I am saving from SBI')

    def loan(self, x):
        print('i am loan from SBI ')

class Axis(WorldBank):
    def save(self, x):
        print('I am saving from Axis')

    def loan(self, x):
        print('i am loan from Axis ')
# s = Axis()
# s.loan('x')
s=SBI()
s.print(SBI)

