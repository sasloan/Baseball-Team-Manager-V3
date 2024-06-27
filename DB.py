# Use a file named db to store the two functions that read from and write to the file that stores the data. 
# These functions should use the same names used in the previous project. The function that reads the file 
# does not use a parameter and returns a lineup object which holds the player objects that are created when 
# the data is read from the given players.txt file. A lineup object is used as the parameter for the function 
# that writes the data to the file. 


import csv
import pickle
from Objects import *

FILENAME = 'players.txt'

def readCSV():
    try:

        with open(FILENAME, 'r', newline="") as file:
            reader_object = csv.reader(file)
        
            lineup = Lineup()

            for player in reader_object:
                first_name = player[0]
                last_name = player[1]
                position = player[2]
                at_bats = player[3]
                hits = player[4]

                player = Player(first_name, last_name, position, at_bats, hits)

                lineup.addPlayer(player)

            return lineup


    except FileNotFoundError as e:
        print(type(e), e)
        print("The", FILENAME, " file could not be found")
        return None
    except Exception as e:
        print(type(e), e)
        print("This error occured while reading from the CSV file")
        return None

def writeCSV(player_list):
    with open(FILENAME, 'w', newline="") as file: 
        for player in player_list:
            file.write(player.getFirstName() + ",")
            file.write(player.getLastName() + ",")
            file.write(player.getPosition() + ",")
            file.write(str(player.getAtBats()) + ",")
            file.write(str(player.getHits()) + "\n")



