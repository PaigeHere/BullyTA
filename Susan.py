sIntro = '''
You are Susan. One day as you wait for your daughter to get out of school you
noticed your daughter, Rachel, and a couple of other girls in the football field.
You look a little closer and you can see that Rachel and those girls were
bullying another girl. Rachel was kicking the girl and appears to be holding a gray
backpack. You know that it's not Rachel's bag because everything that Rachel owns
is either pink or white. Rachel then proceeds to dump out the contents of the gray
bag onto the field. What do you do next?

Do you immediately get out of the car and help the girl that's getting bullied by
your daughter or do you ignore everything and wait for Rachel to get into the car?
'''

sGet_Out = '''
You get out the car and rush towards the girl on the floor. The girl had passed out.
As you pick up the girl, you can hear your Rachel yelling, "Mom what are you doing?"
You ignore Rachel and get the girl into the school building. As you help the girl,
you tell Rachel to pick up the stuff on the ground and put it back into the gray bag.
The principal notices you enter the building with the girl and tells everyone to
go to his office while the nurse takes the girl to the nurse's office. The principal
then asks what happens. What do you do next?

Do you tell the principal that it was your daughter that was the one bullying the
girl or do you lie about it?
'''
sIgnore_dinner = '''
As Rachel walks towards the car with her friends, you notice her in a happy mood.
You greet them and drive her friends home. When you get home, you see that your
husband is in kitchen making dinner. You go into your office and work, but you can't
help thinking about Rachel bullying the poor girl.

It is dinner time and everyone is sat together eating. Should you talk to Rachel about
what you saw today or should you continue on with your day?
'''

sBully_Convo = '''
You tell Rachel that you saw her with her friends in the football field. You lecture
Rachel about the effects of bullying and you tell her it can cause the girl to have
depression and anxiety. You tell Rachel that bullying can lead to suicide.

Do you take Rachel to apologize to the girl or do you tell Rachel to not
do it again?
'''
sIgnore_Next_Day = '''
The next day, you arrive at the school. As you wait for Rachel, you see her bullying
the girl again. What do you want to do this time?

Do you immediately get out of the car and help the girl that's getting bullied by
your daughter or do you ignore everything and wait for Rachel to get into the car?
'''

sIgnore_Final = '''
You ignore the situation once again. This time, the principal happens to be showing
the superintendent the school and the football field. The both of them sees what
happens and immediately helps the girl up. The superintendent and the principal
tells the girls to go to the principal's office. Whilst everything is happening,
you are sitting in the car and watching. A while later, you get a call and learn that
Rachel and the girls are suspended and the girl had passed out and was seriously injured.

The suspension had scarred Rachel's records and everyone in the school no longer looks
up to her as she lost her place as her class president and the head cheerleader.
'''
sDefend_Rachel = '''
You tell the princpal that you saw the girl lying on the floor and that Rachel and her
friends were trying to help the girl get up. The principal stares at you as if you are
telling a fib. What do you do?

Do you tell the principal that it was your daughter that was the one bullying the
girl or do you contune lying about it?
'''
sHelp_Final = '''
You get out the car and rush towards the girl on the floor. The girl had passed out.
As you pick up the girl, you can hear your Rachel yelling, "Mom what are you doing?"
You ignore Rachel and get the girl into the school building. As you help the girl,
you tell Rachel to pick up the stuff on the ground and put it back into the gray bag.
You take the girl to the nurse's office. When the girl wakes up, you make Rachel apologize.
The girl then learns that you were the one that helped her to the nurse's offices. Rachel
aplogizes to the girl and the girl accepts her apology. You then ask the girl about her
grades and the girl tells you that she is not doing very well at school. You tell Rachel
to tutor the girl. Years later, Rachel is good friends with the girl and had stopped
talking to her other friends.

'''
sApologize = '''
You take Rachel to apologize to the girl. The girl had learned that you were the one
that helped her to the nurse's offices. Rachel aplogizes to the girl and the girl
accepts her apology. You then ask the girl about her grades and the girl tells you
that she is not doing very well at school. You tell Rachel to tutor the girl. Years
later, Rachel is good friends with the girl and had stopped talking to her other friends.
'''


print(sIntro)
done = False
while not done:
    user_input = input("Type 'help' to help the girl or 'ignore' to ignore everything: ")
    if user_input == "help":
        print(sGet_Out)
        done2 = False
        while not done2:
                user_input = input("Type 'lie' to lie to the principal or 'truth' to reveal what you saw: ")
                if user_input == "lie":
                    print(sDefend_Rachel)
                    done3 = False
                    while not done3:
                        user_input = input("Type 'lie' to continue lying or 'truth' to reveal what you saw: ")
                        if user_input == "lie":
                            print(sIgnore_Next_Day)
                            done4 = False
                            while not done4:
                                user_input = input("Type 'help' to help the girl or 'ignore' to girl everything: ")
                                if user_input == "ignore":
                                    print(sIgnore_Final)
                                    done4 = True
                                elif user_input == "help":
                                    print(sHelp_Final)
                                    done4 = True
                                else:
                                    print("Please type 'help' or 'ignore': ");
                            done3 = True
                        elif user_input == "truth":
                            print(sBully_Convo)
                            done5 = False
                            while not done5:
                                user_input = input("Type 'apologize' to apologize to the girl or 'stop' to finish off lecture: ")
                                if user_input == "apologize":
                                    print(sApologize)
                                    done5 = True
                                elif user_input == "stop":
                                    print(sIgnore_Next_Day)
                                    done6 = False
                                    while not done6:
                                        user_input = input("Type 'help' to help the girl or 'ignore' to ignore everything: ")
                                        if user_input == "help":
                                            print(sHelp_Final)
                                            done6 = True
                                        elif user_input == "ignore":
                                            print(sIgnore_Final)
                                            done6 = True
                                        else:
                                            print("Please type 'help' or 'ignore': ")
                                        done5 = True
                                else:
                                    print("Please type 'apologize' or 'stop': ");
                            done3 = True
                        else:
                            print("Plese type 'lie' or 'truth': ");
                    done2 = True
                elif user_input == "truth":
                    print(sBully_Convo)
                    done7 = False
                    while not done7:
                        user_input = input("Type 'apologize' to apologize to the girl or 'stop' to finish off lecture: ")
                        if user_input == "apologize":
                            print(sApologize)
                            done7 = True
                        elif user_input == "stop":
                            print(sIgnore_Next_Day)
                            done8 = False
                            while not done8:
                                user_input = input("Type 'help' to help the girl or 'ignore' to ignore everything: ")
                                if user_input == "help":
                                    print(sHelp_Final)
                                    done8 = True
                                elif user_input == "ignore":
                                    print(sIgnore_Final)
                                    done8 = True
                                else:
                                    print("Please type 'help' or 'ignore': ");
                            done7 = True
                    done2 = True
                else:
                    print("Please type 'lie' or 'truth': ");
        done = True

    elif user_input == "ignore":
        print(sIgnore_dinner)
        done9 = False
        while not done9:
                user_input = input("Type 'talk' to talk to Rachel about bullying or 'ignore' to continue on with the day: ")
                if user_input == "talk":
                    print(sBully_Convo)
                    done10 = False
                    while not done10:
                        user_input = input("Type 'apologize' to apologize to the girl or 'stop' to finish off lecture: ")
                        if user_input == "apologize":
                            print(sApologize)
                            done10 = True
                        elif user_input == "stop":
                            print(sIgnore_Next_Day)
                            done11 = False
                            while not done11:
                                user_input = input("Type 'help' to help the girl or 'ignore' to ignore everything: ")
                                if user_input == "help":
                                    print(sHelp_Final)
                                    done11 = True
                                elif user_input == "ignore":
                                    print(sIgnore_Final)
                                    done11 = True
                                else:
                                    print("Please type 'help' or 'ignore': ");
                            done10 = True
                        else:
                            print("Please type 'apologize' or 'stop': ");
                    done9 = True
                elif user_input == "ignore":
                    print(sIgnore_Next_Day)
                    done12 = False
                    while not done12:
                        user_input = input("Type 'help' to help the girl or 'ignore' to ignore everything: ")
                        if user_input == "help":
                            print(sHelp_Final)
                            done12 = True
                        elif user_input == "ignore":
                            print(sIgnore_Final)
                            done12 = True
                        else:
                            print("Please type 'help' or 'ignore': ");
                    done9 = True
                else:
                    print("Please type 'talk' or 'ignore': ");
        done = True
    else:
        print("Please type 'help' or 'ignore': ");
