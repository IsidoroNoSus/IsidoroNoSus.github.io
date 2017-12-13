



#My python story
def greeting():
    response=input('Do you want to go on an adventure? (yes/no): ')
    print("You are a spy in 1945 and you are on your way to Nazi Germany. Your objective is to assassinate Hitler. ")
    return response
def second_choice():
    print("You are in a plane and there is a bomb set to explode in ten minutes. ")
    response=input('Do you try defuse it? (yes/no): ')
    return response
def third_choice():
    print("You go up to the bomb to try and defuse it and three Nazis come to stop you. ")
    response=input('Do you fight them? (yes/no): ')
    return response
def fourth_choice():
    print("You kill two of the Nazis with one punch. The last Nazi has good foot positioning meaning he has experience with hand-to-hand combat. He gets you in a rear naked choke and you become unconscious. You wake up and the timer on the bomb only has one minute and thirty seconds. There are three wires. RED BLUE and YELLOW.")
    response=input("Which wire do you cut? (red/blue/yellow ): ")
    return response
def fifth_choice():
    print("You survived the bomb. Now you have to pilot the plane to Germany to assassinate Hitler. You are right above Turkey. Your plane is facing north-west.If you fly to the left you land in France. If you fly to the right you land in Germany")
    response=input('Do you turn (right/left): ')
    return response
def sixth_choice():
    print("You landed in Germany. You find Hitler's hideout/base. He is watching an anime on the theatre screen.")
    response=input('Do you (watch the anime with him/assassinate him like president Abraham Lincoln): ')
    return response
def seventh_choice():
    print("You finished the anime and now you talk and decide to become friends with him")
    response=input('Do you decide to (assassinate him/join the nazis): ')
    return response
def eighth_choice():
    print("You and Hitler become great friends. You share drinks, go to amusement parks in Germany, watch more animes, and kill jews together. You get a really hot nazi girlfriend. You start to hang out with her more than Hitler now. Hitler wants to ride a new ride at a German Amusement park")
    response=input('What do you do? (Chill with your hot girlfriend/ride the new ride with Hitler): ')
    return response
def ninth_choice():
    print("Since you left to the amusement park to be with Hitler instead to be with your girlfriend, you and her get into a big argument. You notice that she doesn't really talk, kiss, and hug as much anymore. When you come home from a hard days work you notice that she isn't home")
    response=input('What do you do(You go to sleep and forget about the THOT/go look for your girlfriend): ')
    return response
def tenth_choice():
    print("You can't find her and you have looked everywhere. You go to Hitler for help and moaning upstairs")
    response=input('Do you (leave your friend alone and let him do his buisness/go upstairs to find out if your girlfriend is cheating): ')
    return response
def eleventh_choice():
    print("As you creep up the stairs, you notice it sounds like your girlfriend. You bust down Hitler's door and see your girlfriend naked in a bed with Hitler. You didn't take off your uniform from work and you remeber you have your Mauser C96 in your pistol holder")
    response=input('Do you (kill your best friend / Let him be) ;( : ')
    return response
    print('THE END')
def countdown(t):
    import time
    print('This window will remain open for 3 more seconds...')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Goodbye! \n \n \n \n \n')        
def no_opened():    
    print("You died! But it's okay, keep going.")
def opened():
    print('Alright')
def other():
    print("You Died")
x = greeting()

if x =="yes":
    y = second_choice()
    if y=="yes":
        opened()
    else:
        other()

else:
    no_opened()

    
if x =="yes":
    y = third_choice()
    if y=="yes":
        opened()
    else:
        other()

else:

    no_opened()

    
if x =="yes":
    y = fourth_choice()
    if y=="red":
        opened()
    else:
        other()

else:

    no_opened()

if x =="yes":
    y = fifth_choice()
    if y=="right":
        opened()
    else:
        other()

else:

    no_opened()

if x =="yes":
    y = sixth_choice()
    if y=="watch the anime with him":
        opened()
    else:
        other()


else:

    no_opened()
if x =="yes":
    y = seventh_choice()
    if y=="join the nazis":
        opened()
    else:
        other()


else:

    no_opened()
if x =="yes":
    y = eighth_choice()
    if y=="ride the new ride with Hitler":
        opened()
    else:
        other()

else:
    no_opened()


if x =="yes":
    y = ninth_choice()
    if y=="go look for your girlfriend":
        opened()
    else:
        other()

else:
    no_opened()
if x =="yes":
    y = ninth_choice()
    if y=="go look for your girlfriend":
        opened()
    else:
        other()

else:
    no_opened()
if x =="yes":
    y = tenth_choice()
    if y=="go upstairs to find out if your girlfriend is cheating":
        opened()
    else:
        other()
else:
    no_opened()
if x =="yes":
    y = eleventh_choice()
    if y=="kill your best friend":
        opened()
    else:
        other()




