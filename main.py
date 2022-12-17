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
        quit
elif btnPress == 'south':
    print('south')
elif btnPress == 'east':
    print('east')
elif btnPress == 'field':
    print('field')