from calculator import Calculator

#function for doing the normal operation inside the calc.
# def perform_arithmetic_operation(calc,operation):
#     num1,num2=calc.get_user_input()
#     result=operation(num1,num2)
#     print("Result:",result)
#     return result

def main(): 
    calc=Calculator()
    
    #making out the choices: 
    while True: 
        print("Options: ")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Set Memory")
        print("6. Recall Memory")
        print("7. Clear Memory")
        print("8. View History")
        print("9. Clear History")
        print("10. Quit")

        choice=input("Enter the option: ")

        if choice in ['1','2','3','4']:
            operation_symbol={'1':'+','2':'-','3':'*','4':'/'}[choice]
            num1,num2=calc.get_user_input()
            result=calc.perform_arithmatic_operation(num1,num2,operation_symbol)
            print("Result:",result)
            

        elif choice=="5":
            value=int(input("Enter value to set in memory:"))
            calc.set_memory(value)
            print("Value set in memory")

        elif choice=="6":
            memory=calc.recall_memory()
            print("Memory:",memory) if memory is None else print("Memory is empty")
        
        elif choice=='7':
            calc.clear_history()
            print("Memory cleared!")
        
        elif choice=='8':
            history=calc.get_history()
            if not history: print('No history available')
            else: 
                print("calulation history: ")
                for entry in history: 
                    print(entry)
        
        elif choice=='9':
            calc.clear_memory()
            print("History is cleared")
        

        elif choice=="10":                
            print("Thank You for choosing out Calculator, Happy Calculating!")
            break
        else: 
            print("Invalid Input!")

if __name__=="__main__":
    main()