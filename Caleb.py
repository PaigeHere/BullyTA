import time

start = '''
WELCOME to Stand Up or Stand Down- Presented by TPMLJ.As you sit down to play this game, center yourself, take a deep breath,
and wash away all preconceived ideas you have about bullying.  Take a chance and explore the different characters’ lives
 in these different stories. Please choose your character: caleb, logan, aiden, carly
'''
bIntro = '''
You are on your way to tryouts. It’s a new season, and you and your closest friends are the team captains.
As team captains you run the tryout practices to select the best new member for the team. Your friends point out a scrawnier boy among the boys.
As you look at him yourself, your friends laugh and joke about how unqualified he must be. “Can he even hold the ball with those noodle arms?”, they say.
You aren’t amused but laugh anyways to get them off your back. Your friends stop laughing and turn to you. “Yo, Caleb. We should totally give him a hard time.
Why don’t you mess with him. Come on. It would  be funny!”
'''
bPractice = '''
You decide to give into your friends. “Yea, sure. I’ll mess up the kid. This’ll be hilarious”, you lie to them. As you watch the boy doing the different stations
in practice you realize that you don’t really want to hurt the kid. He shows a lot of effort, maybe even more than the other boys, but you know you can’t back down
 now that you already promised your friends you’d mess him up. So, what are you going to do: Use your fists or single him out?
'''

bFists = '''
As the players finish up the stations that they were doing they come over to the benches where you sit with the other captains. Finally, the one kid comes over, out of breath and shaking.
He sits by his bag and starts drinking out of his water bottle you go over to him. “Hey boy. What’s your name? Nathan, aye? Okay Nathan. How do you explain being the last one here?”
He looks around at the boys who still haven’t come over to the bench, “Um... but I'm not, so... I’m sorry I don’t understand.” You feign annoyance, “OH so you don’t understand let me help you understand!”
With that you pull back your arm and punch him hard in the cheek. He cries out. All the boys saw you punch him. Your buddies are sneering and nudging each other laughing,
“Shit He did it! He really did it!” You stare down at your fist; it’s red and raw from the collision. You didn’t plan this well. All all the trainees stare and whisper about you,
“Should we tell someone?... I don’t know what to do…. Was that legal?... I don’t know if I want to play anymore…” You instantly regret the punch. What can you do to stop the whispers and put them back at ease?
Should you apologize to Nathan in front of all the boys?
'''

bAdmit = '''
Oh Gosh, Nathan! I’m so sorry!!! I really didn’t mean that. I had a rough night last night my dad screamed his ass off at me and my mom is out and I don’t know
I’ve had a lot of stress” as I apologize I noticed that a lot of the words I’m saying are the truth. My friends looked at me with disapproval, but I didn’t care.
I wanted to make it up to this hard working boy. “You know Nathan, I was actually really surprised you didn’t finish faster. You were probably the most hardworking
out there. So um… in order to apologize and make it up to you I’m admitting you into the team. Congratulations!” Nathan looks at you with stunned eyes. “Um Yeah.
Thanks. Okay yea. I forgive you. Alright.” A smile forms on his face. “Thanks so much! Awesome. Wait you are?” You hadn’t even noticed that you hadn’t told him your
name yet. “Oh, I’m Caleb.” You look over at your friends while Nathan thanks you again.
They stare at you. “So you really want to do this? Do you think this guy will even be good?”
They are less than impressed with your actions. One of the other captains started talking,
“After you already punched him you think you can go be his friend? Well, whatever, I’m done with this. I can’t play this game with you. Sorry. Bye guys.” He just got up and left.
To my surprise all the other captains exchanged glances, got up, and followed him. You stand in the field with all the boys trying out. Nathan still stands next to you. “Forget them.”
He says. “Let’s go out for food.” Nathan, you and all the boys go to the nearest fast food place and stuff yourselves. You decide to welcome all the tryouts to the team.
'''

dAgainst = '''
After School the next day, you go to practice. All your new teammates joke with you in breaks, and on the field they listen to you. Meanwhile, the other captains have been shooting you glares.
They repeatedly make mean comments about you and laugh while you’re helping the new teammates. You’re annoyed, but you don’t want to make the situation worse than it is, so you don’t say anything
 to them. After practice ends you go into the locker room to shower. You can hear your mom’s voice in your head, “Caleb if you try to get into my car like a sweaty mess then you’re walking home.”
 You drop your bag on the bench, pull out your soap, grab your tower and head for the shower. While you’re showering you hear footsteps and a snicker, but think nothing of it. Finally, you get out
of the shower and find that your bag is gone. All you have is a towel and some soaps. You can’t go out of the locker room like that. It’s hopeless. You sit down on the bench and heave a sigh,
putting your hands on your head. Suddenly the door opens and you hear shouts from outside. Nathan comes in with your bag in his hands, “Caleb, I saw the other captains with this bag,
and I noticed it was yours, so I took it from them to give to you. I’m sorry that happened. Here.” He hands you your bag. You put on your cloths. You are surprised by your friends actions.
What do you do?
'''
bForgive= '''
You think back to tryouts. They pressured you into tormenting Nathan, and you gave in. Now after you decided to stop your own bullying they have retaliated by bullying you.
You feel sorry for them. “Can they not just be good to others?” You ask yourself. You decide to forgive their actions. You will be strong, but stand down and not retaliate yourself.
You have already stood up against them when you made up with Nathan. You forgive them because they have it worse than you. Time passes and you become great friends with Nathan.
Your old “friends” continue to bully you for awhile, but when you don’t pay them any attention, they lose interest and stop. The season ends, but you know you won’t forget what you
learned from Nathan. If you’re friends force you to be mean to others, are they really your friends? Is it really worth it to hurt someone to please someone else?  If you realize something
is wrong, Stand Up and take action to make it right.
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
    print(dAgainst)
    done = False
    while not done:
        user_input = input("Type Report or Forgive: ")
        if user_input = Report:
            print(bReport)
            sleep.time(10)
            done = True
        elif user_input = Forgive:
            print(bForgive)
            sleep.time(10)
            done = True
        else:
            print("Please type Report or Forgive: ")

Def bIgnore
