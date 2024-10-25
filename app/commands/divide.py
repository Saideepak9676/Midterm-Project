# app/commands/divide.py
from app.commands.command import Command

class Divide(Command):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
