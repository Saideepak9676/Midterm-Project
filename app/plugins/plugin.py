from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def run(self):
        pass

class GreetPlugin(Plugin):
    def run(self):
        print("Hello, welcome to the Advanced Python Calculator!")
