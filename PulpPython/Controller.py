import cmd
import doctest
import pickle
import os
import unittest
import sys
from Character import Follower, Ally, Sidekick, Leader
from League import League

__author__ = 'Jessie'
# -------------------------------------------------------------------------------
# Name:        Pulp Alley - Character Sheet
# Purpose:     PR301 - Assignment 1
# Author:      Jessie Velano
# Created:     05/08/2015
# Copyright:
# Licence:
# -------------------------------------------------------------------------------


# just a line separator
def print_separator():
    print("-------------------------------------------------------------")


# Controller Class
class Controller(cmd.Cmd):
    leagues = None
    hasLeague = None
    hasLeader = None

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "\nEnter Command: "
        print_separator()
        print("      Welcome to Pulp Alley Character Sheet Creator \n" +
              "Type 'about' for more info or 'help' for available commands ")
        print_separator()
        self.leagues = League(self)
        self.hasLeader = False
        self.hasLeague = False

    def do_about(self, line):
        """
        ---About---
        - Tells user more about the application
        """
        display_about()

    def do_league(self, line):
        """
        ---League---
        league [leagueName]
        - Create a league that contains the characters
        - a league contains 10 slots
        - leagueName cannot be empty!
        - E.g.: league Avengers
        """
        try:
            if line == "":
                raise InvalidActionError("***League name cannot be empty!***")
            elif self.hasLeague is True:
                raise InvalidActionError("***A League Is Already Created!***")
            else:
                self.leagues = League(line)
                print("***League " + line + " is created!***")
                self.hasLeague = True
        except InvalidActionError as err:
            print(err)

    def do_leader(self, line):
        """
        ---Leader---
        leader [name heal braw sho dod mig fin cun ability1 ability2 ability3]
        - Command to create a leader
        - A league can only have one leader
        - A leader doesn't occupy a slot
        - A leader can possess abilities of any level
        - Input complete values or else you'll get an error
        - E.g.: leader Boss d10 3d10 4d10 3d10 2d8 3d8 2d10 Agile Deadeye Shrewd
        """
        leader(self, line)


    def do_sidekick(self, line):
        """
        ---Side Kick---
        sidekick [name health brawl shoot dodge might finesse cunning ability]
        - Command to create a sidekick
        - A sidekick occupies 3 slots
        - A sidekick can possess level 1 to 3 abilities
        - Input complete values or else you'll get an error
        - E.g.: sidekick Magneto d8 3d8 3d8 2d6 2d8 3d8 2d6 Savvy Sharp Brute
        """
        sidekick(self, line)

    def do_ally(self, line):
        """
        ---Ally---
        ally [name health brawl shoot dodge might finesse cunning ability]
        - Command to create a ally
        - An ally occupies 2 slots
        - An ally can possess level 1 to 2 abilities
        - Input complete values or else you'll get an error
        - E.g.: ally IronMan d6 2d6 3d6 1d6 2d8 1d6 1d6 Athletic finagler
        """
        ally(self, line)

    def do_follower(self, line):
        """
        ---Follower---
        follower [name health brawl shoot dodge might finesse cunning ability]
        - Command to create a Follower
        - A Follower occupies 1 slot
        - A Follower can possess level 1 abilities
        - Input complete values or else you'll get an error
        - E.g.: follower Hulk d6 1d6 1d6 2d6 1d6 2d6 1d6 Mighty
        """
        follower(self, line)

    def do_save(self, line):
        """
            save [file name]
            - Save the Character sheet
            - E.g.: save sampleFile
        """
        save(self, line)

    def do_load(self, line):
        """
            load [file name]
            - load the saved character sheet
            - E.g.: load sampleFile
        """
        load(self, line)

    def do_display(self, line):
        """
        ---Display---
        Display the League and the Characters and their Abilities
        """
        l = self.leagues
        l.display_league()
        l.display_chars()

    def do_restart(self, line):
        """
            restart
            - Empty the character sheet
        """
        self.leagues = League(self)


class InvalidActionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Invalid Action: " + self.value)


def display_about():
    """
    >>> display_about()
    -------------------------------------------------------------
        Welcome to Pulp Alley Character Sheet Creator
                  Created by Jessie Velano
    <BLANKLINE>
         This application will let you create your own
      Character sheet which contains league that is composed
    of a Leader, Sidekick, Ally, and Follower, You cant create
         or add a character if you have'nt created a league.
    -------------------------------------------------------------
    """
    print_separator()
    print("    Welcome to Pulp Alley Character Sheet Creator\n" +
          "              Created by Jessie Velano\n\n"
          "     This application will let you create your own\n" +
          "  Character sheet which contains league that is composed\n" +
          "of a Leader, Sidekick, Ally, and Follower, You cant create\n" +
          "     or add a character if you have'nt created a league.")
    print_separator()


def add_league(self, leagueName):
    """
    >>> add_league(Controller,"FIRST")
    ***League FIRST is created!***
    >>> add_league(Controller,"SECOND")
    'Invalid Action: ***A League Is Already Created!***'
    >>> add_league(Controller,"THIRD")
    'Invalid Action: ***A League Is Already Created!***'
    """
    try:
        if leagueName == "":
            raise InvalidActionError("***League name cannot be empty!***")
        elif self.hasLeague is True:
            raise InvalidActionError("***A League Is Already Created!***")
        else:
            self.leagues = League(leagueName)
            print("***League " + leagueName + " is created!***")
            self.hasLeague = True
    except InvalidActionError as err:
        print(err)


def leader(self, line):
    """
    >>> leader(Controller,"Boss2 d10 3d10 4d10 3d10 2d8 3d8 2d10 Animal Sharp ASDS")
    ***Ability Does Not Exist!***
    ***Leader Not Created!***
    >>> leader(Controller,"Boss d10 3d10 4d10 3d10 2d8 3d8 2d10 Agile Deadeye Shrewd")
    ***Leader 'Boss' is created!***
    >>> leader(Controller,"Boss2 d10 3d10 4d10 3d10 2d8 3d8 2d10 Animal Sharp Stealthy")
    'Invalid Action: ***A Leader Is Already Created!***'
    """
    l = self.leagues
    try:
        if self.hasLeader is True:
            raise InvalidActionError("***A Leader Is Already Created!***")
        elif self.hasLeader is False and self.hasLeague is False:
            raise InvalidActionError("***Create a League First!***")
        else:
            try:
                arg = line.split(" ")
                if len(arg) < 11:
                    raise InvalidActionError("***Incomplete Input!***")
                elif len(arg) > 11:
                    raise InvalidActionError("***Excess Input!***")
                else:
                    if l.add_leader(arg[0], arg[1], arg[2], arg[3], arg[4],
                                    arg[5], arg[6], arg[7], arg[8],
                                    arg[9], arg[10]) is True:
                        self.hasLeader = True
                        print("***Leader '{}' is created!***".
                                format(arg[0]))
                    else:
                        print("***Leader Not Created!***")
            except InvalidActionError as err2:
                print(err2)
    except InvalidActionError as err:
        print(err)


def sidekick(self, line):
    """
    >>> sidekick(Controller,"HULK d8 3d8 3d8 2d6 2d8 3d8 2d6 Lucky-Devil Animal Mighty")
    ***Character Level Is Too Low!***
    ***Sidekick Not Created!***
    >>> sidekick(Controller,"HULK d8 3d8 3d8 2d6 2d8 3d8 2d6 ASD Animal Mighty")
    ***Ability Does Not Exist!***
    ***Sidekick Not Created!***
    >>> sidekick(Controller,"IronMan d8 3d8 3d8 2d6 2d8 3d8 2d6 Specialist Deadeye Shrewd")
    ***Sidekick 'IronMan' is created!***
    >>> sidekick(Controller,"HULK d8 3d8 3d8 2d6 2d8 3d8 2d6 Brute Animal Mighty")
    'Invalid Action: ***Insufficient League Slot***'
    """
    l = self.leagues
    try:
        if self.hasLeague is False:
            raise InvalidActionError("***Create League First!***")
        elif l.leagueSlot < 3:
            raise InvalidActionError("***Insufficient League Slot***")
        elif self.hasLeader is False:
            raise InvalidActionError("***Create A Leader First!***")
        else:
            try:
                arg = line.split(" ")
                if len(arg) < 11:
                    raise InvalidActionError("***Incomplete Input!***")
                elif len(arg) > 11:
                    raise InvalidActionError("***Excess Input!***")
                else:
                    if l.add_sidekick(arg[0], arg[1], arg[2], arg[3],
                                      arg[4], arg[5], arg[6], arg[7],
                                      arg[8], arg[9], arg[10]) is True:
                        print("***Sidekick '{}' is created!***".
                                format(arg[0]))
                    else:
                        print("***Sidekick Not Created!***")
            except InvalidActionError as err2:
                print(err2)
    except InvalidActionError as err:
        print(err)


def ally(self, line):
    """
    >>> ally(Controller,"Vision d6 2d6 3d6 1d6 2d8 1d6 1d6 Savvy Quick-Shot")
    ***Character Level Is Too Low!***
    ***Ally Not Created!***
    >>> ally(Controller,"Vision d6 2d6 3d6 1d6 2d8 1d6 1d6 ASDASDS ASDADSADS")
    ***Ability Does Not Exist!***
    ***Ally Not Created!***
    >>> ally(Controller,"HawkEye d6 2d6 3d6 1d6 2d8 1d6 1d6 Marksman Speedy")
    ***Ally 'HawkEye' is created!***
    >>> ally(Controller,"BWidow d6 2d6 3d6 1d6 2d8 1d6 1d6 Savvy Agile")
    ***Ally 'BWidow' is created!***
    """
    l = self.leagues
    try:
        if self.hasLeague is False:
            raise InvalidActionError("***Create League First!***")
        elif l.leagueSlot < 2:
            raise InvalidActionError("***Insufficient League Slot***")
        elif self.hasLeader is False:
            raise InvalidActionError("***Create A Leader First!***")
        else:
            try:
                arg = line.split(" ")
                if len(arg) < 10:
                    raise InvalidActionError("***Incomplete Input!***")
                elif len(arg) > 10:
                    raise InvalidActionError("***Excess Input!***")
                else:
                    if l.add_ally(arg[0], arg[1], arg[2], arg[3], arg[4],
                                  arg[5], arg[6], arg[7], arg[8],
                                  arg[9]) is True:
                        print("***Ally '{}' is created!***".format(arg[0]))
                    else:
                        print("***Ally Not Created!***")
            except InvalidActionError as err2:
                print(err2)
    except InvalidActionError as err:
        print(err)


def follower(self, line):
    """
    >>> follower(Controller,"Vision d6 1d6 1d6 2d6 1d6 2d6 1d6 Intrepid")
    ***Character Level Is Too Low!***
    ***Follower Not Created!***
    >>> follower(Controller,"Vision d6 1d6 1d6 2d6 1d6 2d6 1d6 ASDASDS")
    ***Ability Does Not Exist!***
    ***Follower Not Created!***
    >>> follower(Controller,"CAP d6 1d6 1d6 2d6 1d6 2d6 1d6 Fierce")
    ***Follower 'CAP' is created!***
    >>> follower(Controller,"AntMan d6 1d6 1d6 2d6 1d6 2d6 1d6 Agile")
    ***Follower 'AntMan' is created!***
    """
    l = self.leagues
    try:
        if self.hasLeague is False:
            raise InvalidActionError("***Create League First!***")
        elif l.leagueSlot < 1:
            raise InvalidActionError("***Insufficient League Slot!***")
        elif self.hasLeader is False:
            raise InvalidActionError("***Create A Leader First!***")
        else:
            try:
                arg = line.split(" ")
                if len(arg) < 9:
                    raise InvalidActionError("***Incomplete Input!***")
                elif len(arg) > 9:
                    raise InvalidActionError("***Excess Input!***")
                else:
                    if l.add_follower(arg[0], arg[1], arg[2], arg[3],
                                      arg[4], arg[5], arg[6], arg[7],
                                      arg[8]) is True:
                        print("***Follower '{}' is created!***".
                                format(arg[0]))
                    else:
                        print("***Follower Not Created!***")
            except InvalidActionError as err2:
                print(err2)
    except InvalidActionError as err:
        print(err)


def save(self, file_name):
    """
    >>> save(Controller, "sampleTest")
    File saved as 'sampleTest.pickle'
    >>> save(Controller, "")
    'Invalid Action: You must specify a file name.'
    """
    try:
        if file_name == "":
            raise InvalidActionError("You must specify a file name.")
        else:
            data = [self.leagues]
            with open(file_name + ".pickle", "wb") as save_file:
                pickle.dump(data, save_file)
            print("File saved as '" + file_name + ".pickle'")
    except InvalidActionError as err:
        print(err)


def load(self, file_name):
    """
    >>> load(Controller, "")
    'Invalid Action: ***You Must Specify A File Name.***'
    >>> load(Controller, "sampleTest-Fake")
    'Invalid Action: Specified file "sampleTest-Fake" does not exist'
    >>> load(Controller, "sampleTestLoad")
    ***Character Sheet is Loaded From sampleTestLoad.pickle***
    """
    try:
        if file_name == "":
            raise InvalidActionError("***You Must Specify A File Name.***")
        if not os.path.exists(file_name + ".pickle"):
            raise InvalidActionError("Specified file \"" + file_name +
                                    "\" does not exist")
        with open(file_name + ".pickle", "rb") as saved_game:
            data = pickle.load(saved_game)
        self.leagues = data[0]
        print("***Character Sheet is Loaded From " + file_name + ".pickle***")
    except InvalidActionError as err:
        print(err)


class MainTest(unittest.TestCase):

    def test_create_league(self):
        self.leagues = League("Avengers")

    def test_create_leader(self):
        # Create a League First then Try to create a Leader
        self.leagues = League("Avengers")
        # Test - Create a Leader
        self.assertTrue(self.leagues.add_leader("Fury", "11", "22", "33", "44",
                                                "55", "66", "77", "animal",
                                                "shrewd", "brute"), Leader)

    def test_create_sidekick(self):
        # Create a League First and a leader
        self.leagues = League("Avengers")
        self.leagues.add_leader("Fury", "11", "22", "33", "44", "55", "66",
                                "77", "animal", "shrewd", "brute")
        # Test - Create a Sidekick
        self.assertTrue(self.leagues.add_sidekick("IronMan", "11", "22", "33",
                                                  "44", "55", "66", "77",
                                                  "savvy", "specialist",
                                                  "Quick-Strike"), Sidekick)

    def test_create_ally(self):
        # Create a League First and a leader
        self.leagues = League("Avengers")
        self.leagues.add_leader("Fury", "11", "22", "33", "44", "55", "66",
                                "77", "animal", "shrewd", "brute")
        # Test - Create an Ally
        self.assertTrue(self.leagues.add_ally("Thor", "11", "22", "33", "44",
                                              "55", "66", "77", "Brute",
                                              "Animal"), Ally)

    def test_create_follower(self):
        # Create a League First and a leader
        self.leagues = League("Avengers")
        self.leagues.add_leader("Fury", "11", "22", "33", "44", "55", "66",
                                "77", "animal", "shrewd", "brute")
        # Test - Create a Follower
        self.assertTrue(self.leagues.add_follower("Hawk", "11", "22", "33",
                                                  "44", "55", "66", "77",
                                                  "agile"), Follower)

    def test_duplicate_league(self):
        # Test when creating a league if its already created/present
        self.leagues = League("Avengers")
        self.hasLeague = True
        # Test - Create a Duplicate League here
        self.assertRaises(InvalidActionError,
                          Controller.do_league(self, "Avengers2"))

    def test_duplicate_leader(self):
        # Test when creating a leader if its already created/present
        self.leagues = League("Avengers")
        self.hasLeader = True
        line = "Fury 11 22 33 44 55 66 77 animal shrewd brute"
        # Test - Create a Duplicate Leader here
        self.assertRaises(InvalidActionError,
                          Controller.do_leader(self, line))

    def test_create_sidekick_without_leader(self):
        self.leagues = League("Avengers")
        self.hasLeague = True
        self.hasLeader = False
        line = "Vision 11 22 33 44 55 66 77 agile animal stealthy"
        # Test - Create a Follower without a leader
        self.assertRaises(InvalidActionError,
                          Controller.do_sidekick(self, line))

    def test_create_ally_without_leader(self):
        self.leagues = League("Avengers")
        self.hasLeague = True
        self.hasLeader = False
        line = "Spiderman 11 22 33 44 55 66 77 agile animal"
        # Test - Create a Follower without a leader
        self.assertRaises(InvalidActionError,
                          Controller.do_ally(self, line))

    def test_create_follower_without_leader(self):
        self.leagues = League("Avengers")
        self.hasLeague = True
        self.hasLeader = False
        line = "Hawk 11 22 33 44 55 66 77 agile"
        # Test - Create a Follower without a leader
        self.assertRaises(InvalidActionError,
                          Controller.do_follower(self, line))

    def test_incomplete_input(self):
        # Test when creating a character with incomplete input value
        self.leagues = League("Avengers")
        self.hasLeague = True
        self.hasLeader = True
        line = "Fury 11 22 33 44 55 66 77 animal"
        # Test - One ability is missing
        self.assertRaises(InvalidActionError, Controller.do_ally(self, line))

    def test_excess_input(self):
        # Test when creating a character with incomplete input value
        self.leagues = League("Avengers")
        self.hasLeague = True
        self.hasLeader = True
        line = "Fury 11 22 33 44 55 66 77 animal agile"
        # Test - One excess ability
        self.assertRaises(InvalidActionError,
                          Controller.do_follower(self, line))

    def test_league_slot(self):
        # Test league if it can only hold 10 slots
        # Create a league first and then the characters
        self.leagues = League("Avengers")
        self.hasLeader = True
        self.hasLeague = True
        line1 = "Fury 11 22 33 44 55 66 77 animal agile shrewd"
        Controller.do_leader(self, line1)
        line2 = "Cap 11 22 33 44 55 66 77 savvy brute quick-shot"
        Controller.do_sidekick(self, line2)
        line3 = "IronMan 11 22 33 44 55 66 77 stealthy intrepid"
        Controller.do_ally(self, line3)
        line4 = "Hawk 11 22 33 44 55 66 77 animal"
        Controller.do_follower(self, line4)
        line5 = "Magneto 11 22 33 44 55 66 77 sharp finagler"
        Controller.do_ally(self, line5)
        line6 = "P.X. 11 22 33 44 55 66 77 specialist clever"
        Controller.do_ally(self, line6)
        # 10 slot is already occupied - Test if we can still add 1 follower
        line7 = "Wolverine 11 22 33 44 55 66 77 Fierce"
        self.assertRaises(InvalidActionError,
                          Controller.do_follower(self, line7))

    def test_save_error(self):
        # Test - Save with no name given
        self.assertRaises(InvalidActionError, Controller.do_save(self, ""))

    def test_load_error(self):
        # Test - Load with no name given
        self.assertRaises(InvalidActionError, Controller.do_load(self, ""))

    def test_load_unknown(self):
        # Test - Load with non-existing file
        self.assertRaises(InvalidActionError, Controller.do_load(self,"Unknown"))

    def test_ability_level(self):
        # Create a League First and a leader
        self.leagues = League("Avengers")
        self.leagues.add_leader("Fury", "11", "22", "33", "44", "55", "66",
                                "77", "animal", "shrewd", "brute")
        self.hasLeader = True
        self.hasLeague = True
        # Test - Level of ability and char is not matched
        line = "Wolverine 11 22 33 44 55 66 77 Brute"
        self.assertRaises(InvalidActionError,
                          Controller.do_follower(self, line))

    def test_ability_exist(self):
        # Create a League First and a leader
        self.leagues = League("Avengers")
        self.leagues.add_leader("Fury", "11", "22", "33", "44", "55", "66",
                                "77", "animal", "shrewd", "brute")
        self.hasLeader = True
        self.hasLeague = True
        # Test - Ability doesnt exist
        line = "Wolverine 11 22 33 44 55 66 77 HOHOHO"
        self.assertRaises(InvalidActionError,
                          Controller.do_follower(self, line))

# PRETTY PRINT
def handle_command_line_switch():
    try:
        if len(sys.argv) == 3 and sys.argv[1] == "-l":
            print("load game")
            load(sys.argv[2])
            return
        raise InvalidActionError("Switch or argument not supported.")
    except InvalidActionError as err:
        print(err)

def main():
    # doctest.testmod(verbose=True)
    # handle_command_line_switch()
    control = Controller()
    control.cmdloop()

if __name__ == '__main__':
    # unittest.main()
    main()
