from calculator import Calculator
from ArithmaticOperations import ArithmaticOperations
from history import History


def main(): 
    calc=Calculator()
    arithmatic_calc=ArithmaticOperations()
    memory_calc=History()
    
    #making out the choices: 
    while True: 
        print("Options: ")
        print("1. Basic Calculator")
        print("2. History")
        print("3. Memory")
        print("4. Unit Conversion")
        print("5. Quit")

        choice=input("Enter the option: ")

        if choice=='1':
            arithmatic_calc.handle_basic_calculator()

        elif choice=='2':
            memory_calc.handle_history()
        
        elif choice=='3':
            print("Feature is in beta version")
        
        elif choice=='4':
            print('feature is in beta version')
        
        elif choice=='5':
            print("Thank You choose OOPSCalc")
            break 
        
        else: print("Invalid Input_Choice")

if __name__=="__main__":
    main()