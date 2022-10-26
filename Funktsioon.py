import math


def print_hello():
    print("Hello")

def get_hello():
    return("hello")

def ask_name_and_greet_user():
    name = input("nimi?")
    name = name.capitalize()
    print(f"Hi {name}. Would you like to have a Hamburger")

    if name == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
ask_name_and_greet_user()

def calculate_hypotenuse_length(kaat, kaat2):
   hypo = math.sqrt(kaat ** 2 + kaat2 **2)
   return hypo

def calculate_cathetus_length(cath, hypo):
    cath2 = math.sqrt(int(hypo) ** 2 - int(cath) ** 2)
    return cath2

print(calculate_hypotenuse_length(42, 23)
print(calculate_cathetus_length(22 , 93))
