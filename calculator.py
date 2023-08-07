from history import History

class Calculator(History):  #history is acting like a sub-class. 
    def __init__ (self):
        super().__init__()   # initiliazing history from the base class.  
   

    def get_user_input(self):
        num1=int(input("Enter the first Number: "))
        num2=int(input("Enter the second Number: "))
        return num1,num2

    def perform_arithmatic_operation(self,num1,num2,operator):
        if operator=='+':
                result=num1+num2
                operation_str=f"{num1}+{num2}"
        elif operator=='-':
                result=num1-num2
                operation_str=f"{num1}-{num2}"
        elif operator=='*':
                result=num1*num2
                operation_str=f"{num1}*{num2}"
        elif operator=='/':
                if num2==0: return "Cannot divide by 0"
                result=num1//num2
                operation_str=f"{num1}/{num2}"
        else: return "Invalid opeator"

        entry=f"{operation_str}={result}"
        self.add_entry(entry)
        return result

        
    def set_memory(self,value):
        self.memory=value
    
    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory=None

    


    

    



    
