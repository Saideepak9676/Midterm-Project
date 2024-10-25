import pytest
from app.commands.add import Add  
def test_add_command():
    command = Add()  
    result = command.execute(2, 3) 
    assert result == 5 
