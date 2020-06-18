from abc import ABC,abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Programmer:
    def code(self,com):
        print("Develop")
        com.process()

class Laptop(Computer):
    def process(self):
        print("Its running")

# com = Computer()
com = Laptop()
prog = Programmer()
prog.code(com)

