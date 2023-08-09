from calculator import Calculator
from history import History

class ArithmaticOperations(Calculator):
    def addition(self,num1,num2):
        return num1+num2
    
    def substraction(self,num1,num2):
        return num1-num2
    
    def multiplication(self,num1,num2):
        return num1*num2

    def division(self,num1,num2):
        if num2==0: 
            print( "Cannot divide by 0")
        return num1//num2
        

         #it's just a instance of the class : History()
    def handle_basic_calculator(self): 
        print("Welcome to Basic Calculator!")
        history_calc=History()

        operator_mapping={'1':'+','2':'-','3':'*','4':'/'}
        for key,value in operator_mapping.items():
            print(f"{key}.{value}")
        # num1,num2=self.get_user_input()

        operation_choice=input("Enter the operator choice: ")

        if operation_choice in operator_mapping: 
            operator=operator_mapping[operation_choice]
            num1,num2=self.get_user_input()
            result=self.perform_arithmatic_operation(operator,num1,num2)

            calculation=f"{num1}{operator}{num2}={result}"
            history_calc.store_history(calculation)
            print("Result: ",result)
        else: 
            print("Invalid Operator")
        
       