import random
import getpass
import os
import time

class Player:
    def __init__(self, input_name, input_no):
        self.name = input_name
        self.number = input_no
        self.hasLost = False
        self.fighters = []
        self.fighters_left = 8

    def __str__(self):
        return f'{self.name}'

    def update_life(self, change):
        self.fighters_left += change
        if self.fighters_left == 0:
            self.hasLost = True

    def print_start():
        choice = input("Is this your first time playing The Lord of The Rings: Front Commando Line? Y/N\n").capitalize()
        if choice == "Y":
            print("Please adjust this window so that the following line is on the same command line as this text: -------------------------------------------------------------------\n")
            input("Press Enter to continue.\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            print("The Lord of The Rings: Front Commando Line is a strategic, turn-based game on a table of 8 x 12 randomly placed locations.\n"
                  "2 players start at opposite side of the table, each with eight fighters from The Lord of The Rings.\n"
                  "The fighters have strength ranged from 8 to 1.\n"
                  "In order to win a player must beat all of the opponent's fighters. A fighter with higher strength beats a fighter with lower strength.\n"
                  "If two fighters with same strength confront each other, they both die.\n"
                  "You cannot see who your opponents fighters are until you have confronted them.\n\n"
                  "Three of your fighters will have certain abilities. One will act as miner, one as a bomber and one as a resurrector.\n"
                  "The bomber can arm 1 invisible bomb in any location. Any opponent fighter entering that location will die.\n\n"
                "The resurrector can bring back a dead fighter by sacrificing themselves at a mausoleum. There are two randomly placed mausoleums in each game.\n"
                "If you attempt to resurrect your strongest fighter, and the stars align, something extra-ordinary might happen.\n\n"
                "Only the miner can traverse mountains. The miner's ability is to build a tunnel through a mountain pass.\n"
                "Tunnels allow all fighters, opponents as well, to pass. The miner can only build one tunnel per game.\n"
                  "When a tunnel is built it is in view for both players.\n\n"
                "Abilities can be used at the end of a turn, after movement. \n"
                  "Confrontation will not reveal if a fighter had an ability.\n\n"
                  "The different landscapes are forests, hills, plains, mountains and water. From Plains and Hills you can move 2 tiles in one turn.\n"
                  "Water can not be passed or entered, and mountains can only be entered by a miner or after building a tunnel through.\n"
                  "You can move diagonally, unless obstructed.\n\n"
                  #"Fighters can be chosen from three set of worlds. They are Middle Earth, Star Wars, and swedish politicians.\n"
                  "Anytime you are asked to choose a fighter, it's only necessary to provide the first 4 characters.\n"
                  "Choosing to navigate with Elrond for example, only requires you to type Elro.\n"
                  #"Player One plays with creatures of light, and Player Two with creatures of darkness. Choosing middle earth with Player One will not yield the same set of fighters as for Player Two.\n"
                  #"All teams have the same set of strength.\n\n"
                    )
            input("Press Enter to begin the game.")

    def print_help():
        print("Navigate by typing the name of a fighter followed by a new coordinate. Example: Morgul-Rat (or simply morg), 2c.\n"
            "You can move diagonally (unless obstructed).\n"
            "To see the speed of your fighter's landscape, type speed.\n"
            "To switch to another fighter, type switch.\n"
            "Type info to see who has abilities and who of your fighters are dead.\n"
            "To view this again, type Help.")

    def choose_team(self):
        choice = ""
        while choice[0:4] != "Midd" and choice[0:4] != "Star" and choice[0:4] != "Poli":
            choice = input(str(self) + ", type middle earth, star wars or politicians to choose your fighters:\n").capitalize()
            if choice[0:4] != "Midd" and choice[0:4] != "Star" and choice[0:4] != "Poli":
                choice = input("Did you misspell? Choose by typing either Middle Earth, Star Wars or Politicians.\n").capitalize()
        if self.number == 1:
            print("Excellent. " + str(self) + " has chosen " + choice + " as fighters!")
        else:
            print("Good. " + str(self) + " has chosen " + choice + " as fighters!")
        return choice

    def create_fighters(self, input_choice):
        lst = []
        if input_choice[0:4] == "Midd" and self.number == 1:
            fighter1 = Fighter("Eagle", 2561, "too lazy to throw the ring", 8, self)
            fighter2 = Fighter("Elrond", "unknown age", "a wise cracker", 7, self)
            fighter3 = Fighter("Numenor", "eternal", "with whole lot of glory", 6, self,
                                "After a glorious fight, Numenor sheaths his weapon and whistles loudly."
                                "A horse swiftly approaches, carrying plenty of wine, the best wine of the north. Aaaahhh.\n" \
                                  , "The enemy close in fast. So fast, Numenor doesn't even have time to ready his sword. \n" \
                                "He doesn't feel the heavy blow. Blackness quickly fills his consciousness,\n" \
                                "while his body falls on the ground with a thud.")
            fighter4 = Fighter("Arwen", "very old", "and likes to flood areas", 5, self, "Quick as a diving eagle she draws"
                                "her katana. With a jump attack from higher ground, the enemy stood no chance.",
                               "As Arwen approaches her enemy, they turn to face her. With sparkling eyes they"
                               "produce a\n bow, drawn to maximum, from their robes. She watches as their hand loosen"
                               "its grip on the arrow. There are no rivers to help her here.\n")
            fighter5 = Fighter("Gimli", 42, "apparently sprung from a hole in the ground", 4, self)
            fighter6 = Fighter("Theoden", 58, "dark has been his dreams of late", 3, self)
            fighter7 = Fighter("Eowyn", 29, "and founder of the Aragorn fan-club", 2, self)
            fighter8 = Fighter("Pippin", 27, "an honest fool", 1, self)
            lst.extend([fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8])
            self.fighters = lst
        elif input_choice[0:4] == "Midd" and self.number == 2:
            fighter1 = Fighter("Balrog", "eternal", "of shadow and flame", 8, self)
            fighter2 = Fighter("She-Lob", "unknown age", "an abomination - now with hunger", 7, self)
            fighter3 = Fighter("Saruman", "very old", "and abandoned reason for madness", 6, self)
            fighter4 = Fighter("Cave Troll", "actually quite young", "and not known for his hospitality", 5, self)
            fighter5 = Fighter("Uruk-hai", "old enough to rip flesh", "once taken by the dark powers", 4, self)
            fighter6 = Fighter("Morgul-rat", 37, "a mere leg-eater", 3, self)
            fighter7 = Fighter("Gollum", "500+", "should never have gone fishing", 2, self)
            fighter8 = Fighter("Denethor", 53, "Steward!", 1, self)
            lst.extend([fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8])
            self.fighters = lst
        elif input_choice[0:4] == "Poli" and self.number == 1:
            fighter1 = Fighter("Håkan Juholt", 57, "a good-hearted Wario", 8, self)
            fighter2 = Fighter("Ebba Busch", "forever 21", "christian home-stealer", 7, self)
            fighter3 = Fighter("Greta Thunberg", "too young for this team", "Procurer of vegetables", 6, self)
            fighter4 = Fighter("Bo Lundgren", 78, "lest we forget.", 5, self)
            fighter5 = Fighter("Anders Borg", 57, "appreciates the good life", 4, self)
            fighter6 = Fighter("Nooshi Dadgostar", 31, "secret founder of stoppapressarna.nu", 3, self)
            fighter7 = Fighter("Ulf Lundell", "old in his cabin", "Once the real force of Sweden", 2, self)
            fighter8 = Fighter("Per Bolund", 52, "should be on player 2's team", 1, self)
            lst.extend([fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8])
            self.fighters = lst
        elif input_choice[0:4] == "Poli" and self.number == 2:
            fighter1 = Fighter("Lars Ohly", 63, "mother Russia will rise again", 8, self)
            fighter2 = Fighter("Jimmie Åkesson", 45, "for the glory of the empire", 7, self)
            fighter3 = Fighter("Jonas Sjöstedt", "vampire", "unquenchable thirst", 6, self)
            fighter4 = Fighter("Märta Stenevi", "older than life itself", "More food-mopeds for the climate", 5, self)
            fighter5 = Fighter("Annie Lööf", "undead", "extreme lust for power", 4, self)
            fighter6 = Fighter("Gudrun Schyman", "ancient", "pissening", 3, self)
            fighter7 = Fighter("Ulf Kristersson", 52, "dull but intoxicating", 2, self)
            fighter8 = Fighter("Stefan Löfven", 58, "wannabe harbinger of doom", 1, self)
            lst.extend([fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8])
            self.fighters = lst

    def choose_ability(self, input_ability):
        chosen_ability = False
        while chosen_ability == False:
            chosen = input(self.name + ", type the name of your " + input_ability + ":\n")
            for i in range(8):
                if self.fighters[i].name[0:4] == chosen[0:4].title():
                    if self.fighters[i].resser == True or self.fighters[i].miner == True or self.fighters[i].bomber == True:
                        print(self.fighters[i].name + " already has an ability!")
                    else:
                        if input_ability == "bomber":
                            self.fighters[i].bomber = True
                        elif input_ability == "resser":
                            self.fighters[i].resser = True
                        elif input_ability == "miner":
                            self.fighters[i].miner = True
                        chosen_ability = True
                        print(self.fighters[i].name + " is your", input_ability,"!")

    def view_fighters(self):
        print(self.name + ", your fighters are:")
        for i in range(8):
            print(str(self.fighters[i]))
        print("\n")

    def coord_letter_gen(self, input):
        match input.capitalize():
            case "A":
                return 0
            case "B":
                return 1
            case "C":
                return 2
            case "D":
                return 3
            case "E":
                return 4
            case "F":
                return 5
            case "G":
                return 6
            case "H":
                return 7
            case "I":
                return 8
            case "J":
                return 9
            case "K":
                return 10
            case "L":
                return 11
            case default:
                return 0

    def choose_start_positions(self, input_board):
        gameboard = input_board
        number = 0
        if self.number == 1:
            number = 0
        elif self.number == 2:
            number = 7
        print(self,", type the starting position column letter for:")
        for i in range(8):
            text = self.fighters[i].name + ", strength ("+ str(self.fighters[i].strength) + ")"
            text2 = (" and a bomber" if self.fighters[i].bomber else " and a resurrector" if self.fighters[i].resser else " and a miner" if self.fighters[i].miner else "")
            letter = input(text + text2 + ":\n")
            letter = letter.capitalize()
            while letter not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L") or gameboard.square[number][self.coord_letter_gen(letter)].has_fighter == True:
                if letter not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"):
                    letter = input("Letter must be in range A-L. Enter letter for " + self.fighters[i].name + ", strength: ("+ str(self.fighters[i].strength) + "):\n")
                    letter = letter.capitalize()
                else:
                    letter = input("That position is already taken. Enter new position for " + self.fighters[i].name + ":\n")
                    letter = letter.capitalize()
            self.fighters[i].position = (str(number + 1) + letter)
            gameboard.square[number][self.coord_letter_gen(letter)].has_fighter = True
            gameboard.square[number][self.coord_letter_gen(letter)].fighter = self.fighters[i]
            print(self.fighters[i].name, "starts at", self.fighters[i].position, "!")

    def interpretor(self, string, board, string2=""):
        if string.capitalize() == "Help" or string2.capitalize() == "Help":
            Player.print_help()
            input_fighter = input("Enter fighter:\n")
            self.interpretor(input_fighter, board)

        elif string.capitalize() == "Info":
            self.view_fighters()
            input_fighter = input("Enter fighter:\n")
            self.interpretor(input_fighter, board)

        elif len(string2) == 0:
            input_action = input("Enter second argument:\n")
            self.interpretor(string, board, input_action)

        elif string2.capitalize() == "Switch":
            input_fighter = input("Enter new fighter:\n")
            self.interpretor(input_fighter, board)

        elif self.has_fighter_name(string) and len(string2) > 0:
            selected_fighter = self.get_fighter(string)
            if string2.capitalize() == "Speed":
                print(selected_fighter.name + "'s position is " + selected_fighter.position + ".")
                if board.square[int(selected_fighter.position[0]) - 1][self.coord_letter_gen(selected_fighter.position[1])].diag:
                    print("You can move diagonally from this square.")
                print("Current square has " + str(board.square[int(selected_fighter.position[0]) - 1][self.coord_letter_gen(selected_fighter.position[1])].speed) + " speed.")
                input_action = input("Enter new coordinates for " + selected_fighter.name + " or type switch to switch fighter:\n")
                self.interpretor(string, board, input_action)
            elif string2[0] in ("1", "2", "3", "4", "5", "6", "7", "8") and string2[1].capitalize() in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L") and len(string2) == 2:
                self.move_fighter(selected_fighter, board, string2)
            else:
                print("That's an invalid argument. 1a, 2B, 8C, 7d etc, are valid coordinates. Or type speed, or switch or help.")
                input_action = input("Enter second argument for " + selected_fighter.name + ":\n")
                self.interpretor(string, board, input_action)
        else:
            print("Type a fighters name to select it or info to list all your fighters. Or type help.")
            input_fighter = input("Enter fighter:\n")
            self.interpretor(input_fighter, board)


    def has_fighter_name(self, string):
        for i in range(8):
            if self.fighters[i].name[0:4] == string[0:4].title() and self.fighters[i].alive:
                return True
            elif self.fighters[i].name[0:4] == string[0:4].title() and self.fighters[i].alive == False:
                print(self.fighters[i].name + " is dead...")
                return False
        print("Found no fighter with that name.")
        return False

    def get_fighter(self, input_string):
        for i in range(8):
            if self.fighters[i].name[0:4] == input_string[0:4].title():
                return self.fighters[i]
        else:
            print("No fighter found!")
            return ""

    def move_fighter(self, input_fighter, input_board, input_coord):
        next_step_number = 0
        next_step_letter = 0
        old_number = (int(input_fighter.position[0]) - 1)
        old_letter = self.coord_letter_gen(input_fighter.position[1])
        new_number = (int(input_coord[0])-1)
        new_letter = self.coord_letter_gen(input_coord[1])
        diff_number = abs(old_number - new_number)
        diff_letter = abs(old_letter - new_letter)
        new_loc = input_board.square[new_number][new_letter]
        old_loc = input_board.square[old_number][old_letter]
        middle_loc = None
        speed = old_loc.speed
        diag_move = False
        two_step_move = False

        if diff_number == 2 and diff_letter == 2:
            diag_move = True

        if (diff_number == 2 and diff_letter == 0) or (diff_number == 0 and diff_letter == 2) or (diag_move):
            two_step_move = True

        if old_loc.kind == "mountain" and input_fighter.miner:
            speed = 1

        if diff_number > speed or diff_letter > speed:
            print("         Current location only allows " + str(old_loc.speed) + " square movement.")

        elif (diff_number == 2 and diff_letter == 1) or (diff_number == 1 and diff_letter == 2):
            print("         You cannot move like a chess horse, since you cannot specify your route.\n"
                  "         There is no way to know if you are restricted or not.")
        else:
            if two_step_move:
                if (old_number - new_number) < 0:
                    next_step_number = (new_number - 1)
                elif (old_number - new_number) > 0:
                    next_step_number = (new_number + 1)
                else:
                    next_step_number = old_number
                if (old_letter - new_letter) < 0:
                    next_step_letter = (new_letter - 1)
                elif (old_letter - new_letter) > 0:
                    next_step_letter = (new_letter + 1)
                else:
                    next_step_letter = old_letter
                middle_loc = input_board.square[next_step_number][next_step_letter]

            if two_step_move and middle_loc.has_fighter:
                print("         You can't pass over a fighter.")

            elif new_loc.has_fighter and new_loc.fighter.player.number == self.number:
                print("         You already have a fighter standing there.")

            elif (two_step_move and middle_loc.kind == "mountain" and input_fighter.miner == False and middle_loc.has_tunnel == False) or (new_loc.kind == "mountain" and input_fighter.miner == False and new_loc.has_tunnel == False):
                print("         You have to use a miner to navigate mountains without a tunnel!")

            elif (two_step_move and middle_loc.kind == "water") or new_loc.kind == "water":
                print("         No fighter can traverse water.")

            elif new_loc == old_loc:
                print("         That's your current position!")

            elif (self.number == 2 and new_loc.has_bomb1) or (self.number == 2 and two_step_move and middle_loc.has_bomb1):
                input_fighter.alive = False
                self.update_life(-1)
                old_loc.has_fighter = False
                old_loc.fighter = None
                if two_step_move:
                    middle_loc.has_bomb1 = False
                else:
                    new_loc.has_bomb1 = False
                print("An unfortunate move. The enemy had placed a powerful explosive device in this location.\n"
                      "It detonates as you enter, the blast resonating through the surrounding area. \n"
                      "The once rich flora and fauna is left in ruin, and so is your body. Only pieces of your spirit lingers behind.\n"
                      "Perhaps, if fate is on your side, someone might bring you back... for a price.")
                input("Your turn is over. Press Enter to start the next turn.\n")
                return

            elif (self.number == 1 and new_loc.has_bomb2) or (self.number == 1 and two_step_move and middle_loc.has_bomb2):
                input_fighter.alive = False
                self.update_life(-1)
                old_loc.has_fighter = False
                old_loc.fighter = None
                if two_step_move:
                    middle_loc.has_bomb2 = False
                else:
                    new_loc.has_bomb2 = False
                print("An unfortunate move. The enemy had placed a powerful explosive device in this location.\n"
                      "It detonates as you enter, the blast resonating through the surrounding area. \n"
                      "The once rich flora and fauna is left in ruin, and so is your body. Only pieces of your spirit lingers behind.\n"
                      "Perhaps, if fate is on your side, someone might bring you back... for a price.")
                input("Your turn is over. Press Enter to start the next turn.\n")
                return

            elif new_loc.has_fighter and new_loc.fighter.player.number != self.number:
                self.confront_fighter(input_fighter, input_board, input_coord)
                old_loc.has_fighter = False
                old_loc.fighter = None
                input("Your turn is over. Press Enter to start the next turn.\n")
                return

            elif new_loc.has_fighter == False:
                new_loc.has_fighter = True
                new_loc.fighter = input_fighter
                old_loc.has_fighter = False
                old_loc.fighter = None
                input_fighter.position = input_coord
                print(input_fighter.name + " moves to the " + new_loc.kind + " of " + input_coord + ".")
                if input_fighter.bomber or (input_fighter.resser and new_loc.res) or (input_fighter.miner and new_loc.kind == "mountain" and new_loc.has_tunnel == False):
                    use_ability=input("Your fighter has an ability fit for this location. Use it now? Y/N\n").capitalize()
                    while use_ability not in ("Y", "N"):
                        use_ability = input(
                            "Type Y to use this fighter's ability here. Type N to end your turn.\n"
                            "Abilities can only be used at the end of a turn, unless a battle has been fought.\n").capitalize()
                    if use_ability == "Y":
                        self.exec_ability(input_fighter, new_loc)
                input("Your turn is over. Press Enter to start the next turn.\n")
                return
        self.interpretor(input_fighter.name, input_board)

    def exec_ability(self, input_fighter, input_loc):
        if input_fighter.bomber:
            print("You place an explosive device here. It is deadly to anyone on the opposite team.")
            if self.number == 1:
                input_loc.has_bomb1 = True
            else:
                input_loc.has_bomb2 = True
            input_fighter.bomber = False
        elif input_fighter.miner:
            print(input_fighter.name + " has built a tunnel! This mountain is passable for all fighters on both teams.")
            input_loc.has_tunnel = True
            input_loc.speed = 1
            input_fighter.miner = False
        elif input_fighter.resser and input_loc.res:
            dice = random.randrange(1, 300)
            if dice < 50:
                print(input_fighter.name + " takes a step towards the mausoleum, then stops. Something\n"
                "feels different... " + input_fighter.name+"'s gaze go to the sky. Usually full of clouds, tonight \n"
                "it is clear. The stars are out. The air feels crisp. And the crypt abnormally... powerful.")
                time.sleep(3)
            else:
                print("As " + input_fighter.name + " steps unto the crumbling stone stair, from the innards of the crypt a foul wind blows.")
            choice = input("What fighter do you wish to bring back from the dead?\n").capitalize()
            dead_fighter = self.get_fighter(choice)
            while dead_fighter == "" and choice != "L":
                choice = input("Type a dead fighters name to resurrect them, or type L to leave the mausoleum.").capitalize()
                dead_fighter = self.get_fighter(choice)

            if choice != "L" and dead_fighter != "" and dead_fighter.alive:
                print("     That fighter is still alive. The ancient power residing here sniffs at you for making such a mistake.\n"
                    "Are you nervous about giving your life?"
                    "You decide to come back when your head is clear.")

            elif choice != "L" and dead_fighter.alive == False:
                dead_fighter.alive = True
                dead_fighter.bomber = False
                dead_fighter.miner = False
                input_fighter.alive = False
                input_fighter.resser = False
                dead_fighter.position = input_fighter.position
                input_loc.fighter = dead_fighter
                if dice < 50 and dead_fighter.strength == 8:
                    if dead_fighter.name == "Eagle":
                        dead_fighter.name = "Gandalf"
                        dead_fighter.age = "that lives, until the task is done"
                        dead_fighter.kind = "and at dawn... Look to the east."
                    elif dead_fighter.name == "Balrog":
                        dead_fighter.name = "Witch-King of Angmar"
                        dead_fighter.age = "pretty old"
                        dead_fighter.kind = "you fool. The world of men will fall."
                    dead_fighter.strength = 9
                    dead_fighter.dark = True
                    input_loc.res = False
                    print("..")
                    time.sleep(2)
                    print("....")
                    time.sleep(2)
                    print("The ground shakes.")
                    time.sleep(2)
                    print("WHAT did you do?")
                    time.sleep(2)
                    print("From the stars above, lightning strikes. With a deafening, crackling roar the crypt's\n"
                    "roof is no more. Fumes of smoke rise from piles of broken masonry. There, " + input_fighter.name + " is lying,\n"
                    "seemingly unhurt, for his body is without harm, yet without life.")
                    time.sleep(5)
                    print("Someone walks slowly from within the crypt, and while passing the dead body he gives it a glance.\n"
                    "Then, concealed in his robes, he disappears into the night.")
                    time.sleep(2)
                    input("Press Enter to continue.")
                    print(dead_fighter.name + " has been resurrected! With strength not of this world.\n"
                    "Except for bombs, which they are still vulnerable to, they have but one weakness.\n"
                    "What it is, you must find out for yourself...\n")


                else:
                    print(dead_fighter.name + " has been resurrected! They step down through the pool of blood of " + input_fighter.name + " who sacrificed themselves.")
                input_fighter.resser = False
        return

    def confront_fighter(self, input_fighter, input_board, input_coord):
        current_loc = input_board.square[int(input_coord[0]) - 1][self.coord_letter_gen(input_coord[1])]
        attacker = input_fighter
        defender = input_board.square[int(input_coord[0]) - 1][self.coord_letter_gen(input_coord[1])].fighter
        if attacker.strength == 2 and defender.strength == 9:
            if defender.name[0:4] == "Witc":
                print("Eowyn has confronted the Witch-King of Angmar. ")
            elif defender.name[0:4] == "Gand":
                print("Gollum has confronted Gandalf.")

            print(attacker.name + " has won!")
            current_loc.fighter = attacker
            attacker.position = input_coord
            attacker.dark = False
            defender.alive = False
            defender.position = ""
            defender.player.update_life(-1)

        elif attacker.strength > defender.strength:
            print(attacker.name + current_loc.story_enter)
            print(attacker.win)
            input("Press Enter to continue...")
            print(attacker.name + " has confronted " + defender.name + ".")
            print(attacker.name + " has won!")
            current_loc.fighter = attacker
            attacker.position = input_coord
            attacker.dark = False
            defender.alive = False
            defender.position = ""
            defender.player.update_life(-1)
        elif defender.strength > attacker.strength:
            print(attacker.name + current_loc.story_enter)
            print(attacker.defeat)
            input("Press Enter to continue...")
            print(attacker.name + " has confronted " + defender.name + ".")
            print(defender.name + " has won!")
            defender.dark = False
            attacker.alive = False
            attacker.position = ""
            attacker.player.update_life(-1)
        else:
            print(attacker.name + current_loc.story_enter)
            input("Press Enter to continue...")
            print(attacker.name + " has confronted " + defender.name + ".")
            print("Both fighters are dead!")
            current_loc.fighter = None
            current_loc.has_fighter = False
            attacker.alive = False
            attacker.position = ""
            attacker.player.update_life(-1)
            defender.alive = False
            defender.position = ""
            defender.player.update_life(-1)

class Fighter:
    def __init__(self, input_name, input_age, input_creature_kind, input_strength, input_player, input_win = "", input_defeat = ""):
        self.name = input_name
        self.age = input_age
        self.kind = input_creature_kind
        self.strength = input_strength
        self.bomber = False
        self.miner = False
        self.resser = False
        self.player = input_player
        self.dark = True
        self.alive = True
        self.position = ""
        self.win = input_win
        self.defeat = input_defeat

    def __str__(self):
        if self.alive and self.bomber == False and self.resser == False and self.miner == False:
            return f'{self.name}, {self.age}, {self.kind}, with a strength of: {self.strength}'
        elif self.alive == True and self.bomber:
            return f'{self.name}, {self.age}, {self.kind}, with a strength of: {self.strength}\n' \
                   f'       {self.name} is a bomber!'
        elif self.alive == True and self.resser:
            return f'{self.name}, {self.age}, {self.kind}, with a strength of: {self.strength}\n' \
                   f'       {self.name} is a resurrector!'
        elif self.alive and self.miner:
            return f'{self.name}, {self.age}, {self.kind}, with a strength of: {self.strength}\n' \
                   f'       {self.name} is a miner!'
        else:
            return f'{self.name} is dead!'

class Gameboard:
    COORDINATES = '\030[47m'
    END = '\033[0m'
    def __init__(self):
        self.square = []
        rows, cols = 8, 12
        self.watercounter = 0
        self.mountaincounter = 0

        for i in range(rows):
            reser = False
            col = []
            for j in range(cols):
                kind = ""
                dice = 0
                while dice == 0:
                    dice = random.randrange(1, 8)
                    if i > 0 and j > 0:
                        if self.square[(i-1)][j].kind == "mountain" or self.square[(i-1)][(j-1)].kind == "mountain":
                            dice = random.randrange(1, 5)
                            if dice != 1:
                                dice = random.randrange(4, 8)

                        elif self.square[(i-1)][j].kind == "water" or self.square[(i-1)][(j-1)].kind == "water":
                            dice = random.randrange(4, 8)
                            if dice != 7:
                                dice = random.randrange(1, 8)
                    if i in (0, 7):
                        dice = random.randrange(2, 7)

                    if dice == 1 and self.mountaincounter < 10:
                        self.mountaincounter += 1
                        kind = "mountain"
                    elif dice == 2:
                        kind = "forest"
                    elif dice in (3, 4):
                        kind = "plains"
                    elif dice in (5, 6):
                        kind = "hills"
                    elif dice == 7 and self.watercounter < 8:
                        self.watercounter += 1
                        kind = "water"
                    else:
                        dice = 0

                res = False
                if i == 3 or i == 4:
                    if dice != 7:
                        dice = random.randrange(1, 13)
                        if dice > 10 and reser == False:
                            res = True
                            reser = True
                    if j == 11 and reser == False:
                        res = True
                        reser = True

                landscape = Landscape(kind, "temperate", str(i) + str(j), res)
                col.append(landscape)
            self.square.append(col)

    def full_printer(self, input_player, row):
        print("  | ----------------------------------------------------------------------------------------------------------------------------------------------|")
        print(" ", self.square[row][0].print_fighter(input_player), self.square[row][1].print_fighter(input_player), self.square[row][2].print_fighter(input_player), self.square[row][3].print_fighter(input_player),
              self.square[row][4].print_fighter(input_player), self.square[row][5].print_fighter(input_player), self.square[row][6].print_fighter(input_player), self.square[row][7].print_fighter(input_player),
               self.square[row][8].print_fighter(input_player), self.square[row][9].print_fighter(input_player), self.square[row][10].print_fighter(input_player), self.square[row][11].print_fighter(input_player),"|")
        print(str(row+1), self.square[row][0], self.square[row][1], self.square[row][2], self.square[row][3], self.square[row][4],
              self.square[row][5], self.square[row][6], self.square[row][7], self.square[row][8], self.square[row][9], self.square[row][10], self.square[row][11], "|")
        print(" ", self.square[row][0].print_structure(), self.square[row][1].print_structure(),
              self.square[row][2].print_structure(), self.square[row][3].print_structure(),
              self.square[row][4].print_structure(),
              self.square[row][5].print_structure(), self.square[row][6].print_structure(),
              self.square[row][7].print_structure(), self.square[row][8].print_structure(), self.square[row][9].print_structure(), self.square[row][10].print_structure(), self.square[row][11].print_structure(), "|")


    def view_board(self, input_player):
        print("\033[47m         A          B           C           D           E           F           G           H           I           J           K           L     \033[0m ")
        for i in range(8):
            self.full_printer(input_player, i)
        print("  | ----------------------------------------------------------------------------------------------------------------------------------------------|")
        print("\033[47m         A          B           C           D           E           F           G           H           I           J           K           L     \033[0m ")
        print("                                                                 The game board.\n")

class Landscape:
    #os.system('color')
    HILLS = '\033[92m'
    WATER = '\033[44m'
    MOUNTAIN = '\033[100m'
    PLAINS = '\033[33m'
    FOREST = '\033[32m'
    RED = '\033[31m'
    END = '\033[0m'
    #exit=input()

    def __init__(self, input_kind, input_climate, input_coord, input_res=False):
        self.kind = input_kind
        self.climate = input_climate
        self.coord = input_coord
        self.res = input_res
        self.speed = 1
        self.diag = False
        self.has_fighter = False
        self.has_bomb1 = False
        self.has_bomb2 = False
        self.has_tunnel = False
        self.fighter = ""
        self.color = ""
        self.story_enter = ""


        if self.kind == "plains":
            self.speed = 2
            self.diag = True
            self.color = Landscape.PLAINS
            self.story_enter = " rushes out unto the vast fields. The grass wavers in the strong breeze. "

        if self.kind == "hills":
            self.diag = True
            self.speed = 2
            self.color = Landscape.HILLS
            self.story_enter = " enters the hills. It looks like a vast sea of rocks and small, mostly dead trees.\n"

        if self.kind == "mountain":
            self.speed = 0
            self.diag = True
            self.color = Landscape.MOUNTAIN
            self.story_enter = " starts to climb the mountain. Gazing up the towering structure, bad weather starts rolling in."


        if self.kind == "water":
            self.speed = 0
            self.color = Landscape.WATER
        if self.kind == "forest":
            self.speed = 1
            self.diag = True
            self.color = Landscape.FOREST
            self.story_enter = " have reached the forest. The air is thick with anticipation."

    def __str__(self):
        if len(self.kind) == 5:
            return f'|   {self.color}{self.kind[0:5].capitalize()}{Landscape.END}  '
        elif len(self.kind) == 6:
            return f'|  {self.color}{self.kind[0:6].capitalize()}{Landscape.END}  '
        elif len(self.kind) == 7:
            return f'|  {self.color}{self.kind[0:7].capitalize()}{Landscape.END} '
        elif len(self.kind) == 8:
            return f'| {self.color}{self.kind[0:8].capitalize()}{Landscape.END} '

    def print_fighter(self, input_player):
        if self.has_fighter and self.fighter.player.number == input_player.number:
            if len(self.fighter.name) == 5:
                return f'|  {self.fighter.name[0:5].upper()}, {str(self.fighter.strength)}'
            elif len(self.fighter.name) == 6:
                return f'| {self.fighter.name[0:6].upper()}, {str(self.fighter.strength)}'
            elif len(self.fighter.name) >= 7:
                return f'|{self.fighter.name[0:7].upper()}, {str(self.fighter.strength)}'
            elif len(self.fighter.name) >= 8:
                return f'|{self.fighter.name[0:8].upper()},{str(self.fighter.strength)}'

        elif self.has_fighter and self.fighter.player.number != input_player.number and self.fighter.dark:
            return f'|     {Landscape.RED}X{Landscape.END}    '
        elif self.has_fighter and self.fighter.player.number != input_player.number:
            return f'|  {Landscape.RED}{self.fighter.name[0:5].upper()}, {str(self.fighter.strength)}{Landscape.END}'
        else:
            return f'|          '

    def print_structure(self):
        if self.res and self.has_tunnel:
            return f'| MAUS|TUNL'
        elif self.res and self.has_tunnel == False:
            return f'| MAUSOLEUM'
        elif self.has_tunnel:
            return f'|  TUNNEL  '
        else:
            return f'|          '