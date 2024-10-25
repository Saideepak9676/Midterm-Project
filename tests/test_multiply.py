import pytest
from app.commands.multiply import Multiply

def test_multiply():
    command = Multiply()
    assert command.execute(3, 5) == 15
    assert command.execute(0, 5) == 0
