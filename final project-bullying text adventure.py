L_START = '''
Your name is Logan. You have just moved to sunny southern California from London, England. You cant wait to
get out there and make some new friends!
'''

L_BOY_NEXT_DOOR_NAME = ''' Logan'''

L_BOY_ON_BUS_NAME = '''Jacob'''

L_BOY_NEXT_DOOR = '''
Congrats! You met your first friend since moving to California, Peter. You guys quickly become great friends
and you find out more about him. He is really funny and smart. You get the feeling he's a bit of a nerd but
you dont mind because he is your best friend.
'''

L_BOY_ON_BUS = '''
Wow, you waited all week to finally meet someone your age on the bus to school. You sit down in an empty row
and soon more kids get on and the bus is filling up. Suddenly a new boyu comes and sits next to you. He introduces
himself as Jacob. You guy become very close and great friends. He lives a few blocks away and you guys hangout all
the time. He is pretty nerdy when it comes to science but it comes in handy when you guys are lab partners.
'''

L_JOCKS = '''
Some jocks walk up and try to make () do their homework. They threaten to hurt him if he doesn't. But you have no
idea what to do!!!
'''

L_NEW_FRIENDS = '''
A few months after school starts some people from the super popular table come to sit with you because they want to
learn more about England and to hear your accent. You try not to notice but you see the new people pushing () away
and you dont know how to stop it. () gets depressed becasue you could do nothing but stand by and watch the
bullying take place.
'''

L_FAIL = '''
You didn't do anything and therefore have failed your best freind when he needed you most...
'''

def start ():
    print (L_START)
    done = False
    while not done:
        user_input = str (input("Do you want to make friends with the boy next door or the boy on the bus? Type either 'next door' or 'bus'."))
        if user_input == "next door":
            print (L_BOY_NEXT_DOOR)

            done = True
        elif user_input == "bus":
            print (L_BOY_ON_BUS)

            done = True
        else:
            print ("Please type 'next door' or 'bus'.);
