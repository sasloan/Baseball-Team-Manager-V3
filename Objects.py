# Use a file named objects to store the code for the Player and Lineup classes.

# Use a Player class that provides attributes that store the first name, last name, position, at bats, and hits for a player. 
# The class constructor should use these five attributes as parameters. This class should also provide a method that returns 
# the full name of a player and a method that returns the batting average for a player.


class Player:
    def __init__(self, first_name = "", last_name = "", position = "", at_bats = 0, hits = 0):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__at_bats = at_bats
        self.__hits = hits

    def getFirstName(self):
        return self.__first_name
    
    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getLastName(self):
        return self.__last_name
    
    def setLastName(self, last_name):
        self.__last_name = last_name

    def getPosition(self):
        return self.__position
    
    def setPosition(self, position):
        self.__position = position

    def getAtBats(self):
        return self.__at_bats
    
    def setAtBats(self, at_bats):
        self.__at_bats = at_bats

    def getHits(self):
        return self.__hits
    
    def setHits(self, hits):
        self.__hits = hits

    def getFullName(self):
        return self.__first_name + " " + self.__last_name
    
    def getBattingAverage(self):
        return int(self.__at_bats) / int(self.__hits)

# Use a Lineup class to store the lineup for the team as a private list attribute. 
# This class must include the following methods (with parameters) to modify the private list 
# attribute:  add player (player object), remove player (lineup number), get player(lineup number), 
# and move player(old lineup number, new lineup number).  The add method will add a new player to the end of the list. 
# The remove and get methods require the lineup location of the targeted player as a parameter and both methods will 
# return the player object at the specified location; the only difference is that the get method will not delete the 
# object from the list attribute. In addition the class must include an iterator so that the lineup object can be used in a for loop.
class Lineup:
    def __init__(self):
        self.__lineup = []

    def addPlayer(self, player):
        self.__lineup.append(player)

    def removePlayer(self, player):
        self.__lineup_number -= self.__lineup[player]
        return self.__lineup.pop(player)

    def getPlayer(self, lineup_number):
        for player in self:
            if player.__lineup_number == lineup_number:
                return player
    
    def movePlayer(self, old_lineup, new_lineup):
        return self.__lineup.insert(int(old_lineup),self.__lineup.pop(self.__lineup.index(new_lineup)))
    
    def getLineupNumber(self): 
        return self.__index + 1

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineup) - 1:
            raise StopIteration
        
        self.__index += 1
        card = self.__lineup[self.__index]
        return card