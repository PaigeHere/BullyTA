import carly
import Caleb as caleb
import susan
import final project-bullying text adventure.py as logan


def start():
    print(startGame)
    done = False
    while not done:
        character = input("Type the character's name! ").lower()
        if character == "caleb":
            caleb.caleb()
            done = True
        elif character == "carly":
            carly.carly()
            done = True
        elif character == "logan":
            logan.logan()
            done = True
        elif character == "susan":
            susan.susan()
            done = True
        elif character == "aiden":
            aiden.aiden()
            done = True
        elif character == "exit":
            exit()
        else:
            print("Type character name!")
