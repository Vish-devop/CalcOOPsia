class History:
    def __init__(self) -> None:
        self.history=[]

    def add_entry(self,entry):
        self.history.append(entry)  #appending the number into the list (history).

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history=[]