import pytest
from app.commands.divide import Divide

def test_divide_command():
    command = Divide()
    assert command.execute(10, 2) == 5
    with pytest.raises(ValueError):
        command.execute(10, 0)
