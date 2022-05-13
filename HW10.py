"""
Georgia Institute of Technology - CS1301
Homework 08 - Object Oriented Programming
"""

class Mario:
    def __init__(self,name):
        self.name = name
        self.lives = 3
        self.coins = 0
        self.isAlive = True
    
    def gainCoins(self,coin=5):
        self.coins += coin
        
        

    def loseLife(self):
        if self.lives > 0:
            self.lives -= 1
        if self.lives == 0:
            self.isAlive = False
            return
            
    
    def gainLife(self):
        if self.lives < 3 and self.lives > 0:
            self.lives += 1
        elif self.lives >= 3:
            self.coins += 10
        elif self.lives == 0:
            return

    def __str__(self):
        return f"Hi! I am {self.name}. I have {self.lives} lives left and {self.coins} coins."

    # the following method is provided to you
    def __eq__(self, other):
        return (self.name == other.name and
                self.lives == other.lives and
                self.coins == other.coins and
                self.isAlive == other.isAlive)

    # the following method is provided to you
    def __repr__(self):
        return f"Mario({self.name})"


##########################################################


class Bowser:
    def __init__(self,name):
        self.name = name
        self.lives = 5
        self.isAlive = True
    
    def loseLife(self):
        if self.lives > 0:
            self.lives -= 1
        if self.lives == 0:
            self.isAlive = False
            return

    def __str__(self):
        return f"Hi! I am {self.name} and I have {self.lives} lives left."

    # the following method is provided to you
    def __eq__(self, other):
        return (self.name == other.name and
                self.lives == other.lives and
                self.isAlive == other.isAlive)

    # the following method is provided to you
    def __repr__(self):
        return f"Bowser({self.name})"


##########################################################


class World:
    def __init__(self,name, bowser, characters = tuple() , isWon = False):
        self.name = name
        self.bowser = bowser
        self.characters = characters
        self.isWon = isWon
    
    def __str__(self):
        if self.isWon == False:
            return f"{self.name} has not been won yet."
        return f"{self.name} has been won!"

    def addChar(self, character):
        for x in self.characters:
            if character.name == x.name:
                return f"{character.name} already exists in {self.name}."
        else:
            self.characters += (character,)
    
    def removeChar(self,character):
        if character in self.characters:
            self.characters = list(self.characters)
            self.characters.remove(character)
            self.characters = tuple(self.characters)
        if len(self.characters) == 0:
            self.gameOver()
    
    def runInto(self,string,character):
        if string == "mushroom":
            character.gainLife()
        elif string == "goomba":
            character.loseLife()
            if character.lives == 0:
                self.removeChar(character)
        elif string == "coin":
            character.gainCoins()
        
    def fight(self,character1,character2, win):
        if win == False:
            character1.loseLife()
            if character1.lives == 0:
                self.removeChar(character1)
        elif win == True:
            character1.gainCoins(20)
            character2.loseLife()
            if character2.lives == 0:
                self.gameOver()
 

    def gameOver(self):
        if len(self.characters) == 0:
            print("Mario Team loses.")
        else:
            print("Mario Team wins!")




    # the following method is provided to you
    def __repr__(self):
        return f"World({self.name}, {self.bowser})"
