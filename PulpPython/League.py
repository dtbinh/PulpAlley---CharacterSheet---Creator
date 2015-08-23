from Character import Character, Leader, Sidekick, Follower, Ally

__author__ = 'Jessie'


def print_separator():
    print("----------------------------------------------------------------"
          "-----------------")


def print_separator2():
    print("-------------------------------------------------------------")


class League(object):
    def __init__(self, leagueName):
        self.leagueName = leagueName
        self.leagueSlot = 10
        self.characters = []

    # Function - To create a leader

    def add_leader(self, name, health, brawl, shoot, dodge, might, finesse,
                   cunning, abilityName1, abilityName2, abilityName3):
        l = Leader(name, health, brawl, shoot, dodge, might, finesse, cunning,
                   abilityName1, abilityName2, abilityName3, types="Leader",
                   slot=0, level=4)
        if l.add_ability(abilityName1) is True and l.add_ability(abilityName2)\
           is True and l.add_ability(abilityName3) is True:
            self.characters.append(l)
            return True
        else:
            return False

    # Function - To create a sidekick

    def add_sidekick(self, name, health, brawl, shoot, dodge, might, finesse,
                     cunning, abilityName1, abilityName2, abilityName3):
        s = Sidekick(name, health, brawl, shoot, dodge, might, finesse,
                     cunning, abilityName1, abilityName2, abilityName3,
                     types="Sidekick", slot=3, level=3)
        if s.add_ability(abilityName1) is True and s.add_ability(abilityName2)\
           is True and s.add_ability(abilityName3) is True:
            self.characters.append(s)
            self.leagueSlot -= 3
            return True
        else:
            return False

    # Function - To create an Ally

    def add_ally(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, abilityName1, abilityName2):
        a = Ally(name, health, brawl, shoot, dodge, might, finesse, cunning,
                 abilityName1, abilityName2, types="  Ally", slot=2, level=2)
        if a.add_ability(abilityName1) is True and a.add_ability(abilityName2)\
           is True:
            self.characters.append(a)
            self.leagueSlot -= 2
            return True
        else:
            return False

    # Function - To create a Follower

    def add_follower(self, name, health, brawl, shoot, dodge, might, finesse,
                     cunning, abilityName):
        f = Follower(name, health, brawl, shoot, dodge, might, finesse,
                     cunning, abilityName, types="Follower", slot=1, level=1)
        if f.add_ability(abilityName) is True:
            self.characters.append(f)
            self.leagueSlot -= 1
            return True
        else:
            return False

    def display_league(self):  # Displays League Name and available Slots
        print_separator()
        print("                      {} -  "
              "Available Slots: {}".format(self.leagueName, self.leagueSlot))
        # print_separator()
        # print_fields()

    def display_chars(self):  # Displays all characters and their abilities
        for i in self.characters:
            print_separator()
            print(Character.__str__(i))
            Follower.display_ability(i)
        print_separator()
