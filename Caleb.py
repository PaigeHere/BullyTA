import time

start = '''
WELCOME to Stand Up or Stand Down- Presented by TPMLJ.As you sit down to play this game, center yourself, take a deep breath,
and wash away all preconceived ideas you have about bullying.  Take a chance and explore the different characters’ lives
 in these different stories. Please choose your character: Caleb, logan, aiden, carly
'''
bIntro = '''
You are on your way to tryouts. It’s a new season, and you and your closest friends are the team captains.
As team captains you run the tryout practices to select the best new member for the team. Your friends point out a scrawnier boy among the boys.
As you look at him yourself, your friends laugh and joke about how unqualified he must be. “Can he even hold the ball with those noodle arms?”, they say.
You aren’t amused but laugh anyways to get them off your back. Your friends stop laughing and turn to you. “Yo, Caleb. We should totally give him a hard time.
Why don’t you mess with him. Come on. It would  be funny!”
'''
bFriends = '''
You don’t feel good about that idea. Your friends look at you expectantly, but you don’t want to give in to their pressure. “Nah, I don’t think I want to.
That doesn’t really seem right.”  They look at you still smiling, “Come on, Caleb. You can’t be serious! It’s just a little fun! It’s no big deal. What do you say?”
They really want you to do this. You think of your options: You could just mess around with the kid. You really don’t want to disappoint your friends, but at the same time.
You’re not sure if it would be the right thing to do. Is it worth it? Your friends wait for a reply, “So buddy. What d’ya say?”, one of them asks.
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

bAgainst = '''
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
learned from Nathan. If your friends force you to be mean to others, are they really your friends? Is it really worth it to hurt someone to please someone else?  If you realize something
is wrong, Stand Up and take action to make it right. The End
'''

bReport = '''
“This had gotten out of hand”, you say to Nathan, “It’s not right what they’re doing. I’m going to talk to the coach. He might still be in the office. Do you want to come with me?”
Nathan smiles, “Yea. Totally.” Together you walk to the coaches office. Luckily, Coach is still there packing up his papers. You both enter the office and tell your stories.
If your friends force you to be mean to others, are they really your friends? Is it really worth it to hurt someone to please someone else?  If you realize something is wrong,
Stand Up and take action to make it right. The End
'''
bIgnore = '''
You look at all the kids trying out. “What do you want?! Can I help you?” You shout to them. They all scatter. “I guess tryouts are over!” You joke to your friends. All of you laugh,
and then go your separate ways. You shower and go home. The next day at practice, Coach pulls you over. He starts talking to you, “Caleb. I’m really sorry I have to do this, but I’m
going to have to cut you from the team.” He looks at you apologetically. You are speechless, so he explains himself. “I heard from the boys that you punched Nathan, so I have to cut you.
I have no choice. It is against our team contract to use violence. It’s school policy. Sorry boy. Maybe try back for the team next year.” He gives you a pat on the back and heads
over to the practice. You go to the bench to grab your bag. “What was that all about?” The captains ask you. “You were cut, right? Haha. Not good enough for tryouts.” You’re filled
with fury when you respond. “Actually yes. I was kicked off the team. Thanks for nothing!” You say. In a furry you grab your bag and go home. Looking back, you can’t see how anything
you did was a good idea. All you did was hurt someone for fun and then lose. Without practice, you grow distant from your “friends”. You realize more and more what bullies they are,
and you are ashamed that you were one yourself. “Never again…” you think. Next time I will Stand Up against what is wrong. I will Stand Down to those I hurt.  The End
'''
bRunning = '''
As the players finish up the stations that they were doing they come over to the benches where you sit with the other captains. Finally, the one kid comes over, out of breath and shaking.
He sits by his bag and starts drinking out of his water bottle you go over to him. “Hey boy. What’s your name? Nathan, aye? Okay Nathan. How do you explain being the last one here?”
He looks around at the boys who still haven’t come over to the bench, “Um... but I'm not, so... I’m sorry I don’t understand.” You feign annoyance, “OH so you don’t understand let
me help you understand! Give me 3 Laps around the field!” He doesn’t move, “What?” I pretend to get angrier, “I SAID GIVE ME 3 LAPS! RUN!” With that he jolts up and runs his three laps
around the field.  Your buddies are sneering and nudging each other laughing, “Shit He did it! He really did it!” All the tryouts look at you and whisper, “What was that all about?...
That was harsh… What did Nathan do?... That’s annoying.” You want to get this over with. You don’t like hearing the whispers. “Alright everyone! Clear out please. Tryouts are over.
That’s right! Go home. Thanks!” They all reluctantly grab their things and leave whispering. You heave a sigh. Your friends are still smiling. They congratulate you and pass around
high fives, fist bumps, and light punches. Soon it’s just you and Nathan left. He comes over to you gasping for air. “So” gasp, “What” gasp “ was that all about?” he asks you. He stands
up straight and folds his arms. He does not look amused. You don’t know what to say. You could just get him off your back by punching him. He’ll never bother you again, or you could apologize.
'''

bHit = '''
You stride over to Nathan. “You know what?”, you say, “I’m done with this!” You pull up your arm and punch him. He stumbles back. “What was that for dude?!” He yells at you. You don’t
want to explain yourself. You pick up your bag and walk home. The next day at practice, Coach pulls you over. He starts talking to you, “Caleb. I’m really sorry I have to do this, but
I’m going to have to cut you from the team.” He looks at you apologetically. You are speechless, so he explains himself. “I heard that you punched Nathan, so I have to cut you. I have
no choice. It is against our team contract to use violence. It’s school policy. Sorry boy. Maybe try back for the team next year.” He gives you a pat on the back and heads over to the
practice. You go to the bench to grab your bag. “What was that all about?” The captains ask you. “You were cut, right? Haha. Not good enough for tryouts.” You’re filled with fury when
you respond. “Actually yes. I was kicked off the team. Thanks for nothing!” You say. In a furry you grab your bag and go home. Looking back, you can’t see how anything you did was a
good idea. All you did was hurt someone for fun and then lose. Without practice, you grow distant from your “friends”. You realize more and more what bullies they are, and you are
ashamed that you were one yourself. “Never again…” you think. Next time I will Stand Up against what is wrong. I will Stand Down to those I hurt.  The End
'''
bFlip='''
“Sorry. I just saw you trying so hard out there, I was disappointed when you weren’t the first back”. He looked confused, “But I came back after others because they didn’t actually
finish their station and left early from it.”  He has a good point, “Okay, yea, I get. Sorry. You shouldn’t have ran; I should have made some of the other boys run. Can we forget this
happened? It was my bad. I was a little on edge for the first day of practice.” He squints at you, trying to see the lie, but you truly are sorry and don’t want to hurt him. “Okay”,
he says, “Just don’t make me run for no reason again. Deal?” You’re relieved by his understanding, “Deal.” You shake hands and go home. The next day at practice, Coach calls you over.
“Hey Caleb. I heard from the other captains that you weren’t treating Nathan properly. I heard you were even harassing him after practice. I’m sorry but that is not within our team contract.
I’m going to have to cut you from the team.” You can’t believe what you heard. Everything goes fuzzy and numb. You walk over to the bench to pick up your bag. The captains are sneering
at you and whispering. As you leave you hear Coach yell after you, “I’m sorry Caleb! Come for some of the games!” As you walk home you think about this whole arch of events. You grow
angry towards your “friends”. You have learned a lot from this. Nothing good can come out of hurting someone for the enjoyment of others. It will come back to hurt you, and you now
know this. Time moves on and eventually the other captains are found out by the coach and cut from the team for harassment towards the players. After you Apologized to Nathan, you
both grow closer as friends. You have learned and lost, but also gained a good friend. Now you know to Stand Up for what is right and Stand Down to those you have done wrong. The End.
'''

def bApologize():
    print(bAgainst)
    done = False
    while not done:
        user_input = input("Type Report or Forgive: ").lower()
        if user_input == "report":
            print(bReport)
            time.sleep(10)
            done = True
        elif user_input == "forgive":
            print(bForgive)
            time.sleep(10)
            done = True
        else:
            print("Please type Report or Forgive.")


def bHumiliate():
    done = False
    while not done:
        user_input= input("What do you do? Type Apologize or Punch: ").lower()
        if user_input == "apologize":
            print(bFlip)
            time.sleep(8)
            done = True
        elif user_input == "punch":
            print(bHit)
            time.sleep(8)
            done = True
        else:
            print("Please type Apologize or Punch." )

def bPunch():
    done = False
    while not done:
        user_input = input("What will you do? Type Apologize or Ignore: ").lower()
        if user_input == "apologize":
            print(bAdmit)
            bApologize()
            done = True
        elif user_input == "ignore":
            print(bIgnore)
            time.sleep(8)
            done = True
        else:
            print("Please type Apologize or Ignore.")


def bViolence():
    done = False
    while not done:
        user_input = input("What will you do? Type Punch or Humiliate: ").lower()
        if user_input == "punch":
            print(bFists)
            bPunch()
            done = True
        elif user_input == "humiliate":
            print(bRunning)
            bHumiliate()
            done = True
        else:
            print("Please type Punch or Humiliate.")
def bDouble():
    done = False
    while not done:
        user_input = input("What will you do? Type Accept or Refuse: ").lower()
        if user_input == "accept":
            print(bPractice)
            bViolence()
            doen = True
        elif user_input == "refuse":
            bApologize()
            time.sleep(8)
            done = True
        else:
            print("Please type Accept or Refuse.")

def caleb():
    print(bIntro)
    done = False
    while not done:
        user_input = input("What do you do? Do you give into the pressure? Type Yes or No: ").lower()
        if user_input == "yes":
            print(bPractice)
            bViolence()
            done= True
        elif user_input == "no":
            print(bFriends)
            bDouble()
            done= True
        else:
            print("Please type Yes or No" )
