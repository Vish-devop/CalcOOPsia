from calculator import Calculator
from ArithmaticOperations import ArithmaticOperations
from history import History
from menu import Menu
# from UnitConversion.UnitConversion import UnitConversion


def main(): 
    calc=Calculator()
    arithmatic_calc=ArithmaticOperations()
    # unit_calc=UnitConversion()
    history_calc=History()
    choices_menu=Menu()
    
    choices_menu.add_choice("1) Basic Calculator")
    choices_menu.add_choice("2) Record History")
    choices_menu.add_choice("3) Unit conversion")
    choices_menu.add_choice("4) Quit")
    
    #making out the choices: 
    while True:
        choice=choices_menu.get_user_choice()
        

        if choice=='1':
            arithmatic_calc.handle_basic_calculator(history_calc)
            

        elif choice=='2':
            
            history_calc.handle_history()
        
        elif choice=='3':
            print("The feature is in Beta Version")
        
        elif choice=='4':
            print("Thank You choose OOPSCalc")
            break 
        
        else: print("Invalid Input_Choice")

if __name__=="__main__":
    main()