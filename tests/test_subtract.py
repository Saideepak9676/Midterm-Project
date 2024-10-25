import pytest
from app.commands.subtract import Subtract

def test_subtract_command():
    command = Subtract()
    result = command.execute(5, 3)
    assert result == 2
