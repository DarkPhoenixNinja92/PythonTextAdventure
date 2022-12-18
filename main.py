import random
restart = ''
inventory = []

def main():
    print('You come to a deep ravine. A rickety ladder leads down into a bottomless chasm below with paths leading off to the south and east and an open field stretches out before an expansive forest.')
    btnPress = input('Which path do you take? (ladder, south, east, field) ')
    randomNum = random.randint(1, 10)
    if btnPress == 'ladder':
        if randomNum >= 5:
            print('You make it safely to the forest floor. You hear the sound of a river to the east but are exhausted from your climb.')
            btnPress = input('Do you make for the river or find a safe spot to rest? (river, rest) ')
            if btnPress == 'river':
                print('After long hours of travel, you arrive at the east bank of the river. Suddenly, you notice ripples circling across the surface of the water. Something is about to emerge.')
                btnPress = input('Do you disturb the water, leave it be or attempt to cross to the opposite bank? (disturb, leave, cross) ')
                if btnPress == 'disturb':
                    print('A tail shoots out of the water, wrapping itself around your ankle and dragging you towards the surface of the lake.')
                elif btnPress == 'leave':
                    print('Thinking it best not to disturb whatever is in the water, you slowly back away from the river and begin trekking along the bank of the river in search of a safer crossing point')
                elif btnPress == 'cross':
                    print('You do not wish to disturb the river but need to cross to the opposite bank. You move slightly away from the central point the ripples are coming from and wade into the water to begin crossing.')
            elif btnPress == 'rest':
                print('You find a soft patch of ground and arrange your pack as a pillow and close your eyes to rest.')
                restRoll = random.randint(1,25)
                if restRoll < 10:
                    print('Your rest passes uneventfully. You awaken the next morning feeling extremely well rested.')
                elif restRoll <= 10 and restRoll < 20:
                    print('You hear a loud splash from the lake and the unmistakable sound of a creature stepping onto dry land. Whatever was in the lake has obviously decided to come out.')
                else:
                    print('You feel a sharp pain in your chest as a set of claws closes around your heart and tears it from your chest, killing you instantly.')
                    print('Game over!')
                    restart = input('Do you wish to play again? (y or n) ')
                    if restart == 'y':
                        print('Welcome to the Adventure!')
                        btnPress = input('Press p to play or q to quit! ')
                    if btnPress == 'q':
                        exit()
                    elif btnPress == 'p':
                        print('Playing!')
                        main()
                    elif restart == 'n':
                        quit
        else:
            print('You slip and fall to the forest floor, breaking your legs. A hungry lion smells your blood and comes to make a meal of you.')
            print('You have died.')
            restart = input('Do you wish to play again? (y or n) ')
            if restart == 'y':
                print('Welcome to the Adventure!')
                btnPress = input('Press p to play or q to quit! ')
                if btnPress == 'q':
                    exit()
                elif btnPress == 'p':
                    main()
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
                        print('Welcome to the Adventure!')
                        btnPress = input('Press p to play or q to quit! ')
                    if btnPress == 'q':
                        exit()
                    elif btnPress == 'p':
                        print('Playing!')
                        main()
                    elif restart == 'n':
                        quit
    elif btnPress == 'east':
        print('east')
    elif btnPress == 'field':
        print('field')

print('Welcome to the Adventure!')
btnPress = input('Press p to play or q to quit! ')
if btnPress == 'q':
    exit()
elif btnPress == 'p':
    print('Playing!')
    main()