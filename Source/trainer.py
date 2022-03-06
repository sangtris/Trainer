import platform
import os

def clear_screen():
    the_system = platform.system()
    if (the_system == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def case_insensitive_input(question):
    value = input(question)
    value = value.lower()
    return value

def ask_vocabulary(question, answer):
    answer = answer.lower()

    input_from_trainee = case_insensitive_input(question)

    while (input_from_trainee != answer):
        print ("Sorry, but the answer is wrong! Ask Tristan, he knows!")
        input_from_trainee = case_insensitive_input(question)

    print ("yoo !!! yooo!!!")

ask_vocabulary("What is Fish in shona?", "Hove")
ask_vocabulary("What is Salad in shona?", "Muriwo")
ask_vocabulary("What is black in shona?", "tema")
ask_vocabulary("What is human in shona?", "munhu")
ask_vocabulary("What is Water in shona?", "Mvura")
