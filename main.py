import random

print('Welcome to the Adventure!')
btnPress = input('Press p to play or q to quit! ')
if btnPress == 'q':
    exit()
elif btnPress == 'p':
    print('Playing!')

print('You come to a deep ravine. A rickety ladder leads down into a bottomless chasm below with paths leading off to the south and east and an open field stretches out before an expansive forest.')
btnPress = input('Which path do you take? (ladder, south, east, field) ')
randomNum = random.randint(1, 10)
if btnPress == 'ladder':
    if randomNum >= 5:
        print('You make it safely to the forest floor. You hear the sound of a river to the east but are exhausted from your climb.')
        print('Do you make for the river or find a safe spot to rest? (river, rest) ')
    else:
        print('You slip and fall to the forest floor, breaking your legs. A hungry lion smells your blood and comes to make a meal of you.')
        print('You have died.')
        restart = input('Do you wish to play again? (y or n) ')
        if restart == 'y':
            pass
        elif restart == 'n':
            quit
elif btnPress == 'south':
    print('You make your way south through the thorny underbrush. You walk until your feet ache and you can go no further. Over the horizon, to the northwest, you spy a tower jutting out of the landscape. To the east, you spy a small log cabin. Perhaps a sign of life?')
    btnPress = input('Do you make for the tower, head for the cabin or find a soft patch of ground to lay down and rest? (tower, cabin, or rest) ')
    if btnPress == 'tower':
            print(btnPress)
    elif btnPress == 'cabin':
            print(btnPress)
    elif btnPress == 'rest':
            restRoll = random.randint(1,25)
            if restRoll < 10:
                print('Your rest passes uneventfully. You awaken the next morning feeling extremely well rested.')
                btnPress = input('You prepare to set out again. Do you head for the tower or the cabin? (tower, cabin) ')
            elif restRoll <= 10 and restRoll < 20:
                print('You awaken to a rustling in the bushes. Something is observing you.')
            else:
                print('You feel a sharp pain in your throat. You briefly open your eyes only to see a cloaked figure run a knife across your neck. He swiftly departs and you slowly bleed to death.')
                print('Game over!')
                restart = input('Do you wish to play again? (y or n) ')
                if restart == 'y':
                    pass
                elif restart == 'n':
                    quit
elif btnPress == 'east':
    print('east')
elif btnPress == 'field':
    print('field')