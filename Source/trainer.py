import platform
import os

the_system = platform.system()
if (the_system == "Windows"):
    os.system("cls")
else:
    os.system("clear")

def ask_vocabulary(question, answer):
    input_from_trainee = input(question)

    if input_from_trainee == answer:
        print ("yoo !!! yooo!!!")
    else:
        print ("Sorry, but the answer is wrong! Ask Tristan, he knows!")

ask_vocabulary("What is Fish in shona?", "Hove")
ask_vocabulary("What is Salad in shona?", "Muriwo")
ask_vocabulary("What is black in shona?", "tema")
ask_vocabulary("What is human in shona?", "munhu")
ask_vocabulary("What is Water in shona?", "Mvura")
