# app/add.py
from app.commands.command import Command

class Add(Command):
    def execute(self, a, b):
        return a + b
