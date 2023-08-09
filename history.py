
from calculator import Calculator

class History(Calculator):
    def __init__(self):
        super().__init__()
        self.history=[]
        

    def store_history(self,calculation):
        return self.history.append(calculation)
    
    def view_history(self):
        print("History: ")
        for calculation in self.history:
            print(calculation)

    def clear_history(self):
        self.history=[]


    def handle_history(self):
        options=[ "["
        "History Options:     ",
        "1. View History "
        "2. Clear History "  "]"
        ]
        for option in options:
            print(option)

        history_choice=input("Enter history choice: ")
        if history_choice=='1':
            view=self.view_history()
            print(view)
        
        elif history_choice=='2':
            clear=self.clear_history()
            print("There's no history now: ",clear)
        
        
    

    # def handle_memory(self):
    #     print("Memory and History Options: ")
    #     print("1. Set Memory")
    #     print("2. View Memory")
    #     print("3. Clear Memory")
    #     print("4. Clear History")
    #     print("5. View History")

    #     history_choice=input("Enter history/memory choice: ")

    #     if history_choice=='1':
    #         value=int(input("Enter the value to set in memory: "))
    #         self.get_memory(value)

    #     elif history_choice=='2':
    #         memory_value= self.view_memory()
    #         print("Memory value: ",memory_value)
        
    #     elif 
        
        
