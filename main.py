import random
restart = ''
inventory = ['knapsack', 'food', 'rope', 'cabin key', 'rusty iron sword']
openEquipSlots = 4
equipped = [
    {
        'name': inventory[4],
        'speed': 7,
        'attack': 1,
        'equip slot': 'main hand'
    }
    ]
health = 100

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
                print('You trapse across the grasslands until you stand upon the threshsold of that cabin.')
                btnPress = input('Nobody appears to be home. Do you knock on the door or seek another path? (knock, leave) ')
                cabinDoor = 'locked'
                if btnPress == 'knock':
                    print('You pound furiously on the door for several minutes but nobody responds. When you eventually think to try the door, it is locked. It would appear you must search elsewhere for a path forward... Unless you have the key? /n (To enter the cabin, you must have the "cabin key" item in your inventory. Use the "enter" command in this are once in possession of this item to enter the cabin.')
                btnPress = input('Do you wish to attempt to enter the cabin? (Requires the "cabin key" item to be in your inventory) ')
                if btnPress == 'yes':
                    for item in inventory:
                            if item == 'cabin key':
                                cabinDoor = 'unlocked'
                if cabinDoor == 'unlocked':
                        print('The door slides open with a click and you slip into the cabin.')
                elif cabinDoor == 'locked':
                        print('You have no means to enter the cabin. Search for the key and then return!')
                else:
                   print('You lack a means to gain entry into the cabin so you must search for help elsewhere.') 
        elif btnPress == 'leave':
                    print('You lack a means to gain entry into the cabin so you must search for help elsewhere.')
        elif btnPress == 'rest':
                restRoll = random.randint(1,25)
                if restRoll < 10:
                    print('Your rest passes uneventfully. You awaken the next morning feeling extremely well rested.')
                    btnPress = input('You prepare to set out again. Do you head for the tower or the cabin? (tower, cabin) ')
                    if btnPress == 'tower':
                        print('The tower seems your best bet so you begin crossing the landscape towards the imposing structure. Hours later, you arrive at the threshold of the tower.')
                        print('You have scarcely set foot in front of the tower when the door is flung open and an angry man brandishing a curved sword emerges. He is shouting incoherently in a language you do not recognize \n but you understand he wants you to leave.')
                        btnPress = input("Do you respect the man's wishes and depart, try to convince him to let you stay or ignore the mad old fool? (respect, convince, ignore) ")
                        if btnPress == 'respect':
                            print('You have no desire to cause trouble - less so with an armed lunatic brandishing a sword in your face so you take your leave of him and go back the way you came.')
                        elif btnPress == 'convince':
                            print('You calmly speak to the old man, trying your best to express that you mean no harm but he continues to rant and rave at you. Lacking a meanas to communicate properly, it seems you cannot make yourself understood by him.\n Unless you have a way to communicate with him? (requires golden branch')
                            btnPress = input('Do you have a means to communicate with the old man? ')
                            if btnPress == 'yes':
                                for item in inventory:
                                    hasBranch = ''
                                    if item == 'golden branch':
                                        hasBranch = True
                                if hasBranch == True:
                                    print('You hold up the branch and the man falls silent. Somehow, without words, the two of you know what the other thinks and believes and can communicate perfectly.')
                                elif hasBranch == False:
                                    print('As you lack a means to communicate with the man, you must depart lest you incur his ire.')
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