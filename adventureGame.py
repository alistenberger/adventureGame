"""
Functions in python console, but not virtural environments like pythonanywhere
Notes: global variables not being changed by global variable designator in function although returned.
Item menu, combat, experience system, and leveling system functioning.
difficulty system functioning.
To do:
Make explored player class variable set explore counter to minimum of 3 so return to areas dont require exploration []
Enemies slain/enemies remaining not functioning []
Add merchants to story areas. [x]
Add branching sidequest to obtain tears of denial/super weapons []
Boss health doesn't reset upon death [o] Fixed, but needs testing. Updated, needs further testing
Progress variables in Player class do not reset upon death, need to reinitialize upon death and start new game (i.e. hasGold) [o] fixed needs tested
Incorporate 'return to' area functions which allows for open world []
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

06/14/20:
Enemy health further modified to regenerate upon death
set variables to reset at new game
Added in game stat display, which displays more than the level up message for stats
Added keep ruins story segment and boss fight
Added 'has visited' boolean variables to player class, need to add corresponding functions
Added sidequest areas primordial oak tree and ancient lake
Added sidequest npcs Mysterious woman and lady in the lake
Added channeling stone for tears of denail sidequest
Added 'explored'*area* variable to Player class. Sets exploreCounter to minimum of 3 if an area has been explored sufficiently
Created newGameVariables() which sets all progress Player class variables to default options

directory: cd /C/Users/Alsty/Desktop/Classes/CSCI_23000/adventureGame
git push: git push -u https://github.com/alistenberger/adventureGame.git

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

def newGameVariables():
    user.hasGold = False
    user.hasTearsOfDenial = False
    user.startHouseVisited = False
    user.southernSettlementVisited = False
    user.greatPlainsVisited = False
    user.exploredGreatPlains = False
    user.primordialOakTreeVisited = False
    user.keepRuinsVisited = False
    user.exploredKeepRuins = False
    user.hasChannelingStone = False
    user.brokeThroughWall = False
    user.ancientLakeVisited = False
    user.worthinessProven = False
    user.acceptedLakeGift = False
    user.ruinedCapitolVisited = False
    user.exploredRuinedCapitol = False
    user.greatPlainsBossDefeated = False
    user.keepRuinsBossDefeated = False
    user.ruinedCapitolBossDefeated = False
    user.enemiesSlain = 0

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
    newGameVariables()
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

    enemiesSlain = 0
    enemiesRemaining = 20 - enemiesSlain

    def getStatsMenu(self):
        print("""
Here are your stats:
Name: {}
Level: {}
Strength: {}
Max Health: {}
Current Health: {}
Amount of Gold: {}
Total Experience: {}
Total Enemies Slain: {}""".format(user.name, user.level, user.strength, user.maxHealth, user.health, user.gold, user.exp, user.enemiesSlain))

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
    startHouseVisited = False
    southernSettlementVisited = False
    greatPlainsVisited = False
    exploredGreatPlains = False
    primordialOakTreeVisited = False
    keepRuinsVisited = False
    exploredKeepRuins = False
    hasChannelingStone = False
    brokeThroughWall = False
    ancientLakeVisited = False
    worthinessProven = False
    acceptedLakeGift = False
    ruinedCapitolVisited = False
    exploredRuinedCapitol = False
    greatPlainsBossDefeated = False
    keepRuinsBossDefeated = False
    ruinedCapitolBossDefeated = False
    
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

def setGlobalGold(self):
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
ghastlyTroll = Enemy("ghastly troll", 30, 250, 250, 30, True)
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
mysteriousWoman = npc("Mysterious Woman", tearsOfDenial)
ladyInTheLake = npc("The Lady in the Lake", "null")

class Location():
    def __init__(self, locationName, locationCode, enemy, npc, nextLocation):
        self.locationName = locationName
        self.locationCode = locationCode
        self.enemy = enemy
        self.npc = npc
        self.nextLocation = nextLocation
ruinedCapitol1 = Location("The Ruined Capitol", "a004", dragon, hardyMerchant, "null")
keepRuins1 = Location("Great Keep Ruins", "a003", troll, ghastlyMerchant, ruinedCapitol1)
ancientLake1 = Location("The Ancient Lake", "a006", "null", ladyInTheLake, keepRuins1)
greatPlains1 = Location("The Great Plains", "a002", goblin, wanderingMerchant, keepRuins1)
primordialOakTree1 = Location("The Primordial Oak Tree", "a005", "null", mysteriousWoman, greatPlains1)
southernSettlement1 = Location("Southern Settlement", "a001", trainingDummy, settlementMerchant, greatPlains1)
startHouse1 = Location("Your house in the Southern Settlement", "a000", trainingDummy, "null", southernSettlement1)

def usePotion(potion):
    if user.health == user.maxHealth:
        print("You do not need to use that right now, but you drink it anyway.")
    else:
        user.health += potion.effect
        if user.health > user.maxHealth:
            user.health = user.maxHealth
        print("You drank the {}, your health is now {}/{}.".format(potion.name, user.health, user.maxHealth))

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
                    user.enemiesSlain += 1
                    enemy.health = enemy.maxHealth
                    keepGoing = False
                else:
                    enemy.attack(enemy)
                if user.health <= 0:
                    if user.hasTearsOfDenial == True:
                        user.health = user.maxHealth
                        print("The mysterious woman's vial breaks open as your body crashes to the ground, spilling the contents inside.")
                        input("Press enter to continue.")
                        print("You suddenly feel the life return to your body. Filled with the will to continue, you stand.")
                        user.hasTearsOfDenial = False
                    elif user.hasTearsOfDenial == False:
                        keepGoing = False
                        enemy.health = enemy.maxHealth
                        death()
            else:
                enemy.attack(enemy)
                if user.health <= 0:
                    if user.hasTearsOfDenial == True:
                        user.health = user.maxHealth
                        print("The mysterious woman's vial breaks open as your body crashes to the ground, spilling the contents inside.")
                        input("Press enter to continue.")
                        print("You suddenly feel the life return to your body. Filled with the will to continue, you stand.")
                        user.hasTearsOfDenial = False
                    elif user.hasTearsOfDenial == False:
                        keepGoing = False
                        enemy.health = enemy.maxHealth
                        death()
                user.attack(enemy)
                if enemy.health <= 0:
                    print("The {} has been defeated. You gain strength.".format(enemy.name))
                    user.gainExp(enemy)
                    user.enemiesSlain += 1
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
    print("Your body crashes to the floor and you feel your strength leave you.")
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
            user.getStatsMenu()
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
                user.startHouseVisited = True
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
    user.southernSettlementVisited = True
    keepGoingSettlement = True
    while keepGoingSettlement:
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
            keepGoingSettlement = False
            setProgressCode("a002")
            greatPlains()
        else:
            print("I don't understand. Please select another option")
            
def greatPlains():
    area = greatPlains1
    exploreCounter = 0
    print("You leave your cozy town and step foot into the world beyond...")
    print("You look around the vast plains before you and see a merchant wandering the plains with his pack. Off in the distance, far to the north, you can see the ruins of a vast keep which once housed the kingdom guards.")
    input("Press enter to continue")
    print("Far to the west, you see a towering oak tree serrounded by a dense underbrush.")
    input("Press enter to continue")
    print("You've now unlocked the explore feature. Use it to explore your surroundings and discover objects hidden in the environment.")
    input("Press enter to continue")
    user.greatPlainsVisited = True
    keepGoingPlains = True
    while keepGoingPlains:
        print("""What would you like to do?
0. Explore
1. Menu
2. Proceed towards the keep ruins
3. Proceed towards the giant oak tree
4. Approach the merchant""")
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
                    keepGoingPlains = False
                    keepRuins()
            else:
                print("I should explore more.")
        elif userChoice == "3":
            keepGoingPlains = False
            primordialOakTree()
        elif userChoice == "4":
            print("You follow the merchants trail and eventually catch up with him.")
            merchant(area)
        else:
            print("I'm sorry, I don't understand. Please try another command.")

def primordialOakTree():
    area = primordialOakTree1
    print("You step through the tangled underbrush and approach the ancient tree, an apparation of a woman stands under it.")
    input("Press enter to continue")
    keepGoingTree = True
    while keepGoingTree:
        print("""What would you like to do?
0. Approach the woman
1. Menu
2. Return to the Great Plains""")
        userChoiceTree = input("> ")
        if userChoiceTree == "0":
            if user.hasChannelingStone == False:
                print("She doesn't react to you, but rather stares off in the distance at the Keep Ruins")
            elif user.hasChannelingStone == True and user.hasTearsOfDenial == False:
                print("She turns to face you and stretches out her hand. In her hand is a vial containing a liquid.")
                print("""You hear a voice echo in your mind...
{}: 'This is my gift to you. In this jar are my tears, they will aid you in a time of great peril.'""".format(area.npc.name))
                print("""
What would you like to do?
0. Take it
1. Refuse her gift""")
                tearsChoice = input("> ")
                if tearsChoice == "0":
                    user.hasTearsOfDenial = True
                    print("You reach out and accept the gift. A strange energy emits from the vial...")
                elif tearsChoice == "1":
                    print("You refuse the gift. The woman seems saddened by your choice.")
                else:
                    print("I don't understand, please select another option.")
            elif user.hasChannelingStone == True and user.hasTearsOfDenial == True:
                print("""You hear a voice echo in your mind...
{}: 'I have nothing else to give you. Return once you have used my gift.""".format(area.npc.name))
        elif userChoiceTree == "1":
            inGameMenu()
        elif userChoiceTree == "2":
            keepGoingTree = False
            greatPlains()
        else:
            print("I do not understand. Please try another option.")
    
                
def keepRuins():
    area = keepRuins1
    exploreCounter = 0
    print("You enter into the ruins of the once great keep, now abandoned and deviod of human life, save for one brave merchant whom set up shop just outside the keep.")
    input("Press enter to continue")
    user.keepRuinsVisited = True
    keepGoingKeepRuins = True
    while keepGoingKeepRuins:
        print("""What would you like to do?
0. Explore
1. Menu
2. Proceed towards the capitol
3. Return to the Great Plains
4. Approach the crumbling wall
5. Approach the merchant""")
        userChoice = input("> ")
        if userChoice == "0" and user.hasChannelingStone == False and exploreCounter >= 3:
            print("""You find a small stone on the ground and sense a strange energy emitting from within it. You pick the stone up and strangely feel drawn to the primordial oak tree.""")
            user.hasChannelingStone = True
        elif userChoice == "0":
            explorationVariable = randint(1, 6)
            exploreCounter += 1
            goldFinderMed = randint(20, 50)
            goldFinderSmall = randint(5, 15)
            if explorationVariable == 1:
                print("You rummage through the remains of an old chest, found {} gold!".format(goldFinderMed))
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
                if user.keepRuinsBossDefeated == False:
                    print("You attempt to make your way to the keep ruins, but a fearsome enemy blocks your path!")
                    battle(ghastlyTroll)
                    user.keepRuinsBossDefeated = True
                else:
                    keepGoingKeepRuins = False
                    ruinedCapitol()
            else:
                print("I should explore more.")
        elif userChoice == "3":
            keepGoingKeepRuins = False
            greatPlains()
        elif userChoice == "4":
            if user.brokeThroughWall == False:
                print("You cautiously approach the crumbling wall, you can feel a breeze coming through the wall.")
                input("Press enter to continue")
                print("""What would you like to do?
0. Leave the wall alone, it looks dangerous.
1. Attempt to bring down the wall.""")
                userChoiceWall = input("> ")
                if userChoiceWall == "0":
                    print("Its probably best left alone.")
                elif userChoiceWall == "1":
                    print("You begin the arduous process of clearing the wall. After what seems like hours, you finally clear a path through.")
                    user.brokeThroughWall = True
                else:
                    print("I'm sorry, I do not understand. Please select another option.")
            elif user.brokeThroughWall == True:
                print("""You approach the path you made. Would you like to proceed through the wall?
0. No
1. Yes""")
                userChoiceWallThrough = input("> ")
                if userChoiceWallThrough == "0":
                    print("You step away from the wall.")
                elif userChoiceWallThrough == "1":
                    keepGoingKeepRuins = False
                    ancientLake()
                else:
                    print("I'm sorry, I didn't understand that. Please try a different command.")
        elif userChoice == "5":
            merchant(area)
        else:
            print("I'm sorry, I don't understand. Please try another command.")

def ancientLake():
    area = ancientLake1
    print("You step over the pile of rubble from the remains of the wall and follow the path down to the lake.")
    input("Press enter to continue")
    print("As you approach the lake, a woman emerges from the middle and approaches you")
    input("Press enter to continue")
    print("""{}: Brave adventurer, you have traveled far and faced many perils. I fear that if you continue with this quest,
what awaits you is far, far worse than what you have faced so far.""".format(area.npc.name))
    input("Press enter to continue")
    print("""{}: Do you know of what awaits you in the capitol? A mighty dragon has taken up residence there. None have survived his wrath.
If you choose to continue, I can aid you should you prove to be worthy of such assistance.""".format(area.npc.name))
    input("Press enter to continue")
    keepGoingLake = True
    while keepGoingLake:
        print("""What would you like to do?
0. Test worthiness
1. Menu
2. Return to Ruined Keep""")
        userChoiceLake = input("> ")
        if userChoiceLake == "0":
            if user.worthinessProven == False:
                print("{}: Brave adventurer, give me your hand. I will judge your worthiness.".format(area.npc.name))
                input("Press enter to continue")
                if user.enemiesSlain >= 20:
                    print("{}: {}, that is your name, correct? You have proven yourself worthy of my gift. Please accept that which I offer to you.".format(area.npc.name, user.name))
                else:
                    print("{}: I'm sorry, you are not worthy of my gift at this time. Please return to me when you have slain {} more foes.".format(area.npc.name, user.enemiesRemaining))
            elif user.worthinessProven == True and user.acceptedLakeGift == True:
                print("{}: {}, you have already proven your worthiness, please use my gift to aid with your adventure.".format(area.npc.name, user.name))
            elif user.worthinessProven == True and user.acceptedLakeGift == False:
                print("{}: {}, I urge you to reconsider your choice. My gift will prove highly valuable to you.".format(area.npc.name, user.name))
        elif userChoiceLake == "1":
            inGameMenu()
        elif userChoiceLake == "2":
            keepGoingLake = False
            keepRuins()
          

def ruinedCapitol():
    pass

def loadArea(progressCode):
    setLocation(user.progressCode)

