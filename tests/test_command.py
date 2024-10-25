import unittest
from app.commands.command import Command

class TestCommand(Command):
    def execute(self, *args):
        return "Executed"

class TestCommandUnit(unittest.TestCase):
    def setUp(self):
        """Set up a TestCommand instance for testing."""
        self.command = TestCommand()

    def test_command_execute_no_args(self):
        """Test execute with no arguments."""
        result = self.command.execute()
        self.assertEqual(result, "Executed")

    def test_command_execute_with_args(self):
        """Test execute with arguments."""
        result = self.command.execute(1, 2, 3)
        self.assertEqual(result, "Executed")  

if __name__ == "__main__":
    unittest.main()
