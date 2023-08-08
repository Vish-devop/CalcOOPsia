


class Calculator():  #history is acting like a sub-class. 
    def __init__ (self):
        self.memory=None
        super().__init__()   # initiliazing history from the base class.  
   

    def get_user_input(self):
        num1=int(input("Enter the first Number: "))
        num2=int(input("Enter the second Number: "))
        return num1,num2

    def perform_arithmatic_operation(self,operator,num1,num2):
        if operator=='+':
                return self.addition(num1,num2)
        elif operator=='-':
                return self.substraction(num1,num2)
        elif operator=='*':
                return self.multiplication(num1,num2)
        elif operator=='/':
                return self.division(num1,num2)
        else: return "Invalid opeator"


        
    def set_memory(self,value):
        self.memory=value
    
    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory=None

    


    

    



    
