import time

start='''
WELCOME to {NAME}- Presented by TPMLJ.As you sit down to play this game, center yourself, take a deep breath,
and wash away all preconceived ideas you have about bullying.  Take a chance and explore the different characters’ lives
 in these different stories. Please choose your character: caleb, logan, aiden, carly
'''
bIntro= '''
You are on your way to tryouts. It’s a new season, and you and your closest friends are the team captains. As team captains you run the tryout practices to select the best new member for the team. 
'''

print(start)
done = False

while not done:
    character = input("Type the character's name! ")
    if character == "Caleb":
        print(cIntro)
