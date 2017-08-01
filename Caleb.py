import time

start='''
WELCOME to {NAME}- Presented by TPMLJ.As you sit down to play this game, center yourself, take a deep breath,
and wash away all preconceived ideas you have about bullying.  Take a chance and explore the different characters’ lives
 in these different stories. Please choose your character: caleb, logan, aiden, carly
'''
bIntro= '''
You are on your way to tryouts. It’s a new season, and you and your closest friends are the team captains.
As team captains you run the tryout practices to select the best new member for the team. Your friends point out a scrawnier boy among the boys.
As you look at him yourself, your friends laugh and joke about how unqualified he must be. “Can he even hold the ball with those noodle arms?”, they say.
You aren’t amused but laugh anyways to get them off your back. Your friends stop laughing and turn to you. “Yo, Caleb. We should totally give him a hard time.
Why don’t you mess with him. Come on. It would  be funny!”
'''

print(start)
done = False

while not done:
    character = input("Type the character's name! ")
    if character == "Caleb":
        print(bIntro)
        done = True
done = False

while not done:
    user_input = input("What do you do? Do you give into the pressure? Type Yes or No: ")
    if user_input == "Yes":
        print()
        done= True
    elif user_input = "No"
        print()
    else:
        print("Please type Yes or No" )
