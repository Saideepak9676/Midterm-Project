from app.commands.add import Add
from app.commands.subtract import Subtract
from app.commands.multiply import Multiply
from app.commands.divide import Divide

def main():
   
    add_command = Add()
    subtract_command = Subtract()
    multiply_command = Multiply()
    divide_command = Divide()
    
   
    print("Addition: ", add_command.execute(5, 3))           
    print("Subtraction: ", subtract_command.execute(5, 3))     
    print("Multiplication: ", multiply_command.execute(5, 3))  
    print("Division: ", divide_command.execute(5, 3))          
    
    
    try:
        print("Division by zero: ", divide_command.execute(5, 0))
    except ValueError as e:
        print(e)  

if __name__ == "__main__":  
    main()
