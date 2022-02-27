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

ask_vocabulary("What is red in shona?", "tsvuku")

input_from_trainee = input("What is white in shona?")

if input_from_trainee == "jena":
    print ("yoo !!! yooo!!!")
else:
    print ("Sorry, but the answer is wrong! Ask Tristan, he knows!")

input_from_trainee = input("What is black in shona?")

if input_from_trainee == "tema":
    print ("yoo !!! yooo!!!")
else:
    print ("Sorry, but the answer is wrong! Ask Tristan, he knows!")

input_from_trainee = input("What is human in shona?")

if input_from_trainee == "munhu":
    print ("yoo !!! yooo!!!")
else:
    print ("Sorry, but the answer is wrong! Ask Tristan, he knows!")
