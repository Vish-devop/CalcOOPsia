from calculator import Calculator

def main(): 
    calc=Calculator()
    
    #making out the choices: 
    while True: 
        print("Options: ")
        print("1. Addition")
        print("2. Quit")

        choice=input("Enter the option (1 or 2): ")

        if choice == "1":
            num1,num2=calc.get_user_input()
            result= calc.addition(num1,num2)
            print("Result: ",result)

        elif choice=="2":
            print("Calculator is exiting. Goodbye!")
            break
        else: 
            print("Invalid Input!")

if __name__=="__main__":
    main()