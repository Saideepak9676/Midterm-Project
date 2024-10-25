# app/commands/multiply.py
from app.commands.command import Command

class Multiply(Command):
    def execute(self, a, b):
        return a * b
