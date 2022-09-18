import random
from entities import Player
from entities import Gameboard
import os
import time


class Gamecore:
    def clear_window():
        os.system('cls' if os.name == 'nt' else 'clear')

    time.sleep(2)
    print("Greetings.")
    time.sleep(2)
    Player.print_start()
    player_one = Player(input("Player 1: What is your name?\n").capitalize(), 1)
    print("Welcome " + str(player_one) + ", to The Lord of The Rings: Front Commando Line!")
    player_two = Player(input("Player 2: And what is your name?\n").capitalize(), 2)
    print("Welcome " + str(player_two) + "!")
    # time.sleep(1)

    # print("Who will you choose to aid you in your quest for victory?")
    # time.sleep(2)
    # print("The creatures of Middle Earth, with eagles, balrogs, dwarves and orcs, among others?")
    # time.sleep(3)
    # print("The warriors of Star Wars with jedis and siths to name a few?")
    # time.sleep(2)
    # print("Or will you choose the mere politicians of Sweden, with Magdalena Andersson,\n"
    # "Ebba Busch and Jimmie Åkesson in the frontline, to squabble for your guidance?")
    # time.sleep(4)
    #one_choice = player_one.choose_team()
    #two_choice = player_two.choose_team()
    player_one.create_fighters("Midd")
    player_two.create_fighters("Midd")

    rules = input("Would you like to read about bombers, resurrectors and miners? y/n:\n").capitalize()
    while rules != "Y" and rules != "N":
        rules = input("Choose to view rules by typing Y or N for Yes or No.\n").capitalize()
    if rules == "Y":
        print("You will each have to choose one bomber, one resurrector and one miner among your fighters.\n"
              "The bomber will have the ability to arm an invisible bomb, once, in 1 location.\n"
            "The bomb cannot be disarmed or removed. Any opponent player entering that location will die.\n"
            "The resurrector is able to resurrect 1 dead fighter, once, by sacrificing themselves at a maousoleum. \n"
              "If the fighter to resurrect was your strongest fighter, and the stars align, something extra-ordinary might happen.\n"
            "The miner is the only fighter able to traverse mountains. The miner's ability is to build a tunnel through a mountain pass,\n"
              "which is the only way for other fighters to cross mountains. The miner can only build 1 tunnel per game.\n"
            "Abilities are used at the end of a turn, unless a battle has been fought.\n")
        input("Press Enter to continue and view " + player_one.name + "'s fighters. " + str(player_two) + " should not be watching.\n")
    else:
        input("Press Enter to see " + str(player_one) + "'s fighters. " + str(player_two) + " should not be watching.\n")

    player_one.view_fighters()
    player_one.choose_ability("bomber")
    player_one.choose_ability("resser")
    player_one.choose_ability("miner")
    print("Good. Screen will clear in 5 seconds. Switch seat with " + str(player_two) + ".")
    time.sleep(5)
    clear_window()
    print(player_one, "have chosen abilities. Your turn,", player_two, "!")

    input("Press Enter to see " + str(player_two) + "'s fighters...")
    player_two.view_fighters()
    player_two.choose_ability("bomber")
    player_two.choose_ability("resser")
    player_two.choose_ability("miner")
    print("Good. Screen will clear in 3 seconds. Switch seat again.")
    time.sleep(3)
    clear_window()
    print("You have both chosen abilities.")

    gameboard = Gameboard()
    gameboard.view_board(player_one)
    print(player_one.name + " starts at row 1. " + player_two.name + " starts at row 8.")

    player_one.choose_start_positions(gameboard)
    print("Screen will clear in 5 seconds. Switch seat with " + str(player_two) + ".")
    time.sleep(5)
    clear_window()
    gameboard.view_board(player_two)
    player_two.choose_start_positions(gameboard)
    clear_window()
    starting_player = random.randrange(1,3)
    input("Press Enter to start the game.")

    while player_one.hasLost == False and player_two.hasLost == False:
        clear_window()
        if starting_player == 1:
            print(player_one, "'s turn!")
        else:
            print(player_two, "'s turn!")
        Player.print_help()
        input("Press Enter to view the gameboard.\n")
        if starting_player == 1:
            gameboard.view_board(player_one)
        else:
            gameboard.view_board(player_two)
        input_fighter = input("Enter fighter:\n")
        if starting_player == 1:
            player_one.interpretor(input_fighter, gameboard)
        else:
            player_two.interpretor(input_fighter, gameboard)
        if starting_player == 1:
            starting_player = 2
        else:
            starting_player = 1



    print("The game is over.")
    if player_one.hasLost:
        print(player_two.name + " has won!")
    else:
        print(player_one.name + " has won!")


