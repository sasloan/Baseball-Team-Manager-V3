# Sebastian Sloan
# Project 3 
# November 19, 2023 
# update project with new material learned over the past 12 weeks

# Use a file named ui to store the code for the user interface. This is the existing code from the main module in projects #1 and #2. 
# Rename the existing module and refactor the code to use a Lineup object instead of a list of dictionaries (project #2) or a list of 
# lists (project #1). Modify the code to separately ask the user for both the first name and last so that the two inputs can be used 
# when creating a player object.


import DB
from datetime import date
import datetime
from Objects import *

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS: ")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print('+' * 50) 
    print()

def display_lineup(player_list):

    print("   Player\t\t\t\tPOS\tAB\tH\tAVG")
    print('-' * 100)

    for player in player_list:
        print(f"{player_list.getLineupNumber()}  {player.getFullName()} \t\t\t {player.getPosition()}\t{player.getAtBats()}\t{player.getHits()}\t{player.getBattingAverage()}")
    print()

def add_player(player_list):

    positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

    first_name = input("Please enter players First Name: ")
    last_name = input("Please enter players Last Name: ")
    position = input("Please enter players position: ")

    while position not in positions:
        print(f"'{position}' is not a valid position, please check the list again and re-enter a valid position.\n")
        print(positions)
        position = input("Position: ")
        print()

    at_bats = input("Please enter players At Bat: ")

    if at_bats.isdigit() == False:
        print("You must enter a positive number, please try again")
        at_bats = input("At Bats: ")
        print()
    elif float(at_bats) < 0:
        print("You must enter a positive number, please try again")
        at_bats = input("At Bats: ")
        print()

    hits = input("Please enter players Hits: ")
    print()

    if hits.isdigit() == False:
        print("You must enter a positive number, please try again")
        hits = input("Hits: ")
        print()

    elif float(hits) > float(at_bats):
        print("This number is not valid, your 'At Bats' score must be higher.")
        hits = input("Hits: ")
        print()

    elif float(hits) < 0:
        print("You must enter a positive number, please try again")
        hits = input("Hits: ")
        print()


    player = Player(first_name, last_name, position, at_bats, hits)

    player_list.addPlayer(player)
    DB.writeCSV(player_list)
    print()

def remove_player(player_list):

    player_to_remove = input("Enter a lineup number to remove: ")

    if str(player_to_remove) in player_list.getLineupNumber():
        player_list.removePlayer(player_to_remove)
        DB.writeCSV(player_list)
        print()

    else:
        print(f"'{player_to_remove}' is not a valid player lineup number, please try again. ")
        print()


def move_player(player_list):

    current_player = input("Enter a current lineup number to move: ")
    new_player = input("Enter new lineup number to move the player to: ")

    if current_player in player_list.getLineupNumber():
        player_list.MovePlayer(current_player, new_player)
        DB.writeCSV(player_list)
        print()
    else:
        print(f"'{current_player}' or '{new_player}' is not a valid player lineup number, please try again. ")
        print()    


def edit_player_position(player_list):

    positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

    player = input("Please enter the players Lineup number who's position you wish to edit: ")

    if player in player_list.getLineupNumber():
        player_to_edit = player_list.getPlayer(player)
        new_position = input("Please enter the new position for the player: ")
        if new_position in positions:
            player_to_edit.__position = new_position
            DB.writeCSV(player_list)
        else:
            print(f"'{new_position}' is not a valid position.")
            print("please select option '5' again and enter one of these positions")
            print(positions)
            print()
    else:
        print("Sorry that player does not exist, please try again.")
        print()
                
def edit_player_stats(player_list):

    line_up_number = input("Enter a lineup number to edit: ")

    if line_up_number in player_list.getLineupNumber():
        player_to_edit = player_list.getPlayer(line_up_number)
        print(f"You selected {player_to_edit.getFullName()}")
        print(f"At Bat = {player_to_edit.getAtBat()}")
        print(f"Hits = {player_to_edit.getHits()}") 
        print()
        which_stat = input("please type '1' to edit At Bat and '2' to edit Hits: ")
        if which_stat == '1':
            new_at_bat = input("Please enter a new 'At Bat' stat: ")
            if int(new_at_bat):
                player_to_edit.__at_bats = new_at_bat
                DB.writeCSV(player_list)
                print(f"player {player_to_edit.getFullName()} has had their 'At Bat' Status updated.")
                print("Please run option '6' again to edit another stat.")
                print()
            else:
                print(f"{which_stat} is not a valid option, please exit and run option '6' again.")
        elif which_stat == '2':
            new_hits = input("Please enter a new 'Hit' stat: ")
            if new_hits < float(player_to_edit.getHits()):
                if int(new_hits):
                    player_to_edit.__hits = new_hits
                    DB.writeCSV(player_list)
                    print(f"player {player_to_edit.getFullName()} has had their 'Hits' status updated.")
                    print("Please run option '6' again to edit another stat.")
                    print()
                else:
                    print(f"{which_stat} is not a valid option, please exit and run option '6' again.")
            else:
                print("The 'Hits' Status cannot be larger than the 'At Bat' Status, please update the 'At Bat' Status first.")
                print("Please exit and re-run option 6.")
        else:
            print(f"{which_stat} is not a valid option, please exit and run option '5' again.")


def main():
    print('-' * 50) 
    header = "Baseball Team Manager"
    print(header.center(50))
    print()

    date_format = '%Y-%m-%d'

    print(f"CURRENT DATE:    {date.today()}")

    game_date = input("GAME DATE:    ")

    try:

        game_day = datetime.datetime.strptime(game_date, date_format)
        today = datetime.datetime.strptime(str(date.today()), date_format)

        time_to_next_game = game_day - today
        print(f"DAYS UNTIL GAME: {time_to_next_game.days}")

    except ValueError:

        print("Incorrect data format, should be YYYY-MM-DD")
 
    print()
    display_menu()

    players = DB.readCSV()

    while True:
        command = input("Menu option: ")
        if command == "1":
            display_lineup(players)
        elif command == "2":
            add_player(players)
        elif command == "3":
            remove_player(players)
        elif command == "4":
            move_player(players)
        elif command == "5":
            edit_player_position(players)
        elif command == "6":
            edit_player_stats(players)
        elif command == "7":
            print("Bye!")
            break
        else:
            print("The command you inputted is not a valid command please try again.")
            display_menu()
            print()
            command = input("Menu option: ")


if __name__ == "__main__":
    main()
