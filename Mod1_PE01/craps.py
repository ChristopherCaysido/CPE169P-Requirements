"""
File: craps.py

This module studies and plays the game of craps.
The play method in the Player class of the craps game plays an entire game without interaction 
with the user. Revise the Player class so that its user can make individual rolls of the dice 

1. Revise Player Class so its users can make individual rolls of the dice, view the results of
each roll.

2.)The Player class no longer accumulates a list of rolls, 
but saves the string representation of each roll after it is made
a

3.) Add new methods rollDice, getRollsCount, isWinner, and isLoser to the Player class. 
The last three methods allow the user to obtain the number of rolls and to determine whether 
there is a winner or a loser. 

The last two methods are associated with new Boolean instance variables. 


Two other instance variables track the number of rolls and the string representation of the most
recent roll. Another instance variable tracks whether or not the first roll has occurred. 
At instantiation, the roll, rollsCount, atStartup, winner, and loser variables are set to their 
appropriate initial values. All game logic is now in the rollDice method. 

This method rolls the dice once, 
updates the state of the Player object, 
and returns a tuple of the values of the dice for that roll. 

Include in the module the playOneGame and playManyGames functions, 
suitably updated for the new interface to the Player class.
Name: Christopher Nilo A. Caysido
"""
from die import Die
import sys
import time

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.stillPlaying = True
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = False #Represents 
        self.prompt = ""
        self.winner = False
        self.loser = False
    def getRollsCount(self):
        print("Current Roll Count: " + str(self.rollsCount))
    def isWinner(self):
            self.winner = True
            self.loser = False
            print("You win")
    def isLoser(self):
            self.loser = True
            self.winner = False
            print("You lose")
    def rollDice(self):
        self.roll = 0
        self.atStartup = False
        self.stillPlaying = True
        self.atStartup = True
        self.prompt = input("Welcome To Craps Dice Game, Would You Like to Play a Round? (y/n)")
        if self.prompt == 'y':
            self.die1.roll()
            self.die2.roll()
            (v1,v2) = (self.die1.getValue(),self.die2.getValue())
            self.roll = "Rolls: " + str(v1) + " & " + str(v2) + "Total: " + str(v1 + v2)
            initialValue = v1 + v2
            self.rollsCount = self.rollsCount + 1
            print(self.roll)
            self.getRollsCount()  
            if initialValue == (2,3,12):
                return self.isLoser()
            elif initialValue == (7,11):
                return self.isWinner()
            else:
                pass
        else:
            print("Good Bye")
            sys.exit()
        time.sleep(5)
        self.atStartup = False
        while(True):
            self.die1.roll()
            self.die2.roll()
            self.rollsCount = self.rollsCount + 1
            (v1,v2) = (self.die1.getValue(),self.die2.getValue())
            latestValue = v1+v2
            self.roll = "Rolls: " + str(v1) + " & " + str(v2) + "Total: " + str(v1 + v2)
            print(self.roll)
            self.getRollsCount()
            if latestValue == 7:
                return self.isLoser()
            elif latestValue == initialValue:
                return self.isWinner()
            else:
                pass
            time.sleep(5)
def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    youWin = player.rollDice()
    print(youWin)

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.rollDice()
        rolls = 0
        if player.winner:
            wins += 1
            winRolls += player.rollsCount
        elif player.loser:
            losses += 1
            lossRolls += player.rollsCount
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def oneGame():
    """Plays a number of games and prints statistics."""
    playOneGame()

def multiGame():
    number = int(input("Enter the number of games: "))
    playManyGames(number)


if __name__ == "__main__":
    oneGame()
    multiGame()