import numpy as np
import random
class Player(object):
    def __init__(self, level=1, name='Player'):
        self.experienceLevel = level
        self.level = int(np.floor(self.experienceLevel/5))
        self.name = name
        self.gold = random.randrange(150,350)
        self.health = random.randrange(25,75)
        self.maxHealth = 100
        self.resistance = 0
        self.strength = 5
        self.actionList = ['1: Drink Potion', '2: Fight Monster', '3: Get Loot', '4: Buy Armor', '5: Buy Weapons']
        #self.speed = random.randrange(1,12)
        #self.luck = random.randrange(3,12)
    def drink_potion(self, potion_type):
        potion = potion_type
        '''
        1:Health
        2:Strength
        3:Resistance
        '''
        if potion == 1:
            self.health += 10
            if self.health > self.maxHealth:
                self.health = self.maxHealth
        elif potion == 2:
            self.strength += 3
        elif potion == 3:
            self.resistance += 3
        else:
            ('Sorry, potion not valid. BaDaBaBaBa')
    def fight_monster(self):
        mob = Mob()
        print(f'{self.name} has {self.health} health.')
        print(f'{mob.fullName} has {mob.mobHealth} health.')
        while mob.mobHealth > 0:
            mob.mobHealth -= self.strength
            if mob.mobHealth < 0:
                break
            self.health -= mob.attack_player()
        if self.health < 1:
            return 0
        else:
            mob.drop_gold()
            return 1
        
class Mob(object):
    def __init__(self):
        self.mobHealth = random.randrange(15, 26)
        self.goldDrop = random.randrange(10, 21) + self.mobHealth
        self.damage = mobHealth-10
        firstName = random.sample(['Angry ','Cute ','Spiky ','Stinky ','Fury ','Scaley ',\
            'Cuddley ','Special ','Disgusting '],1)
        lastName = random.sample(['Bird','Elephent','Porch','Fish','Dragon','Dog',\
            'Code','Blanket','Mob'],1)
        time = random.sample(['1st', '2nd', '3rd', '4th', '5th', \
                '6th', '7th', '8th', '9th', '10th'],1)
        self.fullName = ''.join(firstName + lastName + [' the '] + time)
        
    def attack_player(self, pl):
        return self.damage
        
    def drop_gold(self):
        self.mobHealth = 0
        return self.goldDrop
        