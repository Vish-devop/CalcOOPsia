from calculator import Calculator

def main(): 
    calc=Calculator()
    
    #making out the choices: 
    while True: 
        print("Options: ")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice=input("Enter the option (1 or 2): ")

        if choice == "1":
            num1,num2=calc.get_user_input()
            result= calc.addition(num1,num2)
            print("Result: ",result)
        
        elif choice == "2":
            num1,num2=calc.get_user_input()
            result=calc.substraction(num1,num2)
            print("Result of the computation: ",result)

        elif choice == "3":
            num1,num2=calc.get_user_input()
            result= calc.multiplication(num1,num2)
            print("Result: ",result)
        
        elif choice == "4":
            num1,num2=calc.get_user_input()
            result=calc.division(num1,num2)
            print("Result of the computation: ",result)

        elif choice=="5":
            print("Thank You for choosing out Calculator, Happy Calculating!")
            break
        else: 
            print("Invalid Input!")

if __name__=="__main__":
    main()