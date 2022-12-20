import random
battleState = 'passive'
health = 100
exp = 0
speed = 50
weaponDmg = 9
level = 1
encounteredEnemy = True
# damage = weaponskill + level + weaponDmg - enemyArmor

if encounteredEnemy == True:
    battleState = 'engaged'
    
while battleState == 'engaged':
    firstRoll = True
    
    enemyName = 'Thug'
    enemyLevel = 1
    enemyHealth = 10
    enemySpeed = 20
    enemyDmg = random.randint(2,15)
    
    if firstRoll == True:
        print('You encountered a thug!')
        battleJoin = input('Do you wish to fight or flee? ')
        if battleJoin == 'fight':
            print('Roll for initiative! ')
            playerInitiative = random.randint(1, 20)
            enemyInitiative = random.randint(1, 20)
            
            print(f'You rolled {playerInitiative}')
            print(f'Your opponent rolled {enemyInitiative}')
            
            if playerInitiative > enemyInitiative:
                print('You go first!')
                move = input ('Do you wish to attack or flee? ')
                if move == 'attack':
                    hitRoll = random.randint(1, 20)
                    enemyDodge = random.randint(1, 20)
                    if hitRoll > enemyDodge:
                        print('You land a blow')
                        damageDealt = weaponDmg + level
                        enemyHealth = enemyHealth - damageDealt
                        if enemyHealth <= 0:
                            battleState = 'passive'
                            print('The thug crumples to the ground dead and you raise your blade in triumph!')
                    elif hitRoll < enemyDodge:
                        print('The thug deftly dances around your blows, avoiding harm.')
            elif playerInitiative < enemyInitiative:
                print('The enemy goes first!')
            elif playerInitiative == enemyInitiative:
                print('The roll was a tie. You both reroll')
                