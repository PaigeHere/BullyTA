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
bPractice= '''
You decide to give into your friends. “Yea, sure. I’ll mess up the kid. This’ll be hilarious”, you lie to them. As you watch the boy doing the different stations
in practice you realize that you don’t really want to hurt the kid. He shows a lot of effort, maybe even more than the other boys, but you know you can’t back down
 now that you already promised your friends you’d mess him up. So, what are you going to do: Use your fists or single him out?
'''

bFists= '''
As the players finish up the stations that they were doing they come over to the benches where you sit with the other captains. Finally, the one kid comes over, out of breath and shaking.
He sits by his bag and starts drinking out of his water bottle you go over to him. “Hey boy. What’s your name? Nathan, aye? Okay Nathan. How do you explain being the last one here?”
He looks around at the boys who still haven’t come over to the bench, “Um... but I'm not, so... I’m sorry I don’t understand.” You feign annoyance, “OH so you don’t understand let me help you understand!”
With that you pull back your arm and punch him hard in the cheek. He cries out. All the boys saw you punch him. Your buddies are sneering and nudging each other laughing,
“Shit He did it! He really did it!” You stare down at your fist; it’s red and raw from the collision. You didn’t plan this well. All all the trainees stare and whisper about you,
“Should we tell someone?... I don’t know what to do…. Was that legal?... I don’t know if I want to play anymore…” You instantly regret the punch. What can you do to stop the whispers and put them back at ease?
Should you apologize to Nathan in front of all the boys?
'''

bAdmit='''
Oh Gosh, Nathan! I’m so sorry!!! I really didn’t mean that. I had a rough night last night my dad screamed his ass off at me and my mom is out and I don’t know
I’ve had a lot of stress” as I apologize I noticed that a lot of the words I’m saying are the truth. My friends looked at me with disapproval, but I didn’t care.
I wanted to make it up to this hard working boy. “You know Nathan, I was actually really surprised you didn’t finish faster. You were probably the most hardworking
out there. So um… in order to apologize and make it up to you I’m admitting you into the team. Congratulations!” Nathan looks at you with stunned eyes. “Um Yeah.
Thanks. Okay yea. I forgive you. Alright.” A smile forms on his face. “Thanks so much! Awesome. Wait you are?” You hadn’t even noticed that you hadn’t told him your
name yet. “Oh, I’m Caleb.” You look over at your friends while Nathan thanks you again
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
        print(bPractice)
        bViolence()
        done= True
    elif user_input = "No":
        print()

        done= True
    else:
        print("Please type Yes or No" )

Def  bViolence()
    done = False
    while not done:
        user_input = input("What will you do? Type Punch or Humiliate: ")
        if user_input == "Punch":
            print(bfists)
            bPunch()
            done = True
        elif user_input == "Humiliate":
            print()
            b()
            done = True
        else:
            print("Please type Punch or Humiliate.")

Def bPunch()
    done = False
    while not done:
        user_input = input("What will you do? Type Apologize or Ignore: ")
        if user_input == "Apologize":
            print(bAdmit)
            bApologize()
            done = True
        elif user_input == "Ignore":
            print()
            bIgnore()
            done = True
        else:
            print("Please type Apologize or Ignore: ")

Def bHumiliate()
    done = False
    while not done:
        user_input=
        if user_input == "l":
        elif user_input == "e":
        else:
            print("Please type )

Def bApologize
    print
    done = False
    while not done:
        user_input = input("What will you do? ")
Def bIgnore
