import re

class User:
    def __init__(self, email, ac_type):
        self.email = email 
        self.ac_type = ac_type

class Traveler(User): 
    def __init__(self, email, first_name, last_name, age):
        super().__init__(email, "Traveler")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

class Business(User):
    def __init__(self, email, business_name, business_type):
        super().__init__(email, "Business")
        self.business_name = business_name
        self.business_type = business_type

def check_account():
    email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    user_mail = input("Please enter your user email: ")

    if email_pattern.match(user_mail):
        ac_type = input("Please choose account-type (Traveler or Business): ")
        if ac_type == "Traveler":
            first = input("First name: ")
            last = input("Last name: ")
            age = input("Age: ")
            user = Traveler(user_mail, first, last, age)

        elif ac_type == "Business":
            b_name = input("Business name: ")
            b_type = input("Business type: ")
            user = Business(user_mail, b_name, b_type)

        else:
            print("Invalid account type")
            return

        print(f"Brilliant {user.email}, you've set up a {user.ac_type} account!")

    else:
        print("Invalid email")

check_account()




