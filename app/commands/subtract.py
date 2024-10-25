# app/commands/subtract.py
from app.commands.command import Command

class Subtract(Command):
    def execute(self, a, b):
        return a - b
