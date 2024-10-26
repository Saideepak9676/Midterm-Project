
# Advanced Python Calculator

## Overview

The Advanced Python Calculator is a Python-based calculator application designed with clean, professional software development practices. Key features include a command pattern for operation handling, a plugin architecture, comprehensive logging, environment variable management, and error handling with "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) principles.

## Features

- **Basic Operations**: Addition, Subtraction, Multiplication, Division.
- **Plugin System**: Extends calculator functionalities with plugins.
- **History Management**: Tracks all calculations, with options to save/load history.
- **Logging**: Configurable logging for debugging and tracking.
- **Error Handling**: Robust exception handling following LBYL and EAFP principles.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/advanced-python-calculator.git
cd advanced-python-calculator
pip install -r requirements.txt
```

---

## Usage

Run the calculator:

```bash
python main.py
```

To use the REPL (Read-Eval-Print-Loop) interface, enter commands for different operations:

- `add 5 3`
- `subtract 10 4`
- `multiply 7 6`
- `divide 8 2`

---

## Design Patterns

The project implements several design patterns to promote clean code architecture:

### 1. Command Pattern

The Command Pattern encapsulates requests as objects, making it easier to add new commands. This is used for each arithmetic operation.

**Implementation**:
- Each operation (Add, Subtract, Multiply, Divide) inherits from a `Command` base class in `app/commands/command.py`.

**Code Example** (in `app/commands/add.py`):

```python
from app.commands.command import Command

class Add(Command):
    def execute(self, a, b):
        return a + b
```

### 2. Plugin Architecture (Facade Pattern)

The plugin system follows a simplified **Facade Pattern**, allowing easy loading and execution of plugins.

**Implementation**:
- The `PluginManager` in `app/plugin_manager.py` manages plugins in a user-friendly way.
- The `GreetPlugin` example plugin is in `plugins/greet/greet_plugins.py`.

**Code Example** (in `app/plugin_manager.py`):

```python
class PluginManager:
    def load_plugins(self):
        # Loads all plugins in the specified directory
        pass
    
    def run_plugins(self):
        # Executes the run method of each loaded plugin
        pass

```

### 3. Singleton Pattern
The Singleton Pattern ensures that a class has only one instance and provides a global access point to that instance. This is used for managing the logging configuration'

'''python
class LogManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LogManager, cls).__new__(cls)
            # Initialization code here
        return cls._instance
    def setup_logging(self):
        # Setup logging configuration
        ---
        
## Environment Variables

Environment variables are used for configuration and flexibility, such as setting the logging level.

- **.env** file in the root directory stores environment variables.
- `python-dotenv` package loads these variables automatically.

**Example Code** (in `app/main.py`):

```python
from dotenv import load_dotenv
import os

load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
```

---

## Logging

The application uses a robust logging configuration to capture events and errors. Logs help track the application's execution flow and identify issues.

### Logging Configuration

The configuration file `logging.conf` defines two handlers:
- **File Handler**: Logs are stored in `logs/app.log` with rotation to prevent file growth.
- **Console Handler**: Outputs logs to the console for immediate feedback.

**Example Configuration** (in `logging.conf`):

```ini
[loggers]
keys=root

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=fileHandler,consoleHandler

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=INFO
formatter=simpleFormatter
args=('logs/app.log', 'a', 1048576, 5)
```

### Using Logging in Code

Each main module in the app logs critical events, which helps with debugging and tracking.

**Example Code** (in `app/repl.py`):

```python
import logging

logger = logging.getLogger(__name__)

def run():
    logger.info("Starting the REPL for calculator")
    # Additional logic for REPL
```

---

## Error Handling (LBYL and EAFP)

The application uses both LBYL and EAFP principles for error handling.

### LBYL (Look Before You Leap)

**Example Code** (in `app/commands/divide.py`):

```python
class Divide(Command):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
```

### EAFP (Easier to Ask for Forgiveness than Permission)

**Example Code** (in `app/repl.py`):

```python
try:
    result = command.execute(a, b)
except ValueError as e:
    print(f"Error occurred: {e}")
```

---

## Video Demonstration

[Video](https://www.youtube.com/watch?v=hMFgHw2E1c8)
It showcases the calculator's features, including basic operations, plugins, error handling, and logging.

---

## Continuous Integration

The project uses **GitHub Actions** for continuous integration. The `.github/workflows/python-app.yml` file configures automated testing, linting, and type-checking. All commits to the main branch are verified to ensure code quality and functionality.

**Example Workflow Configuration**:

```yaml
name: Python Application

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest --cov
