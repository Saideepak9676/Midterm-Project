from app.commands.add import Add
from app.commands.subtract import Subtract
from app.commands.multiply import Multiply
from app.commands.divide import Divide

def main():
    # Create command instances
    add_command = Add()
    subtract_command = Subtract()
    multiply_command = Multiply()
    divide_command = Divide()
    
    # Example usage
    print("Addition: ", add_command.execute(5, 3))           # Output: 8
    print("Subtraction: ", subtract_command.execute(5, 3))     # Output: 2
    print("Multiplication: ", multiply_command.execute(5, 3))  # Output: 15
    print("Division: ", divide_command.execute(5, 3))          # Output: 1.666...
    
    # Example of division by zero
    try:
        print("Division by zero: ", divide_command.execute(5, 0))
    except ValueError as e:
        print(e)  # Output: Cannot divide by zero.

if __name__ == "__main__":  # Corrected the conditional statement
    main()
