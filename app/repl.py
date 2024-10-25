import sys
import os
import logging
import logging.config
import configparser
from app.commands.add import Add
from app.commands.subtract import Subtract
from app.commands.multiply import Multiply
from app.commands.divide import Divide
from app.plugin_manager import PluginManager
from app.commands.history import add_to_history, save_history, load_history, clear_history


config = configparser.ConfigParser()
config.read("logging.conf")
logging.config.fileConfig(config)

logger = logging.getLogger(__name__)

def repl():
    """Run the REPL for the Advanced Python Calculator."""
    logger.info("Advanced Python Calculator started. Type 'exit' to quit.")
    print("Advanced Python Calculator. Type 'exit' to quit.")

    
    add_command = Add()
    subtract_command = Subtract()
    multiply_command = Multiply()
    divide_command = Divide()
    
    plugin_manager = PluginManager("app/plugins/greet")
    plugin_manager.load_plugins()

    while True:
        try:
            user_input = input(">> ")
        except EOFError:
            break

        command = user_input.strip().lower()

        if command == "exit":
            save_history()
            logger.info("Calculator exited.")
            break

        elif command == "greet":
            logger.debug("Greet command detected.")
            plugin_manager.run_plugins()
            continue

        elif command == "load history":
            logger.debug("Load history command detected.")
            load_history()
            print("History loaded.")
            continue

        elif command == "clear history":
            logger.debug("Clear history command detected.")
            clear_history()
            print("History cleared.")
            continue

        parts = user_input.split()

        if len(parts) == 3:
            command = parts[0].strip().lower()
            try:
                a, b = float(parts[1]), float(parts[2])
                
                
                if command == "add":
                    result = add_command.execute(a, b)
                    add_to_history("add", a, b, result)
                    logger.debug(f"Performed addition: {a} + {b} = {result}")
                elif command == "subtract":
                    result = subtract_command.execute(a, b)
                    add_to_history("subtract", a, b, result)
                    logger.debug(f"Performed subtraction: {a} - {b} = {result}")
                elif command == "multiply":
                    result = multiply_command.execute(a, b)
                    add_to_history("multiply", a, b, result)
                    logger.debug(f"Performed multiplication: {a} * {b} = {result}")
                elif command == "divide":
                    result = divide_command.execute(a, b)
                    add_to_history("divide", a, b, result)
                    logger.debug(f"Performed division: {a} / {b} = {result}")
                else:
                    logger.warning(f"Unknown command: {command}")
                    print("Unknown command. Please use 'add', 'subtract', 'multiply', or 'divide'.")
                    continue

                print(f"Result: {result}")
            except ValueError:
                logger.error("Invalid input: non-numeric value provided.")
                print("Please provide valid numbers.")
            except ZeroDivisionError:
                logger.error("Error: Division by zero attempted.")
                print("Error: Division by zero is not allowed.")
        else:
            logger.warning("Invalid input format.")
            print("Invalid input format. Use: <command> <a> <b>")

if __name__ == "__main__":
    repl()
