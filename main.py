#AAAAAaaaaaa

#What am I doing its been a while

#This is a d100 Roleplaying System

if __name__ == "__main__":
    main_loop()

// Start the game parameters
def Character(object):
    def __init__(self):
        self.name = ""

        self.current_age = "" # Expect a date string and character's current age in years, months, weeks and days
        self.current_time = "" # Expect a date string and the era that the character is being played in

        self.gender = "" # Expect Male, Female or ?

        self.jobs = [] # Expect all character jobs and levels at those professions. # E.G. ["MagicianLv2, MathTutorLv3 etc...

        self.gifts = [] # Rare bonus. Literally only positive. Everyone gets ONE GIFT.
        self.traits = [] # CHARACTER CREATION ONLY. Things that are both positive and negative. E.G. "Small frame from Fallout"
        self.skills = {} # Skills related to their skill ranks. (Higher number = More Skilled)
        self.feats = [] # Special abilities gained only through life experience.


        ## Character Statistics (Numbers)
        self.health = None # Expect a health related object
        self.wallet = None # Expect a financials related object

        ## Character Info
        self.morals = None # Character morals object. It's kinda like humanity in vampire
        self.personality = None # Character personality object with traits # E.G. ["Funny, Trusting, Suspicious"]
        self.genetics = None # Character traits passed down from parents

        ## Special
        self.inventory = None # Expect an inventory object

        # Game Statistics, these get overwritten by the update() procedure
        self.xp = -1
        self.current_hp = -1
        self.max_hp = -1

        self.alive = None # When initialized, this will become True or False

def main_loop():
    print("Hello world!")
    c = Character()