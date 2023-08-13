from menu import Menu


class LengthConversion:

    def meters_to_feet(self,meters):
        return meters*3.28084
    
    def feet_to_meters(self,feet):
        return feet*0.3048
    
    def inches_to_centimeters(self,inches):
        return inches*2.54
    
    def centimeters_to_inches(self,centimeters):
        return centimeters*0.393701
    
    def kilometers_to_meters(self,kilometers):
        return kilometers*1000
    
    def meters_to_kilometers(self,meters):
        return meters/1000
    
    def get_input(self,prompt):
        user_input=input(prompt)
        return user_input
    
    def handle_length_conversion(self):
        menu=Menu()

        conversion_options=[
            "1) Meters to Feet",
            "2) Feet to Meters",
            "3) Inches to Centimeters",
            "4) Centimeters to Inches",
            "5) Kilometers to Meters",
            "6) Meters to Kilometers",
            "7) Please drop a method for other conversion",
        ]

        choice=menu.get_user_choice("Length Conversion Options: ",conversion_options)

        if choice in range(1,7):
            input_message=f"Enter the length in {conversion_options[choice-1].split()[0].lower()}: "
            value=float(self.get_input(input_message))
            conversion_method=getattr(self,conversion_options[choice-1].replace(" ","_").lower())
            converted_value=conversion_method(value)
            print(f"{value}{conversion_options[choice-1].split()[0].lower()}={converted_value}{conversion_options[choice-1].split()[-1].lower()}")

        elif choice=="7":
            suggestion=self.get_input("Enter your suggestion: ")
            print(f"Thank You for your suggestion: {suggestion}")
        else: 
            print("Invalid Input!")




