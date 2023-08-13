class Menu:
    def __init__(self):
        self.choices=[]

    def add_choice(self,choice):
        self.choices.append(choice)

    def display_menu(self):
        print("Option: ")
        for index,choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def get_user_choice(self):
        self.display_menu()
        choice=input("Enter your option: ")
        return choice