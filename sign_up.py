import re

class User:
    # Define attributes that fit all users
    def __init__(self, email, ac_type):
        self.email = email 
        self.ac_type = ac_type

class Traveler(User):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 



