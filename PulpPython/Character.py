from Abilities import Abilities

__author__ = 'Jessie'


class Character(object):
    space_count = ""
    cut_count = 0

    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, types=None, slot=None, level=None):
        self.types = types
        self.level = level
        self.slot = slot
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.abilities = []

    def allign_attributes(self, name, line, cut):
        self.cut_count += cut
        spacing = ""
        for x in range(0, len(name) - cut):
            if line == 0:
                spacing += " "
            else:
                spacing += "-"
        self.space_count += spacing
        return spacing

    def __str__(self):
        if self.__class__.__name__ == "Leader":
            return "{0} | {1}{2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} \n"\
                   "{10} | {11} |  {12} {13}  |  {14} |  {15} |  {16}  |"\
                   "  {17}  |  {18}   |  {19}   \n" \
                   .format(self.allign_attributes("Leader", 0, 0), "Name",
                           self.allign_attributes(self.name, 0, len("name")),
                           "Health", "Brawl", "Shoot", "Dodge", "Might",
                           "Finesse", "Cunning", "Leader", self.name,
                           self.health, "", self.brawl, self.shoot,
                           self.dodge, self.might, self.finesse, self.cunning)
        elif self.__class__.__name__ == "Sidekick":
            return "{0} | {1}{2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}\n" \
                   "{10} | {11} |  {12} {13}  |  {14}  |  {15}  |  {16}  |"\
                   "  {17}  |   {18}   |  {19}   \n" \
                   .format(self.allign_attributes("Sidekick", 0, 0), "Name",
                           self.allign_attributes(self.name, 0, len("name")),
                           "Health", "Brawl", "Shoot", "Dodge", "Might",
                           "Finesse", "Cunning", "Sidekick", self.name,
                           self.health, " ", self.brawl, self.shoot,
                           self.dodge, self.might, self.finesse, self.cunning)
        elif self.__class__.__name__ == "Ally":
            return "{0} | {1}{2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} \n"\
                   "{10} | {11} |  {12} {13}  |  {14}  |  {15}  |  {16}  |"\
                   "  {17}  |   {18}   |  {19}   \n" \
                   .format(self.allign_attributes("Ally", 0, 0), "Name",
                           self.allign_attributes(self.name, 0, len("name")),
                           "Health", "Brawl", "Shoot", "Dodge", "Might",
                           "Finesse", "Cunning", "Ally", self.name,
                           self.health, " ", self.brawl, self.shoot,
                           self.dodge, self.might, self.finesse, self.cunning)
        elif self.__class__.__name__ == "Follower":
            return "{0} | {1}{2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} \n"\
                   "{10} | {11} |  {12} {13}  |  {14}  |  {15}  |  {16}  |"\
                   "  {17}  |   {18}   |  {19}   \n" \
                   .format(self.allign_attributes("Follower", 0, 0), "Name",
                           self.allign_attributes(self.name, 0, len("name")),
                           "Health", "Brawl", "Shoot", "Dodge", "Might",
                           "Finesse", "Cunning", "Follower", self.name,
                           self.health, " ", self.brawl, self.shoot,
                           self.dodge, self.might, self.finesse, self.cunning)

    def add_ability(self, abilityName):  # Function - to add an ability
        if abilityName == "agile" or abilityName == "Agile":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character's"
                                            " Dodge is increased by +1"
                                            " die.", abilityLevel=1))
            return True
        elif abilityName == "animal" or abilityName == "Animal":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character may"
                                            " not shoot, but adds +1d to two "
                                            "other skills.", abilityLevel=1))
            return True
        elif abilityName == "clever" or abilityName == "Clever":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character's"
                                            " Cunning is increased by +1"
                                            " die", abilityLevel=1))
            return True
        elif abilityName == "fierce" or abilityName == "Fierce":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character's"
                                            " Brawl is increased by +1"
                                            " die.", abilityLevel=1))
            return True
        elif abilityName == "marksman" or abilityName == "Marksman":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character's"
                                            " Shoot is increased by +1"
                                            " die.", abilityLevel=1))
            return True
        elif abilityName == "mighty" or abilityName == "Mighty":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character's"
                                            " Might is increased by +1"
                                            " die.", abilityLevel=1))
            return True
        elif abilityName == "savvy" or abilityName == "Savvy":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character's"
                                            " Finesse is increased by +1"
                                            " die.", abilityLevel=1))
            return True
        elif abilityName == "speedy" or abilityName == "Speedy":
            self.abilities.append(Abilities(abilityName,
                                            abilityEffect="This character may"
                                            " run up to 15\" - instead of"
                                            " 12\".", abilityLevel=1))
            return True
        elif abilityName == "athletic" or abilityName == "Athletic":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " shift this character's"
                                                " dice-type up when rolling"
                                                " for Might or"
                                                " Finesse.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "brute" or abilityName == "Brute":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " this character may re-roll"
                                                " one Brawl or Might"
                                                " die.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "crafty" or abilityName == "Crafty":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " this character may re-roll "
                                                " one Dodge or Cunning"
                                                " die.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "daredevil" or abilityName == "Daredevil":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " this character receives a"
                                                " +1d bonus when rolling for a"
                                                " Peril.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "eagle-eyed" or abilityName == "Eagle-Eyed":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " close range is 12\", and"
                                                " their long range is 48\""
                                                "-instead of 6\" and24\".",
                                                abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "finagler" or abilityName == "Finagler":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " shift this character's "
                                                "dice-type up when rolling for"
                                                " Finesse or Cunning.",
                                                abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "intrepid" or abilityName == "Intrepid":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " may move in any direction"
                                                " when they successfully dodge"
                                                " an attack or peril.",
                                                abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "sharp" or abilityName == "Sharp":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " this character may re-roll"
                                                " one Shoot or Finesse"
                                                " die.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "specialist" or abilityName == "Specialist":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " shift this character's"
                                                " dice-type up when rolling"
                                                " for Cunning or Might.",
                                                abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "stealthy" or abilityName == "Stealthy":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character "
                                                " may hide as an action"
                                                " - instead of a full"
                                                " action.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "astute" or abilityName == "Astute":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character'"
                                                " Shoot and Finesse"
                                                " dice-type are not lowered"
                                                " due to injuries.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "brash" or abilityName == "Brash":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " is not limited to rushing"
                                                " the closest enemy.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "deadeye" or abilityName == "Deadeye":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " is not limited to shooting"
                                                " the closest enemy.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "deductive" or abilityName == "Deductive":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="As an action"
                                                " for this character, you may"
                                                " draw one Fortune card.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "hardened-veteran" or abilityName == "Hardened"\
                                                                 "-Veteran":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " ignores the multiple combats"
                                                " penalty.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "indomitable" or abilityName == "Indomitable":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " may re-roll one Recovery"
                                                " check per turn.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "muscle-of-steel" or abilityName == "Muscle-"\
                                                                "Of-Steel":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " Brawl and Might dice-type"
                                                " are not lowered due to "
                                                " injuries.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "shrewd" or abilityName == "Shrewd":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="This character"
                                                " Dodge and Cunning dice-type"
                                                " are not lowered due to"
                                                " injuries.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "quick-shot" or abilityName == "Quick-Shot":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " this character may shift"
                                                " their shooting dice-type"
                                                " down to gain a +2d bonus"
                                                " only against targets in"
                                                " close range.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "quick-strike" or abilityName == "Quick-Strike":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="Once per turn,"
                                                " this character may shift"
                                                " their brawling dice-type"
                                                " down to gain a +2d bonus.",
                                                abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "lucky-devil" or abilityName == "Lucky-Devil":
            if self.level >= 4:
                self.abilities.append(Abilities(abilityName,
                                                abilityEffect="When this"
                                                " leader activates, the"
                                                " opponent may not play any"
                                                " Fortune cards.",
                                                abilityLevel=4))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        else:
            print("***Ability Does Not Exist!***")
            return False

    def display_ability(self):  # display the abilities of a specific character
        for i in self.abilities:
            print(Abilities.__str__(i))


class Leader(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, ability1, ability2, ability3, types="Leader",
                 slot=0, level=4):
        Character.__init__(self, name, health, brawl, shoot, dodge, might,
                           finesse, cunning, types, slot, level)
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.abilities = []


class Sidekick(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, ability1, ability2, ability3, types="S.kick",
                 slot=3, level=3):
        Character.__init__(self, name, health, brawl, shoot, dodge, might,
                           finesse, cunning, types, slot, level)
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.abilities = []


class Ally(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, ability1, ability2, types="Ally",
                 slot=2, level=2):
        Character.__init__(self, name, health, brawl, shoot, dodge, might,
                           finesse, cunning, types, slot, level)
        self.ability1 = ability1
        self.ability2 = ability2
        self.abilities = []


class Follower(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, ability1, types="Follower", slot=1, level=1):
        Character.__init__(self, name, health, brawl, shoot, dodge, might,
                           finesse, cunning, types, slot, level)
        self.ability1 = ability1
        self.abilities = []
