"""
Functions in python console, but not virtural environments like pythonanywhere
Notes: global variables not being changed by global variable designator in function although returned.
Item menu, combat, experience system, and leveling system functioning.
difficulty system functioning.
To do:
Boss health doesn't reset upon death [] Fixed, but needs testing
Variables do not reset upon death, need to reinitialize upon death (i.e. hasGold) []
Incorporate 'return to' area functions which allows for open world
Incorporate merchants to purchase items from [x]
Implement in-game menu [x]
Build world by defining location functions to drive story, combat, and NPCs []
Buid save/load system [x]
Stress test inventory system and prevent items which do not need to be used from being used []
Incorporate Tears of Denial's auto revive to prevent one death per playthrough (probably if user.tearsOfDenial = True/False:   replace mainMenu() in death() with keepGoing = True user.health += 100)
Assignment of class respective legendary weapons from side quest and add effects to weapons []
Write story []

Modifications:
06/12/20:
Added 'boss' parameter to Enemy class: Boolean True or False
Now cannot flee from bosses
merchant() functionality added
Fixed bug where enemy health doesn't reset on player death
Added to greatPlains() portion of story
Added in-game item menu feature

Professor Harris video (https://www.youtube.com/watch?v=e9miazksRD0)

Requires Dill:
    $ pip install dill or 'pip3.7 install --user dill' in python anywhere bash console. Depending on your version of python.user.name
This project won't function in virtural environment, however works in Python console.

dill documentation here:
    https://pypi.org/project/dill/
    https://dill.readthedocs.io/en/latest/index.html

dill citation:
    M.M. McKerns, L. Strand, T. Sullivan, A. Fang, M.A.G. Aivazis,
    "Building a framework for predictive science", Proceedings of
    the 10th Python in Science Conference, 2011;
    http://arxiv.org/pdf/1202.1056

    Michael McKerns and Michael Aivazis,
    "pathos: a framework for heterogeneous computing", 2010- ;
    http://trac.mystic.cacr.caltech.edu/project/pathos
"""
from random import *
import pickle
import dill
import pdb

name = ""
level = 1
strength = 10
maxHealth = 100
health = 100
weaponEquip = ""
gold = 100
inventory = []
exp = 0
progressCode = "a000"



def setName():
    global name
    user.name = input("""Late one fine Summer evening, after supervising your peasants toiling in the mudfields all day, you find that you have a lingering feeling that a quest is on the horizon. "Just my luck" you think to yourself.
"Another group of travelers whom will most certainly fail to remember my name which is: " Please enter your name: """)
    name = user.name
    return user.name
    name

def cheatMenu():
    print("Enter your cheat. Or enter 'options' to return to options menu. ")
    cheatInput = input("> ")
    if cheatInput == "IDDQD":
        user.maxHealth = 9999
        user.health = 9999
    elif cheatInput == "dnstuff":
        user.inventory.append(healthPotionLarge)
        user.inventory.append(healthPotionLarge)
        user.inventory.append(healthPotionLarge)
        user.weaponEquip = excalibur
    elif cheatInput.lower() == "options":
        optionsMenu()
    else:
        print("Nice try cheater...")
        cheatMenu()

def difficultyChoice():
    keepGoing = True
    while keepGoing:
        print("""Please select a difficulty:
0. Easy
1. Medium
2. Hard
3. Please hurt my feelings""")
        difficultyChoice = input("> ")
        global gameDifficulty
        if difficultyChoice == "0":
            gameDifficulty = "easy"
            keepGoing = False
        elif difficultyChoice == "1":
            gameDifficulty = "medium"
            keepGoing = False
        elif difficultyChoice == "2":
            gameDifficulty = "hard"
            keepGoing = False
        elif difficultyChoice == "3":
            print("Are you sure? Type 'yes or 'no'")
            yesno = input("> ")
            if yesno.lower() == "yes":
                gameDifficulty = "extreme"
                print("Now you've done it. Your adventure is cursed.")
                keepGoing = False
            else:
                print("Good choice.")
        else:
            print("I didn't quite understand that.")
            
    return gameDifficulty

gameDifficulty = "normal"

def chooseCharClass():
    print("""Which best describes you?
0. A knight, proud and strong. You like to solve problems head on and through brute force.
1. An assassain, the dark is your ally. You like to solve problems behind the scenes.
2. A renegade, quick-footed and elusive. You like to solve problems carefully.
3. A sorcerer, acquired knowledge and wisdom through a great deal of time. You like to solve problems with your superior intellect.""")
    charClass = input("> ")
    return charClass


def setCharClass(charClass):
    global weaponEquip
    if charClass == "0":
        user.weaponEquip = sword
        weaponEquip = user.weaponEquip
    elif charClass == "1":
        user.weaponEquip = dagger
        weaponEquip = user.weaponEquip
    elif charClass == "2":
        user.weaponEquip = bow
        weaponEquip = user.weaponEquip
    elif charClass == "3":
        user.weaponEquip = staff
        weaponEquip = user.weaponEquip
    return user.weaponEquip
    weaponEquip

def setProgressCode(code):
    user.progressCode = code
    return user.progressCode

def getProgressCode(self):
    progressCode = user.progressCode
    return progressCode

def setLocation(progressCode):
    if progressCode == "a000":
        startHouse()
    if progressCode == "a001":
        southernSettlement()
    elif progressCode == "a002":
        greatPlains()
    elif progressCode == "a003":
        keepRuins()
    else:
        if progressCode == "a004":
            ruinedCapitol()

def newGame(gameDifficulty):
    global name
    name = setName()
    if gameDifficulty == "easy":
        user.level = 1
        user.strength = 20
        user.maxHealth = 200
        user.health = 200
        user.weaponEquip = sword
        user.gold = 500
        user.inventory.append(healthPotionSmall)
        user.exp = 0
    elif gameDifficulty == "normal":
        user.level = 1
        user.strength = 10
        user.maxHealth = 100
        user.health = 100
        user.weaponEquip = sword
        user.gold = 100
        user.inventory.append(healthPotionSmall)
        user.exp = 0
    elif gameDifficulty == "hard":
        user.level = 1
        user.strength = 7
        user.maxHealth = 70
        user.health = 70
        user.weaponEquip = sword
        user.gold = 70
        user.exp = 0
    elif gameDifficulty == "extreme":
        user.level = 1
        user.strength = 5
        user.maxHealth = 50
        user.health = 50
        user.weaponEquip = sword
        user.gold = 50
        user.exp = 0
    else:
        user.level = 1
        user.strength = 10
        user.maxHealth = 100
        user.health = 100
        user.weaponEquip = sword
        user.gold = 100
        user.exp = 0
    setProgressCode("a000")
    charClass = chooseCharClass()
    setCharClass(charClass)
    setLocation(progressCode)
    return name
    return progressCode

class Weapon():
    def __init__(self, name, stength, effect, cost):
        self.name = name
        self.strength = strength
        self.effect = effect
        self.cost = cost
sword = Weapon("sword", 10, "Just a sword", 50)
dagger = Weapon("dagger", 5, "Attack three times in a turn", 10)
bow = Weapon("bow and arrows", 7, "Take less damage when attacking", 50)
staff = Weapon("magic staff", 8, "Apply elemental damage", 100)
excalibur = Weapon("The legendary sword, Excalibur", 25, "adds random damage", 1000)
avelyn = Weapon("A repeating crossbow", 15, "attacks 3 times", 1000)

def optionsMenu():
    print("""Welcome to the options menu, here you can enter cheats here. Please select an option.
1. Cheats
2. Main Menu""")
    optionsChoice = input("> ")
    if optionsChoice == "1":
        cheatMenu()
    elif optionsChoice == "2":
        mainMenu()
    else:
        print("I'm sorry, I didn't understand that.")
        optionsMenu()


def mainMenu():
    print("""Welcome to the distant past, a grand adventure awaits you! What would you like to do? Input 0, 1, 2, or 3.
    0. Begin a new journey
    1. Load your previous adventure
    2. Options
    3. Quit""")
    menuSelection = input("> ")
    if menuSelection == "0":
        difficultyChoice()
        newGame(gameDifficulty)
    elif menuSelection =="1":
        loadGame()
        print("Loading game")
        loadGame()
    elif menuSelection == "2":
        optionsMenu()
    elif menuSelection == "3":
        quit()
    else:
        print("I do not understand, please make another selection")
        mainMenu()

class Player():
    def __init__(self, name="", level=1, strength=10, maxHealth=100, health=100, weaponEquip="", gold=100, inventory=[], exp=0, progressCode = "a000"):
        self.name = name
        self.level = level
        self.strength = strength
        self.maxHealth = maxHealth
        self.health = health
        self.weaponEquip = weaponEquip
        self.gold = gold
        self.inventory = inventory
        self.exp = exp
        self.progressCode = progressCode

    def attack(self, enemy):
        success = randint(0, 10)
        damage = user.strength + user.weaponEquip.strength
        if success != 0:
            print("You attacked the {} with your {} and did {} damage!".format(enemy.name, user.weaponEquip.name, damage))
            enemy.health -= damage
            print("The {} now has {} health left!".format(enemy.name, enemy.health))
        else:
            print("Your attack missed!")

    def equipWeapon(self, weapon):
        user.weaponEquip = weapon
        return user.weaponEquip

    def levelUp(self):
        user.maxHealth += 20
        user.strength += 3
        user.level += 1
        user.health = user.maxHealth

    def getStats(self):
        print("""Your maximum health is: {}
Your strength is: {}
Your level is: {}""".format(user.maxHealth, user.strength, user.level))

    def gainExp(self, enemy):
        user.exp += enemy.expGiven
        if user.level == 1:
            if user.exp >= 10:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 2:
            if user.exp >= 25:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 3:
            if user.exp >= 50:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 4:
            if user.exp >= 85:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 5:
            if user.exp >= 120:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 6:
            if user.exp >= 150:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 7:
            if user.exp >= 200:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 8:
            if user.exp >= 250:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 9:
            if user.exp >= 300:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        elif user.level == 10:
            if user.exp >= 350:
                user.levelUp()
                print("You leveled up! Your stats are now: ")
                user.getStats()
            else:
                print("Great Job!")
        else:
            print("Great Job!")

    def itemMenu(self):
        keepGoing = True
        while keepGoing:
            print("Here are the items in your inventory: ")
            for index in range(len(user.inventory)):
                itemName = user.inventory[index].name
                number = index
                print("{}. {}".format(number, itemName))
            userChoice = input("Please select an item or type 'quit' to escape. ")
            if userChoice.isalpha() == True:
                userChoice = str(userChoice)
                if userChoice == "quit":
                    keepGoing = False
                else:
                    print("I'm sorry, I didn't understand that.")
            elif userChoice.isnumeric() == True:
                userChoice = int(userChoice)
                if userChoice in range(len(user.inventory)):
                    usePotion(user.inventory[userChoice])
                    user.inventory.pop(userChoice)
                else:
                    print("I'm sorry, I didn't understand that.")
            else:
                print("I'm sorry, I didn't understand that.")

    hasGold = False
    hasTearsOfDenial = False
    greatPlainsBossDefeated = False
    
user = Player(name, level, strength, maxHealth, health, weaponEquip, gold, inventory, exp, progressCode)

def setLevel(self):
    global level
    level = user.level
    return level

def setStrength(self):
    global strength
    strength = user.strength
    return strength

def setMaxHealth(self):
    global maxHealth
    maxHealth = user.maxHealth
    return maxHealth

def setGlobalHealth(self):
    global health
    health = user.health
    return health

def setGlobalWeaponEquip(self):
    global weaponEquip
    weaponEquip = user.weaponEquip
    return weaponEquip

def setGLobalGold(self):
    global gold
    gold = user.gold
    return gold

def setGlobalInventory(self):
    global inventory
    inventory = user.inventory
    return inventory

def setGlobalProgressCode(self):
    global progressCode
    progressCode = user.progressCode
    return progressCode

class Enemy():
    def __init__(self, name, strength, maxHealth, health, expGiven, boss=False):
        self.name = name
        self.strength = strength
        self.maxHealth = maxHealth
        self.health = health
        self.expGiven = expGiven
        self.boss = boss

    def attack(self, enemy):
        success = randint(0, 10)
        if success != 0:
            print("The {} attacks you! You take {} damage!".format(enemy.name, enemy.strength))
            user.health -= enemy.strength
            print("Your health is now {}.".format(user.health))
        else:
            print("The {}'s attack missed".format(enemy.name))

trainingDummy = Enemy("training dummy", 0, 100, 100, 0, False)
goblin = Enemy("goblin", 10, 50, 50, 5, False)
goblinWarlord = Enemy("Goblin Warlord", 15, 100, 100, 20, True)
troll = Enemy("troll", 25, 150, 150, 13, False)
wight = Enemy("wight", 20, 150, 150, 15, False)
dragon = Enemy("dragon", 50, 500, 500, 100, True)

class Item():
    def __init__(self, name, effect, cost):
        self.name = name
        self.effect = effect
        self.cost = cost

healthPotionSmall = Item("small health potion", 20, 10)
healthPotionMedium = Item("medium health potion", 50, 25)
healthPotionLarge = Item("large health potion", 100, 50)
tearsOfDenial = Item("tears of denial", 100, 500)

class npc():
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
settlementMerchant = npc("Settlement Merchant", healthPotionSmall)
wanderingMerchant = npc("Wandering Merchant", healthPotionMedium)
ghastlyMerchant = npc("Ghastly Merchant", healthPotionLarge)
hardyMerchant = npc("Hardy Merchant", healthPotionLarge)

class Location():
    def __init__(self, locationName, locationCode, enemy, npc, nextLocation):
        self.locationName = locationName
        self.locationCode = locationCode
        self.enemy = enemy
        self.npc = npc
        self.nextLocation = nextLocation
ruinedCapitol1 = Location("The Ruined Capitol", "a004", dragon, hardyMerchant, "null")
keepRuins1 = Location("Great Keep Ruins", "a003", troll, ghastlyMerchant, ruinedCapitol1)
greatPlains1 = Location("The Great Plains", "a002", goblin, wanderingMerchant, keepRuins1)
southernSettlement1 = Location("Southern Settlement", "a001", trainingDummy, settlementMerchant, greatPlains1)
startHouse1 = Location("Your house in the Southern Settlement", "a000", trainingDummy, "null", southernSettlement1)

def usePotion(potion):
    if user.health == user.maxHealth:
        print("You do not need to use that right now.")
    else:
        user.health += potion.effect
        if user.health > user.maxHealth:
            user.health = user.maxHealth
            print("You drank the {}, your health is now {}.".format(potion.name, user.health))

def battle(enemy):
    print("You encounter a {}!".format(enemy.name))
    userRoll = randint(1, 10)
    enemyRoll = randint(1, 10)
    keepGoing = True
    while keepGoing:
        print("""What would you like to do?
        1. Attack
        2. Item
        3. Flee""")
        choice = input("> ")
        if choice == "1":
            if userRoll >= enemyRoll:
                user.attack(enemy)
                if enemy.health <= 0:
                    print("The {} has been defeated. You gain strength.".format(enemy.name))
                    user.gainExp(enemy)
                    enemy.health = enemy.maxHealth
                    keepGoing = False
                else:
                    enemy.attack(enemy)
                if user.health <= 0:
                    keepGoing = False
                    death()
            else:
                enemy.attack(enemy)
                if user.health <= 0:
                    keepGoing = False
                    death()
                    enemy.health = enemy.maxHealth
                user.attack(enemy)
                if enemy.health <= 0:
                    print("The {} has been defeated. You gain strength.".format(enemy.name))
                    user.gainExp(enemy)
                    enemy.health = enemy.maxHealth
                    keepGoing = False
        elif choice == "2":
            user.itemMenu()
        elif choice == "3":
            if enemy.boss == False:
                fleeSuccess = randint(1, 4)
                if fleeSuccess != 1:
                    keepGoing = False
                    print("You got away")
                else:
                    print("The {} prevents your escape and calls you a chicken!".format(enemy.name))
                    enemy.attack(enemy)
            elif enemy.boss == True:
                print("You can't escape!")
        else:
            print("I didn't understand that, please try again")

def death():
    print("YOU DIED")
    mainMenu()

def saveGame():
    dill.dump_session(filename = "adventureGameSave.txt", main=None, byref=False)

def loadGame():
    dill.load_session(filename = "adventureGameSave.txt", main=None)

def explore():
    exploreNum = randint(1, 10)
    return exploreNum

def inGameMenu():
    keepGoing = True
    while keepGoing:
        print("""What would you like to do?
0. Item Menu
1. Stats
2. Equipment
3. Save Game
4. Return to Game
5. Main Menu
6. Quit""")
        inGameMenuInput = input("> ")
        if inGameMenuInput == "0":
            user.itemMenu()
        elif inGameMenuInput == "1":
            user.getStats()
        elif inGameMenuInput == "2":
            print("Your weapon is: {}".format(user.weaponEquip.name))
        elif inGameMenuInput == "3":
            saveGame()
            print("Saving your progress")
            print("Progress saved")
        elif inGameMenuInput == "4":
            keepGoing = False
        elif inGameMenuInput == "5":
            mainMenu()
        elif inGameMenuInput == "6":
            quit()

def merchant(area):
    merchantName = area.npc.name
    item = area.npc.inventory
    itemName = area.npc.inventory.name
    itemCost = area.npc.inventory.cost
    keepGoingMerchant = True
    while keepGoingMerchant:
        print("""{}: What would you like to buy?
0. {} : {} gold
1. Exit the shop""".format(merchantName, itemName, itemCost))
        merchantChoice = input("> ")
        if merchantChoice == "0":
            keepGoingPurchase = True
            print("""That will cost {} gold. Purchase?
0. No
1. Yes""".format(itemCost))
            purchaseChoice = input("> ")
            if purchaseChoice == "0":
                keepGoingPurchase = False
            elif purchaseChoice == "1":
                if user.gold >= itemCost:
                    user.gold -= itemCost
                    user.inventory.append(item)
                    print("Bought {}, you spent {} gold. Gold remaining: {}".format(itemName, itemCost, user.gold))
                    keepGoingPurchase = False
                else:
                    print("You can't afford that.")
                    keepGoingPurchase = False
            else:
                print("I don't understand")
        elif merchantChoice == "1":
            print("{}: Goodbye".format(merchantName))
            keepGoingMerchant = False
        else:
            print("I'm sorry, I didn't understand that.")
def startHouse():
    print("You awaken in your bed to the sound of horsehooves. Instinctively, you reach for your trusty {} and climb out of your bed.".format(user.weaponEquip.name))
    print("You hurredly head towards the door, still dreary from a restless night of sleep you nearly forget your gold pouch.")
    area = startHouse1
    keepGoing1 = True
    while keepGoing1:
        print("""What do you want to do?
0. Head out the door
1. Get your gold from the drawer
2. Look around
3. Look out the window""")
        userChoice1 = input("> ")
        if userChoice1 == "0":
            if user.hasGold == False:
                print("I need to get my gold first!")
            elif user.hasGold == True:
                keepGoing1 = False
                setProgressCode("a001")
                southernSettlement()
        elif userChoice1 == "1":
            if user.hasGold == False:
                print("You stumble over to your dresser and pick up your gold pouch.")
                print("Got {} gold!".format(user.gold))
                user.hasGold = True
            else: print("You've already collected your gold, there's nothing left in the drawer!")
        elif userChoice1 == "2":
            print("You look around the unkempt room. 'Nothing but useless trinkets,' you think to yourself.")
        elif userChoice1 == "3":
            print("You look out the window, you can see a man dressed as a king speaking with the guards. It sounds like they're discussing the migration of coconuts")
        else:
            print("I'm sorry, I didn't quite understand. Try getting your gold.")
def southernSettlement():
    area = southernSettlement1
    print("You step out of your house into the Southern Settlement. You look around and see the king has gone, and in his place the guards still stand discussing the airspeed velocity of various swallow")
    spacer1 = input("Press enter to continue")
    print("You pick up further bits of their conversation. '...great treasure' '...but no one has been to the capitol since the conflagration'")
    spacer2 = input("Press enter to continue")
    print("You decide to seek out this great treasure yourself.")
    input("Press enter to continue")
    print("You've unlocked the Options Menu.")
    input("Press enter to continue")
    print("You need to prepare for your adventure. You look around town and see the villagers beginning to start their day.")
    keepGoing2 = True
    while keepGoing2:
        print("""Where would you like to go?
1. Merchant
2. Combat Training
3. Menu
4. Exit the town""")
        userChoice2 = input("> ")
        if userChoice2 == "1":
            merchant(area)
        elif userChoice2 == "2":
            print("You approach the combat dummy and ready your {}. Fight!".format(user.weaponEquip.name))
            battle(trainingDummy)
        elif userChoice2 == "3":
            inGameMenu()
        elif userChoice2 == "4":
            keepGoing2 = False
            setProgressCode("a002")
            greatPlains()
        else:
            print("I don't understand. Please select another option")
def greatPlains():
    area = greatPlains1
    exploreCounter = 0
    print("You leave your cozy town and step foot into the world beyond...")
    print("You look around the vast plains before you, off in the distance you can see the ruins of a vast keep which once housed the kingdom guards.")
    print("You've now unlocked the explore feature. Use it to explore your surroundings and discover objects hidden in the environment.")
    input("Press enter to continue")
    keepGoing = True
    while keepGoing:
        print("""What would you like to do?
0. Explore
1. Menu
2. Proceed towards the keep ruins""")
        userChoice = input("> ")
        if userChoice == "0":
            explorationVariable = randint(1, 6)
            exploreCounter += 1
            goldFinderMed = randint(20, 50)
            goldFinderSmall = randint(5, 15)
            if explorationVariable == 1:
                print("You rummage through the remains of a merchant's cart, found {} gold!".format(goldFinderMed))
                user.gold += goldFinderMed
            elif explorationVariable == 2:
                print("You explore the area, but find nothing of value")
            elif explorationVariable == 3:
                print("You come across a fallen soldier, you could take his weapon, but you like your {}".format(user.weaponEquip.name))
            elif explorationVariable == 4:
                print("You find a some gold on the ground, got {} gold!".format(goldFinderSmall))
                user.gold += goldFinderSmall
            else:
                battle(area.enemy)
        elif userChoice == "1":
            inGameMenu()
        elif userChoice == "2":
            if exploreCounter >= 3:
                if user.greatPlainsBossDefeated == False:
                    print("You attempt to make your way to the keep ruins, but a fearsome enemy blocks your path!")
                    battle(goblinWarlord)
                    user.greatPlainsBossDefeated = True
                else:
                    keepGoing = False
                    keepRuins()
            else:
                print("I should explore more.")
        else:
            print("I'm sorry, I don't understand. Please try another command.")
                
def keepRuins():
    print("You enter into the ruins of the once great keep, now abandoned and deviod of human life.")
def ruinedCapitol():
    pass

def loadArea(progressCode):
    setLocation(user.progressCode)

