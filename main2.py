import carly
import Caleb as caleb

def start():
    print(startGame)
    done = False
    while not done:
        character = input("Type the character's name! ").lower()
        if character == "caleb":
            caleb()
            done = True
        elif character == "carly":
            carly()
            done = True
        elif character == "logan":
            logan()
            done = True
        elif character == "susan":
            susan()
            done = True
        elif character == "aiden":
            aiden()
            done = True
        elif character == "exit":
            exit()
        else:
            print("Type character name!")

carly.cIntro()
