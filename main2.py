import carly as carly
import Caleb as caleb
import Susan as susan
import Aiden as aiden
import logan as logan

startGame = '''
WELCOME to Stand Up or Stand Down- Presented by TPMLJ.As you sit down to play this game, center yourself, take a deep breath,
and wash away all preconceived ideas you have about bullying.  Take a chance and explore the different characters’ lives
in these different stories. Meet the characters:


Caleb is a 17 year old boy. He spends most of his time doing his homework and going to sports practice. All his close friends are captains with him on the sports team. He’s an only child and lives with his mom and dad. He’s a jock, but still has a soft side.

 Logan is a 17 year old boy from London, England. He just moved to California from his home and he is trying to make some new friends. He loves soccer and graphic design. He is very social and loyal to a fault. He is a funny, friendly guy.

Susan is 38 year old mother. She has an eighteen year old daughter named Rachel. Susan is a working mom and her husband is a stay-at-home dad. Susan has a flexible working schedule, so she is able to pick up Rachel from school when her husband is busy. Susan likes to play tennis on her free time.

Aiden is a quirky 16 year old sophomore in highschool. He enjoys reading comics, and biking. Fun Fact: Aiden is one of few gay guys in highschool.

Carly is a 17 year old year old girl from Spain. She enjoys experimenting with makeup and is very active on Instagram. Carly loves talking to people; she would call herself a social butterfly.

  Please choose your character:  Caleb, Logan, Susan, Aiden, Carly
'''

def start():
    print(startGame)
    done = False
    while not done:
        character = str (input("Type the character's name! ")).lower()
        if character == "caleb":
            caleb.caleb()
            done = True
        elif character == "carly":
            carly.carly()
            done = True
        elif character == "logan":
            logan.logan()
            done = True
        elif character == "aiden":
            aiden.aiden()
            done = True
        elif character == "susan":
            susan.susan()
            done = True
        elif character == "exit":
            exit()
        else:
            print("Type character name!")

start()
