from Entities_Class import *
run = True
player = Player()
while run:
    print(player.health)
    print('Actions')
    print(player.actionList)
    action = int(input('What is your action?'))
    if action == 1:
        print('Potions:')
        print('1:Health, 2:Strength, 3:Resistance')
        potion = int(input('What potion'))
        player.drink_potion(potion)
        print(player.health)
    if action == 2:
        a = player.fight_monster()
        if a == 0:
            break
        
print('You Died')