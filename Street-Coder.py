# 1 class at a minimum
# functions
# for loops
# while loops
# list
# variables
# adding/removing aspects about your class
# the ability to exit the game
# the ability to replay the game
# clean code

# aim for mvp first

import os
import random


Startoption = input("Are you ready???? (Yes or No) ")

def QuitGame1():
    print("""
    
    
    WoW. Thanks
    
    
    """)


def StartGame():
    Startoption
    if Startoption == "Yes":
        Greeting()
    elif Startoption == "No":
        QuitGame1()


def Greeting():
    print("""
    ====================================
        
         Welcome to StreetCoder I
         
    
    
    """)

def ChoseRyu():
    print("""===========================================

2. Ash, A 10 year old boy who is just about to start his Quest after a late start.

3. Luffy, After eating the Gum-Gum fruit and setting out on his journey to become The Pirate King. He will stop at nothing to achieve his goal.

4. Mario, The classic hero we all know equipped with a Fire Flower.

5. Joe, After his fight in FlatIron, now his hobby is let out some steam by attacking his students with his Keyboard Shortcuts.""")

def ChoseAsh():
    print("""===========================================
1. Ryu, Bringing some his iconic moveset, hes here just to have his music looping in your head.

3. Luffy, After eating the Gum-Gum fruit and setting out on his journey to become The Pirate King. He will stop at nothing to achieve his goal.

4. Mario, The classic hero we all know equipped with a Fire Flower.

5. Joe, After his fight in FlatIron, now his hobby is let out some steam by attacking his students with his Keyboard Shortcuts. """)

def ChoseLuffy():
    print("""===========================================
1. Ryu, Bringing some his iconic moveset, hes here just to have his music looping in your head.

2. Ash, A 10 year old boy who is just about to start his Quest after a late start.

4. Mario, The classic hero we all know equipped with a Fire Flower.

5. Joe, After his fight in FlatIron, now his hobby is let out some steam by attacking his students with his Keyboard Shortcuts.""") 
def ChoseMario():
    print("""===========================================
1. Ryu, Bringing some his iconic moveset, hes here just to have his music looping in your head.

2. Ash, A 10 year old boy who is just about to start his Quest after a late start.

3. Luffy, After eating the Gum-Gum fruit and setting out on his journey to become The Pirate King. He will stop at nothing to achieve his goal.

5. Joe, After his fight in FlatIron, now his hobby is let out some steam by attacking his students with his Keyboard Shortcuts.""")

def ChoseJoe():
    print("""===========================================
1. Ryu, Bringing some his iconic moveset, hes here just to have his music looping in your head.

2. Ash, A 10 year old boy who is just about to start his Quest after a late start.

3. Luffy, After eating the Gum-Gum fruit and setting out on his journey to become The Pirate King. He will stop at nothing to achieve his goal.

4. Mario, The classic hero we all know equipped with a Fire Flower.""")

def RyuMoves():
    print("""
    Weapon: Martial Arts
    1. Hadouken 
    2. Sweep Kick 
    """)
def Ashmoves():
    print(""" 
    Weapon:Pikachu 
    1.Thunder Shock
    2.Tackle
    """)
def LuffyMoves():
    print("""
    Weapon: Devil Fruit Powers
    1.Gum-Gum Pistol
    2.Gum-Gum Whip
    """)
def MarioMoves():
    print("""
    Weapon: Fire Flower
    1.Fireball
    2.Stomp
    """)
def JoeMoves():
    print("""
    Weapon: Keyboard
    1.Shortcuts
    2.Bad Pun
    """)


# self, name, weapon, FAir, FDamage, Dair, DDamage, Health):
endgame = ["""
===========================================
You Win
===========================================""","""
===========================================
Game Over
==========================================="""]
class Characters:
    def __init__(self, name, weapon, FAir, FDamage, Dair, DDamage, Health):
        self.name = name
        self.weapon = weapon
        self.FAir = FAir
        self.FDamage = FDamage
        self.Dair = Dair
        self.DDamage = DDamage
        self.Health = Health
    def Youmidattack(self,villain):
        villain.Health = villain.Health - self.FDamage
    def YoulowAttack(self,villain):
        villain.Health = villain.Health - self.DDamage
    def EnemyMidAttack(self,You):
        You.Health = You.Health - self.FDamage
    def EnemyLowAttack(self,You):
        You.Health = You.Health - self.DDamage
    def __str__(self):
        return (f"""
        {self.Name}'s is {self.Health}
        Weapon: {self.weapon}
        1. {self.FAir} 
        2. {self.DAir} 
            
            """)






def Replaygame():

    StartGame()


    print("""
    ============================================
    Your Fighters
    ============================================""")
    YourCharacter = int(input(""" 
    1. Ryu, Bringing some his iconic moveset, hes here just to have his music looping in your head.

    2. Ash, A 10 year old boy who is just about to start his Quest after a late start.

    3. Luffy, After eating the Gum-Gum fruit and setting out on his journey to become The Pirate King. He will stop at nothing to achieve his goal.

    4. Mario, The classic hero we all know equipped with a Fire Flower.

    5. Joe, After his fight in FlatIron, now his hobby is let out some steam by attacking his students with his Keyboard Shortcuts.
    ===========================================
    Select Your Fighter by Fighter Number  
    """))



    if YourCharacter == 1:
        Ryu = Characters("Ryu","Fists","Haudoken",20,"Sweep Kick",15,150)
        You = Ryu
        RyuMoves()
        ChoseRyu()
    if YourCharacter == 2:
        Ash = Characters("Ash","Pikachu","Thunder Shock",50,"Tackle",1,30)
        You = Ash
        Ashmoves()
        ChoseAsh()
    if YourCharacter == 3:
        Luffy = Characters("Luffy","Gum-Gum Powers","Gum-Gum Pistol",20,"Gum-Gum Whip",20,130)
        You = Luffy
        LuffyMoves()
        ChoseLuffy()
    if YourCharacter == 4:
        Mario = Characters("Mario","Fire Flower","Stomp",15,"Fireball",40,100)
        You = Mario
        MarioMoves()
        ChoseMario()
    if YourCharacter == 5:
        Joe = Characters("Joe","Keyboard","Shortcuts",10,"Bad Pun",12,90)
        You = Joe
        JoeMoves()
        ChoseJoe()
        


    Opponent = int(input("""
    ===========================================
    Choose your opponet
    ===========================================
    """))


    if Opponent == 1:
        Ryu = Characters("Ryu","Martial Arts","Haudoken",20,"Sweep Kick",15,150)
        villain = Ryu
        RyuMoves()
    
    if Opponent == 2:
        Ash = Characters("Ash","Pikachu","Thunder Shock",50,"Tackle",1,30)
        villain = Ash
        Ashmoves()

    if Opponent == 3:
        Luffy = Characters("Luffy","Gum-Gum Powers","Gum-Gum Pistol",20,"Gum-Gum Whip",20,130)
        villain = Luffy
        LuffyMoves()

    if Opponent == 4:
        Mario = Characters("Mario","Fire Flower","Stomp",15,"Fireball",40,100)
        villain = Mario
        MarioMoves()

    if Opponent == 5:
        Joe = Characters("Joe","Keyboard","Shortcuts",10,"Bad Pun",12,90)
        villain = Joe
        JoeMoves()

    print(You.name, "VS.",villain.name)


    print("""===========================================
                
                
                
                    !!!!FIGHT!!!!



    ===========================================""")
    while True:
        if You.Health >=0 and villain.Health >= 0:
            YourCharacter
            Choice = int(input(""" Choose your Attack Number
            """))
            Ai = random.randint(1,2)
            if Choice == 1:
                print(You.name,"uses",You.FAir)
                You.Youmidattack(villain)
                print(villain.name,villain.Health)
                if Ai == 1:
                    print(villain.name,"uses",villain.FAir)
                    villain.EnemyMidAttack(You)
                    print(You.name,You.Health)
                elif Ai == 2:
                    print(villain.name,"uses",villain.Dair)
                    villain.EnemyLowAttack(You)
                    print(You.name,You.Health)
                #  villain attacks back   villain.villainAttackFunction(You)
            elif Choice == 2:
                print(You.name,"uses",You.Dair)
                You.YoulowAttack(villain)
                print(villain.name,villain.Health)
                if Ai == 1:
                    print(villain.name,"uses",villain.FAir)
                    villain.EnemyMidAttack(You)
                    print(You.name,You.Health)
                elif Ai == 2:
                    print(villain.name,"uses",villain.Dair)
                    villain.EnemyLowAttack(You)
                    print(You.name,You.Health)
               #  villain attacks back   villain.villainAttackFunction(You)
            else:
                print("Please Choose a Move number 1 or 2")
        else:
            if You.Health > villain.Health:
                print(endgame[0])
                Startoption = input("Do you want to play again? Yes/No")
                if Startoption == "Yes":
                    Replaygame()
                else:
                    QuitGame1()
            if You.Health < villain.Health:
                print(endgame[1])
                Startoption = input("Do you want to play again? Yes/No")
                if Startoption == "Yes":
                    Replaygame()            
                else:
                    QuitGame1()


Replaygame()




























