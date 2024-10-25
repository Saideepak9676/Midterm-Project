import os
import pytest
import warnings
from unittest.mock import patch, MagicMock
from app.repl import repl
from app.commands.history import add_to_history, save_history, load_history, clear_history
from app.plugin_manager import PluginManager
import logging
import logging.config
import configparser


os.makedirs('logs', exist_ok=True)


log_config_path = os.path.abspath("logging.conf")


try:
    
    if os.path.exists(log_config_path):
        logging.config.fileConfig(log_config_path)
    else:
        raise FileNotFoundError(f"Logging configuration file not found at {log_config_path}")
except Exception as e:
    
    print(f"Error loading logging configuration: {e}. Falling back to basicConfig.")
    logging.basicConfig(
        filename='logs/app.log',
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

logger = logging.getLogger(__name__)

@pytest.fixture
def mock_commands():
    """Create mock command objects."""
    return (
        MagicMock(name="Add"),
        MagicMock(name="Subtract"),
        MagicMock(name="Multiply"),
        MagicMock(name="Divide")
    )

def test_repl_eof_error(mock_commands):
    """Test handling of EOFError in REPL."""
    with patch("builtins.input", side_effect=EOFError):
        repl()

def test_repl_greet_command(mock_commands):
    """Test greeting command in REPL."""
    with patch("builtins.input", side_effect=["greet", "exit"]):
        with patch("builtins.print") as mock_print:
            with patch("app.plugin_manager.PluginManager.run_plugins") as mock_run_plugins:
                repl()
                mock_run_plugins.assert_called_once()

def test_repl_load_history_command(mock_commands):
    """Test loading history command in REPL."""
    with patch("builtins.input", side_effect=["load history", "exit"]):
        with patch("app.repl.load_history") as mock_load_history:
            repl()
            assert mock_load_history.call_count == 1
            print(f"load_history called: {mock_load_history.call_count} times")
            print(f"Calls: {mock_load_history.call_args_list}")

def test_repl_clear_history_command(mock_commands):
    """Test clearing history command in REPL."""
    with patch("builtins.input", side_effect=["clear history", "exit"]):
        with patch("app.repl.clear_history") as mock_clear_history:
            repl()
            mock_clear_history.assert_called_once()
            print(f"clear_history called: {mock_clear_history.call_count} times")

def test_repl_valid_operations(mock_commands):
    """Test valid operations in REPL."""
    add_command, subtract_command, multiply_command, divide_command = mock_commands

    add_command.return_value.execute.return_value = 8
    subtract_command.return_value.execute.return_value = 2
    multiply_command.return_value.execute.return_value = 15
    divide_command.return_value.execute.return_value = 1.666

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        with patch("builtins.input", side_effect=[
            "add 5 3",
            "subtract 5 3",
            "multiply 5 3",
            "divide 5 3",
            "exit"
        ]):
            with patch("builtins.print") as mock_print:
                repl()

def test_repl_invalid_command(mock_commands):
    """Test handling of an unknown command in REPL."""
    with patch("builtins.input", side_effect=["unknown 5 3", "exit"]):
        with patch("builtins.print") as mock_print:
            repl()
            mock_print.assert_any_call("Unknown command. Please use 'add', 'subtract', 'multiply', or 'divide'.")

def test_repl_invalid_input_format(mock_commands):
    """Test handling of invalid input format in REPL."""
    with patch("builtins.input", side_effect=["add 5", "exit"]):
        with patch("builtins.print") as mock_print:
            repl()
            mock_print.assert_any_call("Invalid input format. Use: <command> <a> <b>")
