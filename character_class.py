import random
from randomization_data import Data
from tkinter import *

data = Data()

class character:
    'D&D character'
    
    def __init__(self, strength = 10, dexterity = 10, constitution = 10, intelligence = 10, wisdom = 10, charisma = 10,
    gender = None, race = None, appearence = None, talents = None, manneirisms = None, interaction_trait = None, 
    ideals = None, bonds = None, flaws = None, voice_speed = None, voice_pitch = None, vocal_texture = None, vocal_patterns = None, voice_manneirisms = None):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.gender = gender
        self.race = race
        self.appearence = appearence
        self.talents = talents
        self.manneirisms = manneirisms
        self.interaction_trait = interaction_trait
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.voice_speed = voice_speed
        self.voice_pitch = voice_pitch
        self.vocal_texture = vocal_texture
        self.vocal_patterns = vocal_patterns
        self.voice_manneirisms = voice_manneirisms
       
    
    def generate_stat(self):
        rolls = []
        rolls.append(random.randint(1, 6))
        rolls.append(random.randint(1, 6))
        rolls.append(random.randint(1, 6))
        rolls.append(random.randint(1, 6))
        rolls.sort()
        del rolls[0]
        return sum(rolls)
    
    def randomize_strength(self): 
        self.strength = self.generate_stat()
        
    def randomize_dexterity(self):
        self.dexterity = self.generate_stat()

    def randomize_constitution(self):
        self.constitution = self.generate_stat()
    
    def randomize_intelligence(self):
        self.intelligence = self.generate_stat()
    
    def randomize_wisdom(self):
        self.wisdom = self.generate_stat()
    
    def randomize_charisma(self):
        self.charisma = self.generate_stat()

    def randomize_gender(self):
        self.gender = random.choice(('Male', 'Female'))

    def randomize_race(self):
        self.race = random.choices(population = data.races,
          weights = [0.01, 0.04, 0.07, 0.03, 0.08, 0.1, 0.05, 0.13, 0.01, 0.01, 0.01, 0.02, 0.01, 0.03, 
          0.1, 0.5, 0.3, 0.1, 0.2, 0.1, 0.5, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2])
    
    def randomize_appearence(self):
        self.appearence = random.choice(data.appearence)
    
    def randomize_talents(self):
        self.talents = random.choice(data.talents)
    
    def randomize_manneirisms(self):
        self.manneirisms = random.choice(data.manneirisms)
    
    def randomize_interaction_trait(self):
        self.interaction_trait = random.choice(data.interaction_trait)
    
    def randomize_ideals(self):
        ideals_list = random.choice(data.ideals)
        self.ideals = random.choice(ideals_list)
        
        if 'Good' in self.ideals or 'Evil' in self.ideals:
            ideals_list = random.choices(population = data.ideals, weights = [0, 0.25, 0, 0.25, 0.25, 0.25 ])
            self.ideals += ' | ' + str(random.choice(ideals_list))
        
        elif 'Lawful' in self.ideals or 'Chaotic' in self.ideals:
            ideals_list = random.choices(population = data.ideals, weights = (0.25, 0.25, 0.25, 0, 0, 0.25))
            self.ideals += ' | ' + str(random.choice(ideals_list))
        
        elif 'Other' in self.ideals:
            ideals_list = random.choices(population = data.ideals, weights = (0.2, 0.2, 0.2, 0.2, 0.2, 0))
            self.ideals += ' | ' + str(random.choice(ideals_list))
       
        else:
            selected_ideal = self.ideals
            while self.ideals == selected_ideal:
                ideals_list = random.choice(data.ideals)
                selected_ideal = random.choice(ideals_list)
            self.ideals += ' | ' + selected_ideal
    
    def randomize_bonds(self):
        self.bonds = random.choice(data.bonds)

    def randomize_flaws(self):
        self.flaws = random.choice(data.flaws)
    
    def randomize_voice_speed(self):
        self.voice_speed = random.choice(['Slow', 'Medium', 'Fast'])
    
    def randomize_voice_pitch(self):
        self.voice_pitch = random.choice(['Low', 'Medium', 'High'])

    def randomize_vocal_texture(self):
        self.vocal_texture = random.choice(data.vocal_textures)

    def randomize_vocal_patterns(self):
        self.vocal_patterns = random.choice(data.vocal_patterns)

    def randomize_stats(self):
        self.randomize_strength()
        self.randomize_dexterity()
        self.randomize_constitution()
        self.randomize_intelligence()
        self.randomize_wisdom()
        self.randomize_charisma()
    
    def randomize_personality_trait(self):
        self.randomize_appearence()
        self.randomize_talents()
        self.randomize_manneirisms()
        self.randomize_interaction_trait()
        self.randomize_ideals()
        self.randomize_bonds()
        self.randomize_flaws()
    
    def randomize_voice_traits(self):
        self.randomize_voice_speed()
        self.randomize_voice_pitch()
        self.randomize_vocal_texture()
        self.randomize_vocal_patterns()
    
    def randomize_all(self):
        self.randomize_stats()
        self.randomize_gender()
        self.randomize_race()
        self.randomize_personality_trait()
        self.randomize_voice_traits()